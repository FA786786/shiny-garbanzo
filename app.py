import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials from Streamlit secrets
json_key = st.secrets["google_sheets"]

# Authorize client
creds = ServiceAccountCredentials.from_json_keyfile_dict(json_key, scope)
client = gspread.authorize(creds)

# Open the Google Sheet by name
sheet = client.open_by_key("1-fB69hGqWPhCJ80gOhzDeVCvbxDH5y3cFDlqWZy757k").sheet1

# Display header
st.title("🔐 Zerodha API Credential Manager")

# Input fields
api_key = st.text_input("API Key")
api_secret = st.text_input("API Secret")
access_token = st.text_input("Access Token")

# Submit button
if st.button("Save to Google Sheet"):
    if api_key and api_secret and access_token:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([api_key, api_secret, access_token, timestamp])
        st.success("✅ Credentials saved to Google Sheet!")
    else:
        st.error("❌ Please fill all fields before submitting.")

# Optional: show latest 5 rows for confirmation
st.subheader("📄 Last 5 Entries")
rows = sheet.get_all_values()
st.table(rows[-5:] if len(rows) >= 5 else rows)


