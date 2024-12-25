import streamlit as st
import pandas as pd

def load_data(url):
    df = pd.read_table(url, header=None)  # 👈 Download the data
    return df

st.title("Dataframe browser")


df = load_data("https://github.com/papavask/Dataframe01/blob/main/Text01.txt")
st.dataframe(df)

st.button("Rerun")
