import streamlit as st
import pandas as pd
import numpy as np

text = """
# My second app
Hello *world!*
"""

text

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [50, 50],
    columns=['lat', 'lon'])

st.map(map_data)
