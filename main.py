import streamlit as st
import mysql.connector

# Function to establish MySQL connection
# Establish MySQL connection
def establish_connection():
    # Get MySQL connection parameters from secrets
    mysql_config = st.secrets["connections"]["mysql"]
    # Attempt to establish the connection
    try:
        conn = mysql.connector.connect(**mysql_config)
        st.write("Connection established successfully!")
        return conn
    except Exception as e:
        st.error(f"Failed to establish connection: {str(e)}")


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
