import  mysql.connector
def view_table(table_name):
    try:
        cafe = mysql.connector.connect(
            host="127.0.0.1",  # Hostname (equivalent to localhost)
            port=3306,  # Port number
            user="catcafe",  # MySQL user
            password="CoffeeCatSandwich",
            # Password (you can provide your password here if any) # Database/schema (no specific database selected)
            database="CatCafeInfo",
        )
        print("Connected")

        cursor = cafe.cursor()

        cursor.execute(f"SELECT * FROM {table_name}")

        # Fetch all rows from the result
        rows = cursor.fetchall()
        cursor.close()
        cafe.close()

        return rows
    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

def delete_row(primary_key):
    try:
        cafe = mysql.connector.connect(
            host="127.0.0.1",  # Hostname (equivalent to localhost)
            port=3306,  # Port number
            user="catcafe",  # MySQL user
            password="CoffeeCatSandwich",
            # Password (you can provide your password here if any) # Database/schema (no specific database selected)
            database="CatCafeInfo",
        )
        print("Connected")

        cursor = cafe.cursor()

        cursor.execute(f"DELETE FROM cat WHERE {primary_key}")
        cafe.commit()
        cursor.close()
        cafe.close()

    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

def select_cat(customer_email, cat_name):
    try:
        cafe = mysql.connector.connect(
            host="127.0.0.1",  # Hostname (equivalent to localhost)
            port=3306,  # Port number
            user="catcafe",  # MySQL user
            password="CoffeeCatSandwich",
            # Password (you can provide your password here if any) # Database/schema (no specific database selected)
            database="CatCafeInfo",
        )
        print("Connected")
        print(customer_email)
        print(cat_name)
        cursor = cafe.cursor()

        query = "UPDATE Cat SET customer_name = %s WHERE cat_name = %s"
        cursor.execute(query, (customer_email,cat_name ))
        cafe.commit()
        print("update")

        # Fetch all rows from the result
        cursor.close()
        cafe.close()

    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

def adopt_cat(cat_name):
    try:
        cafe = mysql.connector.connect(
            host="127.0.0.1",  # Hostname (equivalent to localhost)
            port=3306,  # Port number
            user="catcafe",  # MySQL user
            password="CoffeeCatSandwich",
            # Password (you can provide your password here if any) # Database/schema (no specific database selected)
            database="CatCafeInfo",
        )
        print("Connected")

        cursor = cafe.cursor()

        query = "DELETE FROM Cat WHERE cat_name = %s"
        cursor.execute(query, (cat_name,))

        cafe.commit()
        # Fetch all rows from the result
        cursor.close()
        cafe.close()

    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

def check_customer(customer_email):
    try:
        cafe = mysql.connector.connect(
            host="127.0.0.1",  # Hostname (equivalent to localhost)
            port=3306,  # Port number
            user="catcafe",  # MySQL user
            password="CoffeeCatSandwich",
            # Password (you can provide your password here if any) # Database/schema (no specific database selected)
            database="CatCafeInfo",
        )
        print("Connected")

        cursor = cafe.cursor()

        query = "SELECT * FROM Customer WHERE email = %s"
        cursor.execute(query, (customer_email,))

        #cursor.execute(f"SELECT * FROM Customer WHERE email = {customer_email}")
        row = cursor.fetchone()
        # Fetch all rows from the result
        cursor.close()
        cafe.close()
        return row
    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

def create_customer(customer_email, first_name, last_name):
    try:
        cafe = mysql.connector.connect(
            host="127.0.0.1",  # Hostname (equivalent to localhost)
            port=3306,  # Port number
            user="catcafe",  # MySQL user
            password="CoffeeCatSandwich",
            # Password (you can provide your password here if any) # Database/schema (no specific database selected)
            database="CatCafeInfo",
        )
        print("Connected")

        cursor = cafe.cursor()


        customer_insert = "INSERT INTO Customer (email, first_name, last_name, cat_name) VALUES (%s, %s, %s, %s)"
        customer_values = (customer_email, first_name, last_name, "none")
        cursor.execute(customer_insert, customer_values)

        print("created customer")
        cafe.commit()

        # Fetch all rows from the result
        cursor.close()

    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

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
