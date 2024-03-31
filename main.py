import mysql.connector
import streamlit as st

# Function to establish MySQL connection
def establish_connection():
    mydb = mysql.connector.connect(
        host="localhost",  # Your host, usually localhost
        user="root",       # Your username
        password="alan#2005",  # Your password
        database="crud_new1"   # Your database name
    )
    return mydb

# Main Streamlit app function
def main():
    # Title of the Streamlit app
    st.title("User Information")

    # Text input for name
    name = st.text_input('Enter your Name')
    
    # Text input for email
    email = st.text_input('Enter your Email')
    
    # Submit button
    sub = st.button("Submit")

    # When submit button is clicked
    if sub:
        # Establish MySQL connection
        mydb = establish_connection()

        # Check if the connection is successful
        if mydb.is_connected():
            st.write("Connected to MySQL database!")

            # Create a cursor object to execute SQL queries
            mycurs = mydb.cursor()

            # SQL query to insert data into the users table
            sql = "INSERT INTO user (name, email) VALUES (%s, %s)"
            val = (name, email)

            # Execute the SQL query
            mycurs.execute(sql, val)

            # Commit changes to the database
            mydb.commit()

            # Close the cursor and connection
            mycurs.close()
            mydb.close()

            # Display success message
            st.success("Data inserted successfully!")
        else:
            st.error("Failed to connect to MySQL database.")

# Call the main function to run the Streamlit app
if __name__ == "__main__":
    main()
