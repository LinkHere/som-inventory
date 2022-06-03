import streamlit as st
import pandas as pd

from inventorydata import InventoryData
from streamlit_option_menu import option_menu

st.set_page_config(
        page_title="SOM-Inventory",
)
with st.sidebar:
    selected = option_menu("Main Menu", ["All","Skills Lab Inventory", "Dean's Office Inventory", 'Stock Room Inventory', 'Models Inventory', 'Microscope Inventory'], 
        icons=['journal-medical', 'journal-medical', 'journal-medical', 'journal-medical', 'journal-medical'], menu_icon="calendar4-week", default_index=0)
st.title("Inventory") 
rows = InventoryData.load_data()
df = pd.DataFrame(rows)
data = df[['Item','Quantity','Commonly_Used_By','Location']]
#data2 = data[data['Location'] == "Stock Room"]
#data.index+=1
st.write("Stock Room")
st.table(data)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

.reportview-container .main .block-container{{
    padding-top: {padding}rem;
    padding-right: {padding}rem;
    padding-left: {padding}rem;
    padding-bottom: {padding}rem;
    }}
</style> """, unsafe_allow_html=True)

