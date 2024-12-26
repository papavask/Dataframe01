import pandas as pd
import streamlit as st
import requests
from io import StringIO


def load_data(url):
    df = pd.read_fwf(url, encoding='utf8', width=512)  # 👈 Download the data
    return df

st.title("Dataframe browser")

df_url = "https://raw.githubusercontent.com/papavask/Dataframe01/main/Text01.txt"
# df = load_data(df_url)
resp = requests.get(df_url)
if response.status_code == 200:
    df = pd.read_csv(StringIO(response.text))
else:
    st.error("Failed to load data from GitHub.")
    df = None

st.dataframe(df)

st.button("Rerun")
