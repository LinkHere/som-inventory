import streamlit as st

from connection import DataBConnection
from gsheetsdb import connect

class InventoryData:
    
    global credentials = DataBConnection.load_credentials()
    global conn = connect(credentials=credentials)
    global sheet_url = st.secrets["private_gsheets_url"]
    global query = f'SELECT * FROM "{sheet_url}"'
    
    def load_data():
        rows = conn.execute(query, headers=1)
        rows = rows.fetchall()
        return rows
