pip install streamlit kiteconnect
# kite_app.py
from kiteconnect import KiteConnect
import streamlit as st
import webbrowser

api_key = "e82vof9ld8ng6p58_API_KEY"
api_secret = "qeawu5ihfnvh5sj4hmlymoat30z4ij33_API_SECRET"
redirect_url = "http://127.0.0.1:8000"

kite = KiteConnect(api_key=api_key)

st.title("Zerodha Kite API Connect")
if st.button("Login to Zerodha"):
    login_url = kite.login_url()
    webbrowser.open(login_url)
    st.write("https://developers.kite.trade/apps/e82vof9ld8ng6p58")

