import mysql.connector
from mysql.connector import errorcode
#Secures the connection to the database

#Please use this to get DB cursor in your code:
#   import dbConnection
#   con = dbConnection.get_connection()
#   c = con.cursor()
#   ~CODE~
#   con.close()

def get_connection():
    try:
        con = mysql.connector.connect(host="127.0.0.1",
                                   user="ali2suhail",
                                   password="Ali2suhaiL10+$++",
                                   database="ali2suhail_prj")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("[DB] Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("[DB] Database does not exist")
        else:
            print(err)
    else:
        print("[DB] Connection Established! IP: ", con._host)
        return con