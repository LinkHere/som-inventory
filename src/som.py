import streamlit as st

st.set_page_config(
    page_title="SOM-Inventory",
)

import pandas as pd


from io import BytesIO
from inventorydata import InventoryData
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from streamlit_option_menu import option_menu

class SomInventory:

    def inventory_list(url):
        #pd.set_option('display.max_colwidth', None)
        index_title = None
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
            check_box=True
        
        elif selected == "Models Gallery":
            data = data[data['Category'] == selected]
            data = data[['Item', 'Img_url']]
            st.write(data)
                
        elif selected:
            data = pd.DataFrame(rows)
            index_title = selected
            data = data[data['Category'] == selected]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]
            check_box=False

        st.title(index_title)
        gb = GridOptionsBuilder.from_dataframe(data)
        gb.configure_pagination(paginationAutoPageSize=True)
        gb.configure_side_bar()
        gb.configure_selection('multiple', use_checkbox=check_box, groupSelectsChildren="Group checkbox select children")
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
        if sel_rows and selected == "All":
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
