import streamlit as st
import SQLAlchemy
conn = st.experimental_connection("sql_connection", type="streamlit.connections.SQLConnection")
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
