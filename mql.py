import mysql.connector
def show_tables():
    cur.execute("show tables")

def new_table():
    cur.execute("")
# Connect to server
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sarthak",
    database="sarthak")

# Get a cursor
cur = cnx.cursor()

# Execute a query
show_tables()

# Fetch one result
for table in cur:
    print(table)
