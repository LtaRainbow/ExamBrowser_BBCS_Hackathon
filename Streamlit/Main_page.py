import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(page_title="Hello!", page_icon="🔥")
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

map_df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [1.2963, 103.8502],
    columns=['lat', 'lon'])

st.map(map_df)

