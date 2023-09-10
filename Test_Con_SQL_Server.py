import streamlit as st



cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+st.secrets["server"]+';DATABASE='+st.secrets["database"]+';UID='+st.secrets["username"]+';PWD='+ st.secrets["password"])
cursor = cnxn.cursor()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
        cursor.execute(query)
        return cursor.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")


