import streamlit as st
import numpy as np
import pandas as pd



st.title("App 1")
st.header(""" This is our header """)
st.write("## Streamlit is awesome")
st.caption(""" This is our caption """)

df = pd.DataFrame(
np.random.randn(30, 20),
columns=('col_no %d' % i for i in range(20)))
st.dataframe(df)


st.metric(label="Temperature", value="31 °C", delta="1.5 °C")

"Adding 100+ (-12222) = ", 100 - 12222 


# Magic working on Charts
import matplotlib.pyplot as plt
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
# Magic chart
"chart", chart

import streamlit as st
import pandas as pd
import numpy as np
st.title('Area')
# Defining dataframe with its values
df = pd.DataFrame(
np.random.randn(40, 4),
columns=["C1", "C2", "C3", "C4"])
# Bar Chart
st.dataframe(df)
st.bar_chart(df)
st.area_chart(df)




# locate_map = pd.DataFrame(
# np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
# columns = ['latitude', 'longitude'])
# # Map Function
# st.map(locate_map)


import streamlit as st
import graphviz as graphviz
st.title('Graphviz')
# Creating graph object
st.graphviz_chart('''
digraph {
"Training Data" -> "ML Algorithm"
"ML Algorithm" -> "Model"
"Model" -> "Result Forecasting"
"New Data" -> "Model"
}
''')


st.snow()