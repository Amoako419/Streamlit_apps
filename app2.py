import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.title("Time series analysis ")



df = pd.read_csv('data.csv')
st.dataframe(df)

fig = make_subplots(rows=3,cols=1)

fig.add_trace(go.Scatter(
    x = df['Exam_Score']
    
))
st.write('Examination score')
st.line_chart(df['Exam_Score'][:100])
st.write('Hours of study')
st.line_chart(df['Hours_Studied'][:100])

st.write('Gender')
male =  df['Gender'].value_counts()[0]
female =  df['Gender'].value_counts()[1]
# plt.pie(male,female)
# plt.show()

st.caption(f"There are {male} boys and {female} girls")