import streamlit as st

st.title('Check whether number is odd or even')
a = st.number_input('Enter a number')
result = ''
if a % 2 == 0:
  result = 'Even'
else
  result = 'Odd'

st.write(result)

