import streamlit as st

from connection import DataBConnection
from gsheetsdb import connect

class InventoryData:
    
    global conn, query
    
    credentials = DataBConnection.load_credentials()
    sheet_url = st.secrets["private_gsheets_url"]
    conn = connect(credentials=credentials)
    query = f'SELECT * FROM "{sheet_url}"'
    
    def load_data():
        rows = conn.execute(query, headers=1)
        rows = rows.fetchall()
        return rows