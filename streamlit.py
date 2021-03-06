import streamlit as st
import pandas as pd
import numpy as np

text = """
# Very Basic Web App


"""
text

#left_column, right_column = st.columns(2)
#pressed = left_column.button('Press me?')
#if pressed:
#  right_column.write("Woohoo!")

#expander = st.expander("FAQ")
#expander.write("Here you could put in some really, really long explanations...")

uploaded_file = st.file_uploader("Choose a file to upload")

try:
  dataframe = pd.read_csv(uploaded_file)
  dataframe
except:
  try:
    dataframe = pd.read_excel(uploaded_file)
    dataframe
  except:
    print('No file')

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

if st.checkbox('Show map data'):
  st.map(map_data)
