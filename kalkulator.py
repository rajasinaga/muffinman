import streamlit as st
st.header('A Very Unconvenient Calculator')
st.subheader('Plot')

#Definitions
c1, c2, c3, c4 = st.columns(4)

with c1:
  a = st.number_input('Real Integers', value=0)

with c2:
  Operators = selectbox('Operators',('+', '-', 'x', ':'), key='k1')

with c3:
  b = st.number_input('Real Integers', value=0)

with c4:
  if c2 == '+':
    return a + b
  if c2 == '-':
    return a - b
  if c2 == 'x':
    return a*b
  if c2 == ':':
    if b == 0:
      return "You cannot divide by zero, Dummy :sparkles:!"
    else:
      return a/b

st.caption('Really, Just use the calculator on your phone!')
    
