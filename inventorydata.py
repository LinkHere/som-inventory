import streamlit as st

from connection import DataBConnection
from gsheetsdb import connect

credentials = DataBConnection.load_credentials()
conn = connect(credentials=credentials)

class InventoryData:

    @st.cache()
    def load_data():
        sheet_url = st.secrets["private_gsheets_url"]
        query = f'SELECT * FROM "{sheet_url}"'
        rows = conn.execute(query, headers=1)
        rows = rows.fetchall()
        return rows
