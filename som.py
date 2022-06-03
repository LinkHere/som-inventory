import streamlit as st
import pandas as pd

from inventorydata import InventoryData

rows = InventoryData.load_data()
df = pd.DataFrame(rows)
data = df[['Item','Quantity','Commonly_Used_By','Location']]
data.index+=1
st.table(data)
# Print results.
#for row in rows:
#    st.write(f"{row.Item} has a :{row.Quantity}:")
