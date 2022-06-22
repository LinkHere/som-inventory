import streamlit as st

from connection import DataBConnection
from gsheetsdb import connect

class InventoryData:
    
    global conn, query
    credentials = DataBConnection.load_credentials()
    conn = connect(credentials=credentials)
    
    @st.experimental_singleton
    def load_data(query):    
        rows = conn.execute(query, headers=1)
        rows = rows.fetchall()
        return rows
