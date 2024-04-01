import streamlit as st

# Function to establish MySQL connection
def establish_connection():
    # Print out all secrets to verify they are loaded correctly
    st.write("Secrets Keys:", st.secrets.keys())

    # Get MySQL connection parameters from secrets
    mysql_config = st.secrets["connections"]["mysql"]

    # Establish MySQL connection
    return mysql.connector.connect(**mysql_config)

# Main Streamlit app function
def main():
    # Title of the Streamlit app
    st.title("User Information")

    # Establish MySQL connection
    conn = establish_connection()

    # Perform query.
    query = 'SELECT * FROM crud_new1;'
    df = pd.read_sql(query, conn)

    # Print results.
    for index, row in df.iterrows():
        st.write(f"{row['id']} has a {row['email']}:")

if __name__ == "__main__":
    main()
