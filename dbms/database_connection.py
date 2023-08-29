import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="your_database"
)

# Check if the connection is successful
if conn.is_connected():
    print("Connected to MySQL database!")

# Close the connection
conn.close()
