import streamlit as st
from google.oauth2 import service_account

class DataBConnection:
    @st.cache
    def load_credentials():
        credentials = service_account.Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=[
                "https://www.googleapis.com/auth/spreadsheets",
            ],
        )
        return credentials