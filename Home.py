import streamlit as st


st.set_page_config(page_title="Trading Panel", page_icon="📈", layout="wide")

st.title("Welcome to the Trading Panel App! 📊")

st.write("""
This app consists of multiple features:
- **Trend Panel**: Check the SMA(200) trend of an asset.
- **Position Sizer**: Calculate the appropriate position size.

Use the menu on the left to navigate! 👈
""")