# import sqlite3

# def list_tables():
#     try:
#         # Connect to the SQLite database
#         conn = sqlite3.connect('db.sqlite3')  # Replace 'db.sqlite3' with your actual SQLite database file

#         # Create a cursor object
#         cursor = conn.cursor()

#         # Get a list of all tables in the database
#         cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#         tables = cursor.fetchall()

#         # Print the list of tables
#         print("Tables in the database:")
#         for table in tables:
#             print(table[0])

#         # Close the cursor and connection
#         cursor.close()
#         conn.close()
#     except sqlite3.Error as e:
#         print("An error occurred:", str(e))

# def remove_data(table_name, condition):
#     try:
#         # Connect to the SQLite database
#         conn = sqlite3.connect('db.sqlite3')  # Replace 'db.sqlite3' with your actual SQLite database file

#         # Create a cursor object
#         cursor = conn.cursor()

#         # Execute the DELETE SQL query
#         cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")

#         # Commit the changes
#         conn.commit()

#         print("Data removed successfully.")
#     except sqlite3.Error as e:
#         print("An error occurred:", str(e))
#     finally:
#         # Close the cursor and connection
#         cursor.close()
#         conn.close()

# # Call the function to list tables
# list_tables()

# # Call the function to remove data from a specified table
# table_name = input("Enter the name of the table from which you want to remove data: ")
# condition = input("Enter the condition to specify which data to remove (e.g., id=1): ")
# remove_data(table_name, condition)


import requests
from bs4 import BeautifulSoup

# URL of the page that requires CSRF protection
url = 'http://localhost:8000/login'

# Make a GET request to the URL
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find CSRF token input field
csrf_token_input = soup.find('input', {'name': 'csrfmiddlewaretoken'})

# Extract CSRF token value
csrf_token = csrf_token_input['value']

# Print CSRF token
print("CSRF Token:", csrf_token)
