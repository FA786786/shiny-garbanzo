import streamlit as st
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from kiteconnect import KiteConnect

# -----------------------------
# Google Sheets Setup
# -----------------------------
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
json_key = st.secrets["google_sheets"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(json_key, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("1-fB69hGqWPhCJ80gOhzDeVCvbxDH5y3cFDlqWZy757k").sheet1

# -----------------------------
# Zerodha App Config
# -----------------------------
st.title("🔑 Zerodha Access Token Generator")

api_key = st.text_input("🔐 API Key", placeholder="Enter your Zerodha API Key")
api_secret = st.text_input("🧾 API Secret", type="password", placeholder="Enter your API Secret")
redirect_url = "https://your-app-name.streamlit.app"  # update with your Streamlit Cloud app URL

# Step 1: Generate login URL
if api_key:
    kite = KiteConnect(api_key=api_key)
    login_url = kite.login_url()
    st.markdown(f"👉 [Click here to login to Zerodha]({login_url})")
    request_token = st.text_input("📥 Paste the Request Token from redirected URL")

    # Step 2: Generate access token
    if st.button("⚙️ Generate & Save Access Token"):
        if api_secret and request_token:
            try:
                data = kite.generate_session(request_token, api_secret=api_secret)
                access_token = data["access_token"]
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Save to Google Sheet
                sheet.append_row([api_key, api_secret, access_token, timestamp])
                st.success("✅ Access token generated and saved successfully!")

            except Exception as e:
                st.error(f"❌ Failed to generate access token: {e}")
        else:
            st.warning("⚠️ Enter both API Secret and Request Token.")

# -----------------------------
# Use existing access token from Sheet
# -----------------------------
st.subheader("📄 Use Last Saved Token")
try:
    rows = sheet.get_all_values()
    if len(rows) > 1:
        latest = rows[-1]
        saved_key, saved_secret, saved_token, saved_time = latest
        st.code(f"API Key: {saved_key}\nAccess Token: {saved_token}\nTimestamp: {saved_time}")

        # Initialize kite with token
        kite = KiteConnect(api_key=saved_key)
        kite.set_access_token(saved_token)
        st.success("🔗 Access token loaded and KiteConnect client initialized.")
except Exception as e:
    st.error(f"⚠️ Error reading from Google Sheet or initializing Kite: {e}")
