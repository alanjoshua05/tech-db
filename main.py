import streamlit as st
import mysql.connector

# Function to establish MySQL connection
@st.cache(allow_output_mutation=True)
def establish_connection():
    mysql_config = st.secrets["mysql"]
    return mysql.connector.connect(**mysql_config)

# Main Streamlit app function
def main():
    # Title of the Streamlit app
    st.title("User Information")

    # Establish MySQL connection
    conn = establish_connection()

    # Check if the connection is successful
    if conn.is_connected():
        st.write("Connected to MySQL database!")

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # SQL query to select data from the users table
        query = "SELECT * FROM crud_new1"

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display fetched data
        for row in rows:
            st.write(f"{row[0]} has a {row[1]}:")

        # Close the cursor and connection
        cursor.close()
        conn.close()
    else:
        st.error("Failed to connect to MySQL database.")

# Call the main function to run the Streamlit app
if __name__ == "__main__":
    main()
