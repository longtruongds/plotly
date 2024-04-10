#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from io import StringIO, BytesIO
import base64
import streamlit as st
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)

mybuff = StringIO()
fig.write_html(mybuff, include_plotlyjs='cdn')
mybuff = BytesIO(mybuff.read().encode('utf8'))
href = f'<a href="data:file/txt;base64, {base64.b64encode(mybuff.read())}" download="plot.html">Downlo\
ad plot</a>'
st.markdown(href, unsafe_allow_html=True)

