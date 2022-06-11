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
            selected = option_menu("Inventory", ["All", "Apparatus", "Equipments", "Instruments", "Models", "Lab Supplies", "Office Supplies", "Tools"], 
                icons=["journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical", "journal-medical"], menu_icon="calendar4-week", default_index=0)
        
        if selected == "All" and index_title == None:
            index_title = "All"
            data['Item'] = data['Item'].str.lower()
            data = data.sort_values(by=['Item'])
            data['Item'] = data['Item'].str.title()
            data.index = data.index.factorize()[0] + 1
            data = data[['Item', 'Quantity', 'Commonly_Used_By', 'Location']]
        
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

        st.title(index_title)
        st.table(data)

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
