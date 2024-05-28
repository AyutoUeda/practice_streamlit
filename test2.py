import streamlit as st
from datetime import time, datetime

st.header("st.slider")

st.subheader("Slider")

#
age = st.slider("how old are you", 0, 100, 5, 5)
st.write("I am", age, "yo")

st.subheader("Appointment")
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))


st.write("You're scheduled for:", appointment)

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)