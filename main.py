import streamlit as st
import pandas as pd

st.title("hello")
dataset = pd.read_csv("sample.csv")
st.dataframe(dataset)
