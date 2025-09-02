import streamlit as st
import requests

# Title
st.title("Live Currency Converter")

# Input amount in INR
amount = st.number_input("Enter the amount in INR:", min_value=1)

# Select target currency
target_currency = st.selectbox("Convert to:", ["USD", "EUR", "GBP", "JPY"])

# Convert button
if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_currency]   # get exchange rate
        converted = rate * amount               # convert amount
        st.success(f"{amount} INR = {converted:.2f} {target_currency}")
    else:
        st.error("Failed to fetch conversion rate")