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

    mycursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1)")

    mycursor2 = db.cursor()

    mycursor2.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    myresults2 = mycursor2.fetchall()

    for x in myresults2:
        print(x)

    mycursor3 = db.cursor()

    mycursor3.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    mycursor4 = db.cursor()

    mycursor4.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    myresults4 = mycursor4.fetchall()

    for x in myresults4:
        print(x)

    mycursor5 = db.cursor()

    mycursor5.execute("DELETE FROM player WHERE first_name = 'Gollum'")

    mycursor6 = db.cursor()

    mycursor6.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    myresults6 = mycursor6.fetchall()

    for x in myresults6:
        print(x)

finally:
    db.close()