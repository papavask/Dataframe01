import streamlit as st
import pandas as pd

def load_data(url):
    df = pd.read_fwf(url, encoding='utf8', header=None, names=["aline"])  # 👈 Download the data
    return df

st.title("Dataframe browser")


df = load_data("https://raw.githubusercontent.com/papavask/Dataframe01/main/Text01.txt")
st.dataframe(df)

st.button("Rerun")
