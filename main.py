import mysql.connector
import pandas as pd
import streamlit as st

@st.cache(allow_output_mutation=True)
def establish_connection():
    mysql_config = st.secrets["connections"]["mysql"]
    return mysql.connector.connect(
        host=mysql_config["host"],
        port=mysql_config["port"],
        database=mysql_config["database"],
        user=mysql_config["username"],
        password=mysql_config["password"]
    )

def main():
    conn = establish_connection()

    # Perform query.
    query = 'SELECT * FROM crud_new1;'
    df = pd.read_sql(query, conn)

    # Print results.
    for index, row in df.iterrows():
        st.write(f"{row['id']} has a {row['email']}:")
        
if __name__ == "__main__":
    main()
