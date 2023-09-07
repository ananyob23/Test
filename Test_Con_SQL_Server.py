


import streamlit as st
from streamlit.connections import SQLConnection

conn = st.experimental_connection('Test',type='sql')
mytable = conn.query('select * from mytable')
st.dataframe(mytable)


