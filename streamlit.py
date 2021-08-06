import streamlit as st
import pandas as pd
import numpy as np

text = """
# Sample Web App


"""
text

uploaded_file = st.file_uploader("Choose a file to upload")

#dataframe = pd.read_csv(uploaded_file)
#dataframe

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
