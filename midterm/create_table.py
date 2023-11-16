# import sqlite3

# # Connect to SQLite database (creates a new database file if it doesn't exist)
# conn = sqlite3.connect('data.db')

# # Create a cursor object to execute SQL queries
# cursor = conn.cursor()

# # Define the SQL query to create a table
# create_table_query = '''
# CREATE TABLE IF NOT EXISTS Student (
#     First_name TEXT,
#     Last_name TEXT,
#     Gender TEXT,
#     Email TEXT,
#     Age TEXT
# );
# '''

# # Execute the query to create the table
# cursor.execute(create_table_query)

# # Commit the changes and close the connection
# conn.commit()
# conn.close()

# print("Database and table created successfully!")


import sqlite3

conn = sqlite3.connect('data.db')
print("Connected to database successfully")

# The corrected SQL query without the SQLite header
conn.execute('CREATE TABLE Student (First_name TEXT, Last_name TEXT, Gender TEXT, Email TEXT, Age TEXT)')
print("Created table successfully!")

conn.close()
