# this is place holder code not perfect yet

import mysql.connector

def main():
    try:
        cafe = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="yourdatabase"
        )
        print("Connected")
    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

if __name__ == "__main__":
    main()
