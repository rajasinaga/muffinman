import streamlit as st
st.header('A Very Unconvenient Calculator')
st.subheader('why are you here?')

#Definitions
c1, c2, c3, c4 = st.columns(4)

with c1:
  a = st.number_input('Real Integers', value=0)

with c2:
  Operators = st.selectbox('Operators',('+', '-', 'x', ':'), key='k1')

with c3:
  b = st.number_input('Real Integers', value=0)

with c4:
  if Operators == '+':
    st.write (a + b)
  elif Operators == '-':
    st.write (a - b)
  elif Operators == 'x':
    st.write (a*b)
  elif Operators == ':':
    if b == 0:
      st.write ('You cannot divide by zero, Dummy :sparkles:!')
    else:
      st.write (a/b)

st.caption('Really, Just use the calculator on your phone!')
    
