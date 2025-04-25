import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Read credentials from Streamlit secrets
json_key = st.secrets["google_sheets"]
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Authorize the credentials
creds = ServiceAccountCredentials.from_json_keyfile_dict(json_key, scope)
client = gspread.authorize(creds)

# Open and write to sheet
sheet = client.open("Your Google Sheet Name").sheet1
sheet.append_row(["2025-04-25", "RELIANCE", "Buy", "2840.00"])
