import streamlit as st
import pandas as pd

st.title(" Book Sales Dashboard")

# File uploader
file = st.file_uploader("Upload your CSV File", type=["csv"])

if file is not None:
    # Read CSV
    df = pd.read_csv(file)

    # Data preview
    st.subheader("Data Preview")
    st.dataframe(df)

    # Summary statistics
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # City filter
    cities = df["City"].unique()
    selected_city = st.selectbox("Filter by City:", cities)

    # Filtered data
    filtered_data = df[df["City"] == selected_city]
    st.subheader(f"Data for {selected_city}")
    st.dataframe(filtered_data)
