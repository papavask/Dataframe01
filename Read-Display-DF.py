import streamlit as st

def load_data(url):
    df = pd.read_csv(url)  # 👈 Download the data
    return df

st.title("Dataframe browser")


df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")
