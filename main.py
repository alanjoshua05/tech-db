import streamlit as st

# Initialize connection.
@st.cache(allow_output_mutation=True)
def establish_connection():
    return st.secrets["mysql"]

conn = establish_connection()

# Perform query.
query = 'SELECT * FROM crud_new1;'
df = conn.query(query, ttl=600)

# Print results.
for index, row in df.iterrows():
    st.write(f"{row['id']} has a {row['email']}:")
