pip install streamlit kiteconnect
# kite_app.py
from kiteconnect import KiteConnect
import streamlit as st
import webbrowser

api_key = "आपका_API_KEY"
api_secret = "आपका_API_SECRET"
redirect_url = "http://127.0.0.1:8000"

kite = KiteConnect(api_key=api_key)

# Step 1: Request Token के लिए लिंक दिखाएं
st.title("Zerodha Kite API Connect")
if st.button("Login to Zerodha"):
    login_url = kite.login_url()
    webbrowser.open(login_url)
    st.write("ब्राउज़र में Zerodha लॉगिन करें और URL से request_token कॉपी करें।")

# Step 2: Request Token से Access Token बनाएं
request_token = st.text_input("यहाँ Request Token पेस्ट करें:")
if st.button("Generate Access Token"):
    try:
        data = kite.generate_session(request_token, api_secret=api_secret)
        access_token = data["access_token"]
        st.success("Access Token मिला: " + access_token)
        # इस token को भविष्य में इस्तेमाल के लिए सेव कर सकते हैं
        kite.set_access_token(access_token)

        # उदाहरण: प्रोफाइल दिखाएं
        profile = kite.profile()
        st.write("आपका प्रोफाइल:")
        st.json(profile)

    except Exception as e:
        st.error(f"Error: {e}")
