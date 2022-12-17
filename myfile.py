import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np

st.title('Python para Ciencia de Datos')
num = st.slider("num", 5,100, step=1)
st.write('Hola **como** estas')
chart_data = pd.DataFrame(np.random.randn(num), columns =['data'])
st.line_chart(chart_data)
