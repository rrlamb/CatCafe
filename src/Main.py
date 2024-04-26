import mysql.connector

import random
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

def view_join_table():
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

        cursor.execute(f"SELECT Customer.first_name, Cat.cat_name FROM Customer, Cat WHERE Customer.email = Cat.customer_name")

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
        query = "UPDATE Customer SET cat_name = %s WHERE email = %s"
        cursor.execute(query, (cat_name,customer_email,))
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

def check_employee(id):
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

        query = "SELECT * FROM Employee WHERE id = %s"
        cursor.execute(query, (id,))

        #cursor.execute(f"SELECT * FROM Employee WHERE id = {id}")
        row = cursor.fetchone()
        # Fetch all rows from the result
        cursor.close()
        cafe.close()
        return row
    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

def check_manager(id):
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

        query = "SELECT * FROM Employee WHERE id = %s && role = 'manager'"
        cursor.execute(query, (id,))

        #cursor.execute(f"SELECT * FROM Employee WHERE id = {id}")
        row = cursor.fetchone()
        # Fetch all rows from the result
        cursor.close()
        cafe.close()
        return row
    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

def add_customer_points(customer_email, total_points):
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
        query = "SELECT points FROM Customer WHERE email = %s"
        cursor.execute(query, (customer_email,))
        points = cursor.fetchone()[0]
        if points is None:
            points = 0
        new_points = total_points + points
        query = "UPDATE Customer SET points = %s WHERE email = %s"
        cursor.execute(query, (new_points, customer_email))
        # Fetch all rows from the result
        cafe.commit()
        cursor.close()
        cafe.close()
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


        customer_insert = "INSERT IGNORE INTO Customer (email, first_name, last_name, cat_name) VALUES (%s, %s, %s, %s)"
        customer_values = (customer_email, first_name, last_name, "none")
        cursor.execute(customer_insert, customer_values)

        print("created customer")
        cafe.commit()

        # Fetch all rows from the result
        cursor.close()

    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

def create_employee(id, first_name, last_name, role, email, age, phone_number, bank_account_number, available_item):
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


        employee_insert = "INSERT IGNORE INTO Employee (id, first_name, last_name, role, email, age, phone_number, bank_account_number, available_item) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        employee_values = (id, first_name, last_name, role, email, age, phone_number, bank_account_number, available_item)
        cursor.execute(employee_insert, employee_values)

        print("created employee")
        cafe.commit()

        # Fetch all rows from the result
        cursor.close()

    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

def update_employee(id, updateListColumns, updateListValues):
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
        i = 0
        statement = "UPDATE Employee SET"
        print(updateListColumns)
        print(updateListValues)
        while i < len(updateListColumns)-1:
            statement+=" "
            statement+=updateListColumns[i]
            statement+=" = "
            if isinstance(updateListValues[i], str):
                statement+="'"
                statement+= updateListValues[i]
                statement += "'"
            else :
                statement+=updateListValues[i]
            statement+=","
            i=i+1
        print(i)
        statement += " "
        statement += updateListColumns[i]
        statement += " = "
        if isinstance(updateListValues[i], str):
            statement += "'"
            statement += updateListValues[i]
            statement += "'"
        else:
            statement += updateListValues[i]
        statement += " WHERE id = "
        statement += str(id[0])
        statement += ";"


        print(statement)
        employee_update = statement
        cursor.execute(statement)

        print("updated employee")
        cafe.commit()

        # Fetch all rows from the result
        cursor.close()

    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

def delete(id):
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

        query = "DELETE FROM Employee WHERE id = %s"
        values = (id,)
        cursor.execute(query, values)

        cafe.commit()
        print("deleted employee")

        # Fetch all rows from the result
        cursor.close()
        cafe.close()

    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

def view_employee(id):
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

        statement = "SELECT * FROM EMPLOYEE WHERE id = %s"
        values = (id[0],)
        cursor.execute(statement, values)

        # Fetch all rows from the result
        rows = cursor.fetchall()
        cursor.close()
        cafe.close()

        return rows
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

        # Insert Initial Values Into Iventory
        bread_insert = "INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES (%s, %s)"
        bread_data = ('Bread', 50)
        turkey_insert = "INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES (%s, %s)"
        turkey_data = ('Turkey', 50)
        lettuce_insert = "INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES (%s, %s)"
        lettuce_data = ('Lettuce', 50)
        tomato_insert = "INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES (%s, %s)"
        tomato_data = ('Tomato', 50)
        cheese_insert = "INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES (%s, %s)"
        cheese_data = ('Cheese', 50)
        avocado_insert = "INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES (%s, %s)"
        avocado_data = ('Avocado', 50)
        chicken_insert = "INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES (%s, %s)"
        chicken_data = ('Chicken', 50)
        water_insert = "INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES (%s, %s)"
        water_data = ('Water', 50)
        coffee_insert = "INSERT IGNORE INTO Inventory (inventory_item, quantity) VALUES (%s, %s)"
        coffee_data = ('Coffee', 50)

        cursor.execute(bread_insert, bread_data)
        cursor.execute(turkey_insert, turkey_data)
        cursor.execute(lettuce_insert, lettuce_data)
        cursor.execute(tomato_insert, tomato_data)
        cursor.execute(cheese_insert, cheese_data)
        cursor.execute(avocado_insert, avocado_data)
        cursor.execute(chicken_insert, chicken_data)
        cursor.execute(water_insert, water_data)
        cursor.execute(coffee_insert, coffee_data)


        # Insert Initial Values Into Menu Table
        turkeyclub_insert = "INSERT IGNORE INTO Menu (item, add_on, price, employee_id) VALUES (%s, %s, %s, %s)"
        #turkeyclub_data = (f'Turkey Club', {add_ons} , 12.25, {employee_id})
        turkeyclub_data = ('Turkey Club', 'NULL', 12.25, 0)
        avotoast_insert = "INSERT IGNORE INTO Menu (item, add_on, price, employee_id) VALUES (%s, %s, %s, %s)"
        avotoast_data = ('Avocado Toast', 'NULL', 8.50, 0)
        chickensalad_insert = "INSERT IGNORE INTO Menu (item, add_on, price, employee_id) VALUES (%s, %s, %s, %s)"
        chickensalad_data = ('Chicken Salad', 'NULL', 10.75, 0)
        watercup_insert = "INSERT IGNORE INTO Menu (item, add_on, price, employee_id) VALUES (%s, %s, %s, %s)"
        watercup_data = ('Water Cup', 'NULL', 0, 0)
        icedcoffee_insert = "INSERT IGNORE INTO Menu (item, add_on, price, employee_id) VALUES (%s, %s, %s, %s)"
        icedcoffee_data = ('Iced Coffee', 'NULL', 4.50, 0)
        hotcoffee_insert = "INSERT IGNORE INTO Menu (item, add_on, price, employee_id) VALUES (%s, %s, %s, %s)"
        hotcoffee_data = ('Hot Coffee', 'NULL', 3.50, 0)

        cursor.execute(turkeyclub_insert, turkeyclub_data)
        cursor.execute(avotoast_insert, avotoast_data)
        cursor.execute(chickensalad_insert, chickensalad_data)
        cursor.execute(watercup_insert, watercup_data)
        cursor.execute(icedcoffee_insert, icedcoffee_data)
        cursor.execute(hotcoffee_insert, hotcoffee_data)


        # Insert Initial Values Into Cat
        cat_insert = "INSERT IGNORE INTO Cat (cat_name, breed, sex, age, weight, adoption_phone_number) VALUES (%s, %s, %s, %s, %s, %s)"
        cat_data = ('cattttttt', 'Shorthair', 'F', 4, 5, '1111111111')

        cursor.execute(cat_insert, cat_data)

        cafe.commit()

        print("Filled Inventory")
        print("Filled Menu")
        print("Added cat")

    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

def inventory_low():
    low_list = []
    try:
        cafe = mysql.connector.connect(
            host="127.0.0.1",  # Hostname (equivalent to localhost)
            port=3306,  # Port number
            user="catcafe",  # MySQL user
            password="CoffeeCatSandwich",  # Password (you can provide your password here if any) # Database/schema (no specific database selected)
            database="CatCafeInfo",
        )
        print("Connected for Procedure")
        cursor = cafe.cursor()

        item_list= "SELECT inventory_item FROM Inventory"
        cursor.execute(item_list)
        proc_result = cursor.fetchall()
        for item in proc_result:
            args = (item[0], 0)
            result = cursor.callproc('Low_Inventory', args)
            if result[1]==1:
                low_list.append(item[0])
        return low_list

    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)
        return low_list

def inventory_remove(club, toast, salad, water, iced, hot):
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

        # Update Bread Inventory
        get_bread = 'SELECT quantity FROM Inventory' ' WHERE inventory_item = %s'
        get_data = ('Bread',)
        cursor.execute(get_bread, get_data)
        bread_result = cursor.fetchone()
        if bread_result:
            bread_quantity = bread_result[0]
            # Not Enough Items In Inventory to Place Order
            if (bread_quantity < ((club * 2) + toast)):
                print("Not enough bread in inventory")
            # Enough Items In Inventory to Place Order
            else:
                new_quantity = bread_quantity - ((club * 2) + toast)
                bread_remove = 'UPDATE Inventory ''SET quantity = %s ''WHERE inventory_item = %s'
                bread_data = (new_quantity, 'Bread')
                cursor.execute(bread_remove, bread_data)
        else:
            print("No quantity result found for 'Bread'")

        # Update Turkey Inventory
        get_turkey = 'SELECT quantity FROM Inventory' ' WHERE inventory_item = %s'
        get_data = ('Turkey',)
        cursor.execute(get_turkey, get_data)
        turkey_result = cursor.fetchone()
        if turkey_result:
            turkey_quantity = turkey_result[0]
            # Not Enough Items In Inventory to Place Order
            if (turkey_quantity < club):
                print("Not enough turkey in inventory")
            # Enough Items In Inventory to Place Order
            else:
                new_quantity = turkey_quantity - club
                turkey_remove = 'UPDATE Inventory ''SET quantity = %s ''WHERE inventory_item = %s'
                turkey_data = (new_quantity, 'Turkey')
                cursor.execute(turkey_remove, turkey_data)
        else:
            print("No quantity result found for 'Turkey'")

        # Update Lettuce Inventory
        get_lettuce = 'SELECT quantity FROM Inventory' ' WHERE inventory_item = %s'
        get_data = ('Lettuce',)
        cursor.execute(get_lettuce, get_data)
        lettuce_result = cursor.fetchone()
        if lettuce_result:
            lettuce_quantity = lettuce_result[0]
            # Not Enough Items In Inventory to Place Order
            if (lettuce_quantity < (club + salad)):
                print("Not enough lettuce in inventory")
            # Enough Items In Inventory to Place Order
            else:
                new_quantity = lettuce_quantity - (club + salad)
                lettuce_remove = 'UPDATE Inventory ''SET quantity = %s ''WHERE inventory_item = %s'
                lettuce_data = (new_quantity, 'Lettuce')
                cursor.execute(lettuce_remove, lettuce_data)
        else:
            print("No quantity result found for 'Lettuce'")

        # Update Tomato Inventory
        get_tomato = 'SELECT quantity FROM Inventory' ' WHERE inventory_item = %s'
        get_data = ('Tomato',)
        cursor.execute(get_tomato, get_data)
        tomato_result = cursor.fetchone()
        if tomato_result:
            tomato_quantity = tomato_result[0]
            # Not Enough Items In Inventory to Place Order
            if (tomato_quantity < club):
                print("Not enough tomato in inventory")
            # Enough Items In Inventory to Place Order
            else:
                new_quantity = tomato_quantity - club
                tomato_remove = 'UPDATE Inventory ''SET quantity = %s ''WHERE inventory_item = %s'
                tomato_data = (new_quantity, 'Tomato')
                cursor.execute(tomato_remove, tomato_data)
        else:
            print("No quantity result found for 'Tomato'")

        # Update Cheese Inventory
        get_cheese = 'SELECT quantity FROM Inventory' ' WHERE inventory_item = %s'
        get_data = ('Cheese',)
        cursor.execute(get_cheese, get_data)
        cheese_result = cursor.fetchone()
        if cheese_result:
            cheese_quantity = cheese_result[0]
            # Not Enough Items In Inventory to Place Order
            if (cheese_quantity < club):
                print("Not enough cheese in inventory")
            # Enough Items In Inventory to Place Order
            else:
                new_quantity = cheese_quantity - club
                cheese_remove = 'UPDATE Inventory ''SET quantity = %s ''WHERE inventory_item = %s'
                cheese_data = (new_quantity, 'Cheese')
                cursor.execute(cheese_remove, cheese_data)
        else:
            print("No quantity result found for 'Cheese'")

        # Update Avocado Inventory
        get_avocado = 'SELECT quantity FROM Inventory' ' WHERE inventory_item = %s'
        get_data = ('Avocado',)
        cursor.execute(get_avocado, get_data)
        avocado_result = cursor.fetchone()
        if avocado_result:
            avocado_quantity = avocado_result[0]
            # Not Enough Items In Inventory to Place Order
            if (avocado_quantity < toast):
                print("Not enough avocado in inventory")
            # Enough Items In Inventory to Place Order
            else:
                new_quantity = avocado_quantity - toast
                avocado_remove = 'UPDATE Inventory ''SET quantity = %s ''WHERE inventory_item = %s'
                avocado_data = (new_quantity, 'Avocado')
                cursor.execute(avocado_remove, avocado_data)
        else:
            print("No quantity result found for 'Avocado'")

        # Update Chicken Inventory
        get_chicken = 'SELECT quantity FROM Inventory' ' WHERE inventory_item = %s'
        get_data = ('Chicken',)
        cursor.execute(get_chicken, get_data)
        chicken_result = cursor.fetchone()
        if chicken_result:
            chicken_quantity = chicken_result[0]
            # Not Enough Items In Inventory to Place Order
            if (chicken_quantity < salad):
                print("Not enough chicken in inventory")
            # Enough Items In Inventory to Place Order
            else:
                new_quantity = chicken_quantity - salad
                chicken_remove = 'UPDATE Inventory ''SET quantity = %s ''WHERE inventory_item = %s'
                chicken_data = (new_quantity, 'Chicken')
                cursor.execute(chicken_remove, chicken_data)
        else:
            print("No quantity result found for 'Chicken'")

        # Update Water Inventory
        get_water = 'SELECT quantity FROM Inventory' ' WHERE inventory_item = %s'
        get_data = ('Water',)
        cursor.execute(get_water, get_data)
        water_result = cursor.fetchone()
        if water_result:
            water_quantity = water_result[0]
            # Not Enough Items In Inventory to Place Order
            if (water_quantity < water):
                print("Not enough water in inventory")
            # Enough Items In Inventory to Place Order
            else:
                new_quantity = water_quantity - water
                water_remove = 'UPDATE Inventory ''SET quantity = %s ''WHERE inventory_item = %s'
                water_data = (new_quantity, 'Water')
                cursor.execute(water_remove, water_data)
        else:
            print("No quantity result found for 'Water'")

        # Update Coffee Inventory
        get_coffee = 'SELECT quantity FROM Inventory' ' WHERE inventory_item = %s'
        get_data = ('coffee',)
        cursor.execute(get_coffee, get_data)
        coffee_result = cursor.fetchone()
        if coffee_result:
            coffee_quantity = coffee_result[0]
            # Not Enough Items In Inventory to Place Order
            if (coffee_quantity < (iced + hot)):
                print("Not enough coffee in inventory")
            # Enough Items In Inventory to Place Order
            else:
                new_quantity = coffee_quantity - (iced + hot)
                coffee_remove = 'UPDATE Inventory ''SET quantity = %s ''WHERE inventory_item = %s'
                coffee_data = (new_quantity, 'Coffee')
                cursor.execute(coffee_remove, coffee_data)
        else:
            print("No quantity result found for 'Coffee'")

        cafe.commit()

        print("Food items ordered have been removed from inventory.")

    except mysql.connector.Error as e:
        print("Cannot connect to database:", e)

if __name__ == "__main__":
    main()
