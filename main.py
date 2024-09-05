import streamlit as st
import pandas as pd
import numpy as np
 
st.write("""
# My first app
Hello *world!*
""")
 
# df = pd.read_csv("Onli")

rand = np.random.randint(11)
df = pd.DataFrame({
    "a":[1,2,3,4,5,6,7,8,9,10,11],
    "b":[12,13,14,15,16,17,18,19,20,21,22],
    "random":[23,45,11,34,66,76,12,45,22,10,55],
})
st.line_chart(df)