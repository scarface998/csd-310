import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "Franklin12",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try: 
    db = mysql.connector.connect(**config)

    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)


try:
    mycursor = db.cursor()

    mycursor2 = db.cursor()

    mycursor2.execute("SELECT team_id, team_name, mascot FROM team")

    myresults2 = mycursor2.fetchall()

    for x in myresults2:
        print(x)

    mycursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    myresults = mycursor.fetchall()

    for x in myresults:
        print(x)

finally:
    db.close()