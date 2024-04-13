import mysql.connector

def main():
    try:
        cafe = mysql.connector.connect(
            host="127.0.0.1",  # Hostname (equivalent to localhost)
            port=3306,  # Port number
            user="catcafe",  # MySQL user
            password="CoffeeCatSandwich",  # Password (you can provide your password here if any) # Database/schema (no specific database selected)
            database="CatCafeInfo",
        )
        print("Connected")

        cursor = cafe.cursor()

        cat_insert = "INSERT INTO Cat (cat_name, breed, sex, age, weight, adoption_phone_number) VALUES (%s, %s, %s, %s, %s, %s)"
        cat_data = ('cattttttt', 'Shorthair', 'F', 4, 5, '1111111111')

        cursor.execute(cat_insert, cat_data)

        cafe.commit()

        print("Added cat")

    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

if __name__ == "__main__":
    main()
