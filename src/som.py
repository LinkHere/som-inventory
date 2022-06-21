import streamlit as st
import pandas as pd
import requests

from io import BytesIO
from inventorydata import InventoryData
from PIL import Image
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from streamlit_option_menu import option_menu

class SomInventory:

    def inventory_list():
        index_title = None
        rows = InventoryData.load_data()
        data = pd.DataFrame(rows)

        with st.sidebar:
            selected = option_menu("Inventory", ["All", "Apparatus", "Equipments", "Instruments", "Models", "Lab Supplies", "Office Supplies", "Tools"], 
                icons=["journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical"], menu_icon="calendar4-week", default_index=0)
        
        if selected == "All" and index_title == None:
            index_title = "All"
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
#             st.write(data.columns[0])
#             for row in data.itertuples(index = True, name ='Pandas'):
#                 st.write(getattr(row, "Item"), getattr(row, "Location"))
                
#             #data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]
#             picurl = "https://raw.githubusercontent.com/LinkHere/inventory-images-models/main/bls-dummy.jpg"
#             response = requests.get(picurl)
#             img = Image.open(BytesIO(response.content))
#             new_img = img.resize((600, 400))
#             #data = data['Item']
#             #image = Image.open("https://raw.githubusercontent.com/LinkHere/inventory-images-models/main/OrgChart.jpg")
#             for a in data:
#                 #st.image(new_img, caption=a['Item'], width=400)
#                 st.write(a)
                
        if selected == "Apparatus" and index_title == None:
            index_title = "Apparatus"
            data = data[data['Category'] == "Apparatus"]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]

        if selected == "Equipments" and index_title == None:
            index_title = "Equipments"
            data = data[data['Category'] == "Equipments"]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]

        if selected == "Instruments" and index_title == None:
            index_title = "Instruments"
            data = data[data['Category'] == "Instruments"]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]

        if selected == "Models" and index_title == None:
            index_title = "Models"
            data = data[data['Category'] == "Models"]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]
            st.title(index_title)
            st.table(data['Item'])
            
        if selected == "Lab Supplies" and index_title == None:
            index_title = "Lab Supplies"
            data = data[data['Category'] == "Lab Supplies"]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]
            
        if selected == "Office Supplies" and index_title == None:
            index_title = "Office Supplies"
            data = data[data['Category'] == "Office Supplies"]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]
            
        if selected == "Tools" and index_title == None:
            index_title = "Tools"
            data = data[data['Category'] == "Tools"]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']] 

#         st.title(index_title)
#         st.table(data)
        gb = GridOptionsBuilder.from_dataframe(data)
        gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
        gb.configure_side_bar() #Add a sidebar
        gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
        gridOptions = gb.build()

        grid_response = AgGrid(
            data,
            gridOptions=gridOptions,
            data_return_mode='AS_INPUT', 
            update_mode='MODEL_CHANGED', 
            fit_columns_on_grid_load=False,
            theme='blue', #Add theme color to the table
            enable_enterprise_modules=True,
            height=600,
            reload_data=True
            )

        data = grid_response['data']
        selected = grid_response['selected_rows'] 
        df = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df
        #st.write(df["Img_url"])
#         df["Img_url"] = df["Img_url"].astype(str)
#         picurl = df["Img_url"]
        df = df.astype(str)
        st.write(df.dtypes)
#         respo = requests.get(picurl)
#         img = Image.open(BytesIO(respo.content))
#         new_img = img.resize((600, 400))
#         st.image(new_img, width=400)

st.set_page_config(
    page_title="SOM-Inventory",
)

SomInventory.inventory_list()

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
