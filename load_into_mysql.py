import mysql.connector

# Set up the connection
cnx = mysql.connector.connect(user='root', password='Hello@2024',host='localhost',database='datalake')
cursor = cnx.cursor()

def insert_data_mysql(name):
    # Insert a record into the table
    insert_stmt = "INSERT INTO user (id, name, permission) VALUES (%s, %s, %s)"
    data = (1, name, 'B')
    cursor.execute(insert_stmt, data)

    # Commit the changes
    cnx.commit()

    # Close the connection
    cursor.close()
    cnx.close()