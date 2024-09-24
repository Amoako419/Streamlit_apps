import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("appendix.csv")

st.title("Course enrollment last year")
st.dataframe(data)


st.write("The percentage of Male student that enrolled")
st.line_chart(data['% Male'])
st.write("The percentage of Female student that enrolled")
st.line_chart(data['% Female'],color="#ffaa00")

# plt.plot(data["% Female"],data["% Male"])
# plt.show()
st.write("## Total course hours ")
st.bar_chart(data["Total Course Hours (Thousands)"])

st.write(data['Course Title'].value_counts())
st.bar_chart(data['Course Title'].value_counts())
st.write(data['Instructors'].value_counts())
st.bar_chart(data['Instructors'].value_counts())

st.balloons()


