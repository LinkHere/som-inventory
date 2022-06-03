import streamlit as st
import pandas as pd

from inventorydata import InventoryData
from streamlit_option_menu import option_menu

class SomInventory:

    def inventory_list():
        index_title = None
        rows = InventoryData.load_data()
        df = pd.DataFrame(rows)

        with st.sidebar:
            selected = option_menu("Main Menu", ["All","Skills Lab Inventory", "Dean's Office Inventory", 'Stock Room Inventory', 'Models Inventory', 'Microscope Inventory'], 
                icons=['journal-medical', 'journal-medical', 'journal-medical', 'journal-medical', 'journal-medical', 'journal-medical'], menu_icon="calendar4-week", default_index=0)
        
        if selected == "All" and index_title == None:
            index_title = "All"
            data = df[['Item','Quantity','Commonly_Used_By','Location']]
        
        if selected == "Skills Lab Inventory" and index_title == None:
            index_title = "Skills Lab Inventory"
            data = df[df['location'] == "Skills Lab"]


        #data2 = data[data['Location'] == "Stock Room"]
        #data.index+=1
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