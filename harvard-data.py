import streamlit as st
import pandas as pd

data = pd.read_csv("appendix.csv")

st.title("Course enrollment last year")
st.dataframe(data)


st.write("The percentage of Male student that enrolled")
st.line_chart(data['% Male'])
st.write("The percentage of Female student that enrolled")
st.line_chart(data['% Female'],color="#ffaa00")