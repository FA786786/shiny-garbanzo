import streamlit as st
from kiteconnect import KiteConnect
import webbrowser
import os


API_KEY = "e82vof9ld8ng6p58your"
API_SECRET = "qeawu5ihfnvh5sj4hmlymoat30z4ij33"
REDIRECT_URL = "http://127.0.0.1:8000"

kite = KiteConnect(api_key=API_KEY)

st.set_page_config(page_title="Zerodha API Demo", layout="centered")
st.title("📈 Zerodha Kite Connect - Streamlit Demo")



    login_url = https://developers.kite.trade/apps()
    webbrowser.open(login_url)
    st.info(https://developers.kite.trade/apps.")


request_token = st.text_input("https://developers.kite.trade/apps:")
import streamlit as st

# Safe loading of Google Sheets secret
json_key = st.secrets.get("google_sheets", None)

import streamlit as st
import json
from auth import get_google_sheet

# 🛡️ Safe way to load the secret:
json_key = st.secrets.get("google_sheets", None)

if json_key is None:
    st.warning("⚠️ Google Sheets key not found. Skipping Google Sheet integration.")
    sheet = None  # fallback in case needed
else:
    sheet_url = "https://docs.google.com/spreadsheets/d/your_sheet_id_here"
    sheet = get_google_sheet(sheet_url, json_key)


if st.button("⚙️ Generate Access Token"):
    try:
        session = kite.generate_session(request_token, api_secret=API_SECRET)
        access_token = session["access_token"]
        kite.set_access_token(access_token)

        # Save to file
        with open("access_token.txt", "w") as f:
            f.write(access_token)

        st.success("✅ Access token generated and saved!")
        st.code(access_token)

        # Show profile
        profile = kite.profile()
        st.subheader("👤 Profile Info")
        st.json(profile)

    except Exception as e:
        st.error(f"❌ Error: {e}")

# 📂 Use Saved Token
if st.button("📂 Use Saved Token"):
    try:
        if os.path.exists("access_token.txt"):
            with open("access_token.txt", "r") as f:
                token = f.read()
            kite.set_access_token(token)

            profile = kite.profile()
            st.subheader("👤 Profile Info (from saved token)")
            st.json(profile)
        else:
            st.warning("Token file not found. Please login first.")
    except Exception as e:
        st.error(f"❌ Error: {e}")
