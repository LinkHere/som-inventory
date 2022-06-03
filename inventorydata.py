import streamlit as st

from connection import DataBConnection

credentials = DataBConnection.load_credentials()
conn = connect(credentials=credentials)

class InventoryData:

    #@st.cache(ttl=600)
    @st.experimental_singleton
    def load_data():
        sheet_url = st.secrets["private_gsheets_url"]
        query = f'SELECT * FROM "{sheet_url}"'
        rows = conn.execute(query, headers=1)
        rows = rows.fetchall()
        return rows


#rows = run_query(f'SELECT * FROM "{sheet_url}"')