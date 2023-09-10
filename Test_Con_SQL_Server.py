import streamlit as st
import pyodbc
# Initialize connection.

conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1,1433"
        + ";DATABASE=Test"
        + ";UID=Demo"
        + ";PWD=admin"
    )


# Perform query.

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
