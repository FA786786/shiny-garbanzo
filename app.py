import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Define the Google Sheets scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials from Streamlit secrets
json_key = st.secrets["google_sheets"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(json_key, scope)

# Authorize the gspread client
client = gspread.authorize(creds)

# Open the sheet using the spreadsheet ID (not name)
sheet = client.open_by_key("1-fB69hGqWPhCJ80gOhzDeVCvbxDH5y3cFDlqWZy757k").sheet1

# Streamlit app UI
st.title("🔐 Zerodha API Credential Saver")

st.markdown("Enter your **Zerodha API Key**, **API Secret**, and **Access Token** to store it securely in Google Sheets.")

# Input fields
api_key = st.text_input("API Key")
api_secret = st.text_input("API Secret")
access_token = st.text_input("Access Token")

# On button click, append data to the sheet
if st.button("💾 Save to Google Sheet"):
    if api_key and api_secret and access_token:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([api_key, api_secret, access_token, timestamp])
        st.success("✅ Credentials saved successfully!")
    else:
        st.warning("⚠️ Please fill in all fields before submitting.")
