import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# connection establishment
conn = psycopg2.connect(
database='docs_test',
	user='test',
	password='password',
	host='localhost',
	port= '5432'
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
conn.autocommit = True

# Creating a cursor object
cursor = conn.cursor()

name_Database = "docs";
# query to create a database
sql = ''' CREATE database products ''' +name_Database+";"

# executing above query
cursor.execute(sql)
print("Database has been created successfully !!");

# Closing the connection
conn.close()
