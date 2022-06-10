import streamlit as st
import pandas as pd

from inventorydata import InventoryData
from streamlit_option_menu import option_menu

class SomInventory:

    def inventory_list():
        index_title = None
        rows = InventoryData.load_data()
        data = pd.DataFrame(rows)

        with st.sidebar:
            selected = option_menu("Main Menu", ["All", "Apparatus", "Equipments", "Instruments", "Models", "Supplies", "Tools"], 
                icons=["journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical"], menu_icon="calendar4-week", default_index=0)
        
        if selected == "All" and index_title == None:
            index_title = "All"
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]
            st.title(index_title)
            st.table(data)
        
        if selected == "Apparatus" and index_title == None:
            index_title = "Apparatus"
            data = data[data['Category'] == "Apparatus"]
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]
            st.title(index_title)
            st.table(data)

        if selected == "Dean's Office Inventory" and index_title == None:
            index_title = "Dean's Office Inventory"
            data = data[data['Location'] == "Dean's Office"]
            data = data.sort_values(by=['Item'])
            data.index = data.index.factorize()[0] + 1
            st.title(index_title)
            st.table(data)

        if selected == "Stock Room Inventory" and index_title == None:
            index_title = "Stock Room Inventory"
            data = data[data['Location'] == "Stock Room"]
            data = data.sort_values(by=['Item'])
            data.index = data.index.factorize()[0] + 1
            st.title(index_title)
            st.table(data)

        if selected == "Models Inventory" and index_title == None:
            index_title = "Models Inventory"
            datamsg = "Not yet sorted!"
            #data = data.sort_values(by=['Item'])
            #data.index = data.index.factorize()[0] + 1
            st.title(index_title)
            st.write(datamsg)

        if selected == "Microscope Inventory" and index_title == None:
            index_title = "Microscope Inventory"
            datamsg = "Not yet sorted!"
            #data = data.sort_values(by=['Item'])
            #data.index = data.index.factorize()[0] + 1 
            st.title(index_title)
            st.write(datamsg)      

        # st.title(index_title)
        # st.table(data)

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
