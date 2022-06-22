import streamlit as st
st.set_page_config(
    page_title="SOM-Inventory",
)
import streamlit.components.v1 as components
import pandas as pd
import requests


from io import BytesIO
from inventorydata import InventoryData
from PIL import Image
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from streamlit_option_menu import option_menu

class SomInventory:

    def inventory_list(url):
        #pd.set_option('display.max_colwidth', None)
        index_title = None
        data = None
        rows = InventoryData.load_data(url)
        
        @st.cache
        def convert_df(df):
            return df.to_csv().encode('utf-8')
        
        with st.sidebar:
            selected = option_menu("Inventory", ["All", "Apparatus", "Equipments", "Instruments", "Models", "Models Gallery", "Lab Supplies", "Office Supplies", "Tools"], 
                icons=["journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical"], menu_icon="calendar4-week", default_index=0)
        
        if selected == "All":
            data = pd.DataFrame(rows)
            index_title = "All"
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
                
        elif selected == "Apparatus":
            data = pd.DataFrame(rows)
            index_title = "Apparatus"
            data = data[data['Category'] == "Apparatus"]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]

        elif selected == "Equipments":
            data = pd.DataFrame(rows)
            index_title = "Equipments"
            data = data[data['Category'] == "Equipments"]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]

        elif selected == "Instruments":
            data = pd.DataFrame(rows)
            index_title = "Instruments"
            data = data[data['Category'] == "Instruments"]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]

        elif selected == "Models":
            data = pd.DataFrame(rows)
            index_title = "Models"
            data = data[data['Category'] == "Models"]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]
        
        elif selected == "Models Gallery":
            st.write("Under Maintenance")
            
            
        elif selected == "Lab Supplies":
            data = pd.DataFrame(rows)
            index_title = "Lab Supplies"
            data = data[data['Category'] == "Lab Supplies"]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]
            
        elif selected == "Office Supplies":
            data = pd.DataFrame(rows)
            index_title = "Office Supplies"
            data = data[data['Category'] == "Office Supplies"]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]
            
        elif selected == "Tools":
            data = pd.DataFrame(rows)
            index_title = "Tools"
            data = data[data['Category'] == "Tools"]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']] 

        st.title(index_title)
        if data:
            gb = GridOptionsBuilder.from_dataframe(data)
            gb.configure_pagination(paginationAutoPageSize=True)
            gb.configure_side_bar()
            gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children")
            gridOptions = gb.build()

            grid_response = AgGrid(
                data,
                gridOptions=gridOptions,
                data_return_mode='AS_INPUT', 
                update_mode='MODEL_CHANGED', 
                fit_columns_on_grid_load=False,
                theme='blue',
                enable_enterprise_modules=True,
                height=500,
                reload_data=True
                )
        
        sel_rows = grid_response['selected_rows']
        if sel_rows:
            df = pd.DataFrame(sel_rows)
            st.dataframe(df)
            csv = convert_df(df)
            st.download_button(
               "Download Selected file as CSV",
               csv,
               "file.csv",
               "text/csv",
               key='download-csv'
               )
            
sheet_url = st.secrets["private_gsheets_url"]
SomInventory.inventory_list(f'SELECT * FROM "{sheet_url}"')

st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .reportview-container .main .block-container{{
    padding-top: {padding}rem;
    padding-right: {padding}rem;
    padding-left: {padding}rem;
    padding-bottom: {padding}rem;
    }}
</style> """, unsafe_allow_html=True
)
