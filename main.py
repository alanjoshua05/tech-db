import streamlit as st

# Initialize connection.
@st.cache(allow_output_mutation=True)
def establish_connection():
    try:
        # Assuming 'mysql' is the correct secret name in Streamlit Secrets
        return st.secrets["mysql"]
    except Exception as e:
        st.error(f"Failed to establish MySQL connection: {e}")
        return None

# Establish MySQL connection
conn = establish_connection()

if conn:
    try:
        # Perform query.
        query = 'SELECT * FROM crud_new1;'
        df = conn.query(query, ttl=600)

        # Print results.
        for index, row in df.iterrows():
            st.write(f"{row['id']} has an email: {row['email']}")
    except Exception as e:
        st.error(f"Error executing query: {e}")
