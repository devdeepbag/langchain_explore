import sqlite3

# Create or connect to the database
conn = sqlite3.connect('Chinook.db')
cursor = conn.cursor()

# Read the SQL file with utf-8 encoding
with open('Chinook_Sqlite.sql', 'r', encoding='utf-8') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL commands
cursor.executescript(sql_script)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Chinook database created successfully.")
