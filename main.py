import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from st_aggrid import AgGrid

st.title("hello")
dataset = pd.read_csv("sample.csv")
st.dataframe(dataset)
st.image("1.png", caption="Strawberry", use_container_width=True)




# Sample Data
categories = ["A", "B", "C", "D"]
values = [10, 25, 7, 30]

# Create Bar Chart
plt.bar(categories, values, color=['blue', 'green', 'red', 'aqua'])

# Display in Streamlit
st.pyplot(plt)


st.title("Grid Layout in Streamlit")

# Creating a 3-column layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<h1 style='font-size: 20px;'>OOPs In Python</h1>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=zDrbVHxIis8")

with col2:
    st.markdown("<h1 style='font-size: 20px;'>Python Full Course</h1>", 
    unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=ix9cRaBkVe0")

with col3:
    st.markdown("<h1 style='font-size: 20px;'>Python In 1 Viedio</h1>", 
    unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=gPvYox9JIYI")

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "San Francisco", "Los Angeles"]
}

df = pd.DataFrame(data)

st.title("Interactive Data Grid")
st.dataframe(df)  # This renders a scrollable and sortable table

# ------------

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": ["25", "30", "35"],
    "City": ["New York", "San Francisco", "Los Angeles"]
}

df = pd.DataFrame(data)

st.title("Advanced Data Grid with Ag-Grid")

AgGrid(df)  # This provides sorting, filtering, and editing features
