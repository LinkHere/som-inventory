import streamlit as st
import pandas as pd

from inventorydata import InventoryData

st.set_page_config(
        page_title="SOM-Inventory",
)
st.title("Inventory") 
rows = InventoryData.load_data()
df = pd.DataFrame(rows)
data = df[['Item','Quantity','Commonly_Used_By','Location']]
data2 = data[data['Location'].isin("Stock Room")]
#data.index+=1
st.write("Stock Room")
st.table(data2)

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

