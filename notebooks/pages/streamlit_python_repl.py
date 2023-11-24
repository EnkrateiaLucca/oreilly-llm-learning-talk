import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


'''
Try changing the code in the text area below to
`plt.plot(data[:, 1])`
'''

data = np.random.randn(100, 2)
default_code = 'plt.plot(data)'
code = st.text_area('Enter some code', default_code)

exec(code, locals())
st.pyplot()