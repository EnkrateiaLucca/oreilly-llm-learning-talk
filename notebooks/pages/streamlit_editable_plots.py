import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Quadratic Equation Graph with Coefficients and x Value")

a = st.sidebar.slider("Coefficient a", -10.0, 10.0, 1.0)
b = st.sidebar.slider("Coefficient b", -10.0, 10.0, 0.0)
c = st.sidebar.slider("Coefficient c", -100.0, 100.0, 0.0)
x = np.linspace(-10, 10, 20)
y = a * x**2 + b * x + c
# Your existing code
# Create a DataFrame
df = pd.DataFrame({'f(x)': y})
# Print the DataFrame
st.line_chart(df, use_container_width=True)