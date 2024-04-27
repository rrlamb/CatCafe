import tkinter as tk
from tkinter import ttk, CENTER
import random
import Main

email = ""
selected_value = ""
employee_id = 32672


def create_window1():
    global selected_value
    global email
    window1 = tk.Tk()
    window1.configure(bg="light blue")

    window1.geometry("1420x1200")
    heading_font = ("Georgia", 38, "bold")
    subheading_font = ("Georgia", 15)

    label1 = tk.Label(window1, text="CAT CAFE", font=heading_font, foreground="white", bg="light blue")
    label1.pack()
    window1.title("CAT CAFE")

    def customer_check():
        customer_check = tk.Tk()
        customer_check.title("Enter Customer Email")
        customer_check.configure(bg="light blue")
        customer_check.geometry("450x360")

        def check_and_continue():
            global email
            email = email_entry.get()
            if Main.check_customer(email):
                customer()
                customer_check.destroy()
            else:
                create_customer()
                customer_check.destroy()

        email_label = tk.Label(customer_check, text="Enter Your Email:")
        email_label.grid(row=0, column=0, padx=10, pady=5)
        email_entry = tk.Entry(customer_check)
        email_entry.grid(row=0, column=1, padx=10, pady=5)

        check_button = tk.Button(customer_check, text="Submit", command=check_and_continue)
        check_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        customer_check.mainloop()


    def update_employee():
        update_employee = tk.Tk()
        update_employee.configure(bg="light blue")
        update_employee.geometry("1420x1200")

        def check_id():
            global id
            id = id_entry.get()
            if Main.check_employee(id):
                update(Main.check_employee(id))
                update_employee.destroy()
            else:
                create_employee()
                update_employee.destroy()

        id_label = tk.Label(update_employee, text="Enter Employee ID to Update Information For:")
        id_label.grid(row=0, column=0, padx=10, pady=5)
        id_entry = tk.Entry(update_employee)
        id_entry.grid(row=0, column=1, padx=10, pady=5)

        check_button = tk.Button(update_employee, text="Submit", command=check_id)
        check_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        update_employee.mainloop()

    def manage_check():
        manage_check = tk.Tk()
        manage_check.title("Enter Employee ID")
        manage_check.configure(bg="light blue")
        manage_check.geometry("450x360")

        def check():
            global id
            id = id_entry.get()
            if Main.check_manager(id):
                manage_employees()
                manage_check.destroy()
            else:
                id_label = tk.Label(manage_check, text="That is not a valid ID")
                id_label.grid(row=1, column=0, padx=10, pady=5)

        def back_page():
            create_window1()
            manage_check.destroy()

        id_label = tk.Label(manage_check, text="Enter Your Employee ID:")
        id_label.grid(row=0, column=0, padx=10, pady=5)
        id_entry = tk.Entry(manage_check)
        id_entry.grid(row=0, column=1, padx=10, pady=5)

        check_button = tk.Button(manage_check, text="Submit", command=check)
        check_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        back_button = tk.Button(manage_check, text="Back", command=back_page)
        back_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        manage_check.mainloop()

    def manage_employees():
        global employee_id
        manage_employees_window = tk.Tk()
        manage_employees_window.configure(bg="light blue")
        manage_employees_window.geometry("1420x1200")

        manage_employees_window.title("Employees")
        warning = tk.Label(manage_employees_window, text="Highlight employees to select them")
        warning.place(x=650, y=0)




        def delete_user():
            global employee_id

            if Main.check_employee(employee_id):
                if Main.check_employee(employee_id):
                    delete(Main.check_employee(employee_id))
                    manage_employees_window.destroy()
                else:
                    create_employee()
                    manage_employees_window.destroy()

        def back_page():
            create_window1()
            manage_employees_window.destroy()

        def check_id():
            global employee_id
            print (employee_id)
            if Main.check_employee(employee_id):
                update(Main.check_employee(employee_id))
                manage_employees_window.destroy()
            else:
                create_employee()
                manage_employees_window.destroy()
        def create():
            employee_check2()



        def view_employee():

            def on_select(event):
                global selected_value
                global employee_id
                selected_item = tree.selection()[0]  # Get the selected item
                selected_values = tree.item(selected_item, 'values')  # Get the values of the selected item
                selected_value = selected_values[0]
                # Do something with the selected data
                print("Selected row:", selected_values[0])
                employee_id = int(selected_values[0])



            tree = ttk.Treeview(manage_employees_window, show="headings")
            tree["columns"] = ("ID", "First Name", "Last Name", "Role", "Email", "Age",
                               "Phone Number", "Bank Account Number", "Available Item")  # Replace with your column names
            tree.column("ID", width=100, anchor = CENTER)
            tree.heading("ID", text="ID")
            tree.column("First Name", width=100, anchor = CENTER)
            tree.heading("First Name", text="First Name")
            tree.column("Last Name", width=100, anchor = CENTER)
            tree.heading("Last Name", text="Last Name")
            tree.column("Role", width=100, anchor = CENTER)
            tree.heading("Role", text="Role")
            tree.column("Email", width=100, anchor = CENTER)
            tree.heading("Email", text="Email")
            tree.column("Age", width=100, anchor = CENTER)
            tree.heading("Age", text="Age")
            tree.column("Phone Number", width=100, anchor = CENTER)
            tree.heading("Phone Number", text="Phone Number")
            tree.column("Bank Account Number", width=100, anchor = CENTER)
            tree.heading("Bank Account Number", text="Bank Account Number")
            tree.column("Available Item", width=100, anchor = CENTER)
            tree.heading("Available Item", text="Available Item")
            tree.pack(fill="none", expand=True,  anchor = CENTER)
            tree.place()
            tree.bind("<ButtonRelease-1>", on_select)

            # Fetch data from the database
            rows = Main.view_table("Employee")
            # Clear existing data in the Treeview
            for row in tree.get_children():
                tree.delete(row)
            # Insert fetched data into the Treeview
            for row in rows:
                tree.insert('', 'end', values=row)



        view_employee()
        delete_button1 = tk.Button(manage_employees_window, text="Add User", command=create)
        delete_button1.place(x=550,y=800)
        delete_button2 = tk.Button(manage_employees_window, text="Update User", command=check_id)
        delete_button2.place(x=650,y=800)
        delete_button3 = tk.Button(manage_employees_window, text="Delete User", command=delete_user)
        delete_button3.place(x=750, y=800)


        manage_employees_window.mainloop()
    def delete_employee():
        delete_employee = tk.Tk()
        delete_employee.configure(bg="light blue")
        delete_employee.geometry("1420x1200")

        def check_id_delete():
            global id
            id = id_entry.get()
            if Main.check_employee(id):
                delete(Main.check_employee(id))
                delete_employee.destroy()
            else:
                create_employee()
                delete_employee.destroy()

        id_label = tk.Label(delete_employee, text="Enter Employee ID to Delete:")
        id_label.grid(row=0, column=0, padx=10, pady=5)
        id_entry = tk.Entry(delete_employee)
        id_entry.grid(row=0, column=1, padx=10, pady=5)

        check_button = tk.Button(delete_employee, text="Submit", command=check_id_delete)
        check_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        delete_employee.mainloop()

    def employee_check2():
        employee_check2 = tk.Tk()
        employee_check2.configure(bg="light blue")
        employee_check2.geometry("1420x1200")

        def check():
            global id
            id = id_entry.get()
            if Main.check_employee(id):
                warning = tk.Label(employee_check2, text="ID already exists")
                warning.grid(row=2, column=0, padx=10, pady=5)
                employee_check2()
            else:
                create_employee(id)
                employee_check2.destroy()

        id_label = tk.Label(employee_check2, text="Enter New Employee ID:")
        id_label.grid(row=0, column=0, padx=10, pady=5)
        id_entry = tk.Entry(employee_check2)
        id_entry.grid(row=0, column=1, padx=10, pady=5)

        check_button = tk.Button(employee_check2, text="Submit", command=check)
        check_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        employee_check2.mainloop()

    def create_employee(new_id):
        create_employee_window = tk.Tk()
        create_employee_window.configure(bg="light blue")
        create_employee_window.geometry("680x360")

        create_employee_window.title("Create Employee")

        def create_employee():
            id = new_id
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            role = role_entry.get()
            email = email_entry.get()
            age = age_entry.get()
            phone_number = phone_number_entry.get()
            bank_account_number = bank_account_number_entry.get()
            available_item = available_item_entry.get()
            # Call a method in main to create the employee
            Main.create_employee(id, first_name, last_name, role, email, age, phone_number, bank_account_number,
                                 available_item)
            create_window1()
            create_employee_window.destroy()


        first_name_label = tk.Label(create_employee_window, text="First Name:")
        first_name_label.grid(row=0, column=0, padx=10, pady=5)
        first_name_entry = tk.Entry(create_employee_window)
        first_name_entry.grid(row=0, column=1, padx=10, pady=5)

        last_name_label = tk.Label(create_employee_window, text="Last Name:")
        last_name_label.grid(row=1, column=0, padx=10, pady=5)
        last_name_entry = tk.Entry(create_employee_window)
        last_name_entry.grid(row=1, column=1, padx=10, pady=5)

        role_label = tk.Label(create_employee_window, text="Role:")
        role_label.grid(row=2, column=0, padx=10, pady=5)
        role_entry = tk.Entry(create_employee_window)
        role_entry.grid(row=2, column=1, padx=10, pady=5)

        email_label = tk.Label(create_employee_window, text="Email:")
        email_label.grid(row=3, column=0, padx=10, pady=5)
        email_entry = tk.Entry(create_employee_window)
        email_entry.grid(row=3, column=1, padx=10, pady=5)

        age_label = tk.Label(create_employee_window, text="Age:")
        age_label.grid(row=4, column=0, padx=10, pady=5)
        age_entry = tk.Entry(create_employee_window)
        age_entry.grid(row=4, column=1, padx=10, pady=5)

        phone_number_label = tk.Label(create_employee_window, text="Phone Number:")
        phone_number_label.grid(row=5, column=0, padx=10, pady=5)
        phone_number_entry = tk.Entry(create_employee_window)
        phone_number_entry.grid(row=5, column=1, padx=10, pady=5)

        bank_account_number_label = tk.Label(create_employee_window, text="Bank Account Number:")
        bank_account_number_label.grid(row=6, column=0, padx=10, pady=5)
        bank_account_number_entry = tk.Entry(create_employee_window)
        bank_account_number_entry.grid(row=6, column=1, padx=10, pady=5)

        available_item_label = tk.Label(create_employee_window, text="Available Item:")
        available_item_label.grid(row=7, column=0, padx=10, pady=5)
        available_item_entry = tk.Entry(create_employee_window)
        available_item_entry.grid(row=7, column=1, padx=10, pady=5)

        create_button = tk.Button(create_employee_window, text="Create Employee", command=create_employee)
        create_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        create_employee_window.mainloop()

    def delete(id):
        delete_window = tk.Tk()
        delete_window.configure(bg="light blue")
        delete_window.geometry("1420x1200")

        delete_window.title("Are You Sure You Want To Delete This Employee?")
        warning = tk.Label(delete_window, text="Are you sure you want to delete the following employee? This cannot be undone.")
        warning.place(x=500, y=0)

        def delete_user():


            # Call a method in main to create the user
            Main.delete(id[0])

            create_window1()
            delete_window.destroy()

        def back_page():
            create_window1()
            delete_window.destroy()



        def view_employee():
            tree = ttk.Treeview(delete_window, show="headings")
            tree["columns"] = ("ID", "First Name", "Last Name", "Role", "Email", "Age",
                               "Phone Number", "Bank Account Number", "Available Item")  # Replace with your column names
            tree.column("ID", width=100, anchor = CENTER)
            tree.heading("ID", text="ID")
            tree.column("First Name", width=100, anchor = CENTER)
            tree.heading("First Name", text="First Name")
            tree.column("Last Name", width=100, anchor = CENTER)
            tree.heading("Last Name", text="Last Name")
            tree.column("Role", width=100, anchor = CENTER)
            tree.heading("Role", text="Role")
            tree.column("Email", width=100, anchor = CENTER)
            tree.heading("Email", text="Email")
            tree.column("Age", width=100, anchor = CENTER)
            tree.heading("Age", text="Age")
            tree.column("Phone Number", width=100, anchor = CENTER)
            tree.heading("Phone Number", text="Phone Number")
            tree.column("Bank Account Number", width=100, anchor = CENTER)
            tree.heading("Bank Account Number", text="Bank Account Number")
            tree.column("Available Item", width=100, anchor = CENTER)
            tree.heading("Available Item", text="Available Item")
            tree.pack(fill="none", expand=True,  anchor = CENTER)
            tree.place()

            # Fetch data from the database
            rows = Main.view_employee(id)
            # Clear existing data in the Treeview
            for row in tree.get_children():
                tree.delete(row)
            # Insert fetched data into the Treeview
            for row in rows:
                tree.insert('', 'end', values=row)

        view_employee()
        delete_button1 = tk.Button(delete_window, text="Delete User", command=delete_user)
        delete_button1.place(x=650,y=700)
        delete_button2 = tk.Button(delete_window, text="Back", command=back_page)
        delete_button2.place(x=650,y=800)

        delete_window.mainloop()


    def employee_check():
        employee_check = tk.Tk()
        employee_check.title("Enter Employee ID")
        employee_check.configure(bg="light blue")

        def check():
            global id
            id = id_entry.get()
            if Main.check_employee(id):
                employee()
                employee_check.destroy()
            else:
                id_label = tk.Label(employee_check, text="That is not a valid ID")
                id_label.grid(row=1, column=0, padx=10, pady=5)

        def back_page():
            create_window1()
            employee_check.destroy()

        id_label = tk.Label(employee_check, text="Enter Your Employee ID:")
        id_label.grid(row=0, column=0, padx=10, pady=5)
        id_entry = tk.Entry(employee_check)
        id_entry.grid(row=0, column=1, padx=10, pady=5)

        check_button = tk.Button(employee_check, text="Submit", command=check)
        check_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        back_button = tk.Button(employee_check, text="Back", command=back_page)
        back_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        employee_check.mainloop()

    def update(id):
        update_window = tk.Tk()
        update_window.configure(bg="light blue")

        update_window.title("Update Employee Information: Only enter information for what you want to update")

        employee_label = tk.Label(update_window, text="Current Employee Info", font=subheading_font, bg="light blue")
        employee_label.pack()
        employee_label.place(x=600, y=0)
        tree3 = ttk.Treeview(update_window, show="headings")
        tree3["columns"] = ("ID", "First Name", "Last Name", "Role", "Email", "Age",
                            "Phone Number", "Bank Account Number", "Available Item")  # Replace with your column names
        tree3.column("ID", width=55)
        tree3.heading("ID", text="ID")
        tree3.column("First Name", width=55)
        tree3.heading("First Name", text="First")
        tree3.column("Last Name", width=55)
        tree3.heading("Last Name", text="Last")
        tree3.column("Role", width=55)
        tree3.heading("Role", text="Role")
        tree3.column("Email", width=55)
        tree3.heading("Email", text="Email")
        tree3.column("Age", width=55)
        tree3.heading("Age", text="Age")
        tree3.column("Phone Number", width=55)
        tree3.heading("Phone Number", text="Phone #")
        tree3.column("Bank Account Number", width=55)
        tree3.heading("Bank Account Number", text="Bank #")
        tree3.column("Available Item", width=55)
        tree3.heading("Available Item", text="Item")
        tree3.pack(fill="none", expand=True)
        tree3.place(x=500, y=50)
        # Fetch data from the database
        rows = Main.view_employee(id)
        print(str(rows))
        # Clear existing data in the Treeview
        for row in tree3.get_children():
            tree3.delete(row)
        # Insert fetched data into the Treeview
        for row in rows:
            tree3.insert('', 'end', values=row)

        def update_employee():
            update_listColumns=[]
            update_listValues=[]
            first_name = first_name_entry.get()
            if(len(first_name)!=0):
                update_listColumns.append("first_name")
                update_listValues.append(first_name)
            last_name = last_name_entry.get()
            if (len(last_name) != 0):
                update_listColumns.append("last_name")
                update_listValues.append(last_name)
            role = role_entry.get()
            if (len(role) != 0):
                update_listColumns.append("role")
                update_listValues.append(role)
            email = email_entry.get()
            if (len(email) != 0):
                update_listColumns.append("email")
                update_listValues.append(email)
            age = age_entry.get()
            if (len(age) != 0):
                update_listColumns.append("age")
                update_listValues.append(age)
            phone_number = phone_number_entry.get()
            if (len(phone_number) != 0):
                update_listColumns.append("phone_number")
                update_listValues.append(phone_number)
            bank_account_number = bank_account_number_entry.get()
            if (len(bank_account_number) != 0):
                update_listColumns.append("bank_account_number")
                update_listValues.append(bank_account_number)
            available_item = available_item_entry.get()
            if (len(available_item) != 0):
                update_listColumns.append("available_item")
                update_listValues.append(available_item)


            # Call a method in main to update the employee
            Main.update_employee(id, update_listColumns, update_listValues)
            create_window1()
            update_window.destroy()

        first_name_label = tk.Label(update_window, text="Updating information for: " + str(id[0]))
        first_name_label.grid(row=0, column=0, padx=10, pady=5)

        first_name_label = tk.Label(update_window, text="First Name:")
        first_name_label.grid(row=1, column=0, padx=10, pady=5)
        first_name_entry = tk.Entry(update_window)
        first_name_entry.grid(row=1, column=1, padx=10, pady=5)

        last_name_label = tk.Label(update_window, text="Last Name:")
        last_name_label.grid(row=2, column=0, padx=10, pady=5)
        last_name_entry = tk.Entry(update_window)
        last_name_entry.grid(row=2, column=1, padx=10, pady=5)

        role_label = tk.Label(update_window, text="Role:")
        role_label.grid(row=3, column=0, padx=10, pady=5)
        role_entry = tk.Entry(update_window)
        role_entry.grid(row=3, column=1, padx=10, pady=5)

        email_label = tk.Label(update_window, text="Email:")
        email_label.grid(row=4, column=0, padx=10, pady=5)
        email_entry = tk.Entry(update_window)
        email_entry.grid(row=4, column=1, padx=10, pady=5)

        age_label = tk.Label(update_window, text="Age:")
        age_label.grid(row=5, column=0, padx=10, pady=5)
        age_entry = tk.Entry(update_window)
        age_entry.grid(row=5, column=1, padx=10, pady=5)

        phone_number_label = tk.Label(update_window, text="Phone Number:")
        phone_number_label.grid(row=6, column=0, padx=10, pady=5)
        phone_number_entry = tk.Entry(update_window)
        phone_number_entry.grid(row=6, column=1, padx=10, pady=5)

        bank_account_number_label = tk.Label(update_window, text="Bank Account Number:")
        bank_account_number_label.grid(row=7, column=0, padx=10, pady=5)
        bank_account_number_entry = tk.Entry(update_window)
        bank_account_number_entry.grid(row=7, column=1, padx=10, pady=5)

        available_item_label = tk.Label(update_window, text="Available Item:")
        available_item_label.grid(row=8, column=0, padx=10, pady=5)
        available_item_entry = tk.Entry(update_window)
        available_item_entry.grid(row=8, column=1, padx=10, pady=5)

        submit_button = tk.Button(update_window, text="Update Employee", command=update_employee)
        submit_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        update_window.mainloop()



    def create_customer():
        create_customer_window = tk.Tk()
        create_customer_window.configure(bg="light blue")
        create_customer_window.geometry("680x360")

        create_customer_window.title("Create Customer")

        def create_user():
            global email
            email = email_entry.get()
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()

            # Call a method in main to create the user
            Main.create_customer(email, first_name, last_name)

            customer()
            create_customer_window.destroy()

        email_label = tk.Label(create_customer_window, text="Email:")
        email_label.grid(row=0, column=0, padx=10, pady=5)
        email_entry = tk.Entry(create_customer_window)
        email_entry.grid(row=0, column=1, padx=10, pady=5)

        first_name_label = tk.Label(create_customer_window, text="First Name:")
        first_name_label.grid(row=1, column=0, padx=10, pady=5)
        first_name_entry = tk.Entry(create_customer_window)
        first_name_entry.grid(row=1, column=1, padx=10, pady=5)

        last_name_label = tk.Label(create_customer_window, text="Last Name:")
        last_name_label.grid(row=2, column=0, padx=10, pady=5)
        last_name_entry = tk.Entry(create_customer_window)
        last_name_entry.grid(row=2, column=1, padx=10, pady=5)

        create_button = tk.Button(create_customer_window, text="Create Customer", command=create_user)
        create_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        create_customer_window.mainloop()

    def employee():
        window1.destroy()
        # Employee Window
        employee = tk.Tk()
        employee.configure(bg="light blue")
        employee.geometry("1420x1200")
        # Header saying name of window
        label3 = tk.Label(employee, text="Employee View", font=heading_font, foreground="white", bg="light blue")
        label3.pack()
        employee.title("Employee View")

        def back():
            employee.destroy()
            create_window1()

        def update2():
            update(id)
            employee.destroy()

        backBtn = tk.Button(employee, text="Back", command=back, bg="light blue")
        backBtn.pack()
        backBtn.place(x=750, y=1000)

        updateBtn = tk.Button(employee, text="Update", command=update2, bg="light blue")
        updateBtn.pack()
        updateBtn.place(x=1125, y=925)

        #Turkey Club Menu Item
        turkeyclub_label = tk.Label(employee, text="0", font=("Georgia", 20), bg="light blue")
        turkeyclub_label.pack()
        turkeyclub_label.place(x=250, y=100)

        def inc():
            current = int(turkeyclub_label["text"])
            turkeyclub_label["text"] = str(current + 1)

        def dec():
            current = int(turkeyclub_label["text"])
            if current > 0:
                turkeyclub_label["text"] = str(current - 1)

        turkey_price = tk.Label(employee, text="1. Turkey Club: $12.25 ", font=subheading_font, bg="light blue")
        turkey_price.pack()
        turkey_price.place(x=0, y=100)

        incBtn = tk.Button(employee, text="+", command=inc, bg="light blue")
        decBtn = tk.Button(employee, text="-", command=dec, bg="light blue")
        incBtn.pack()
        incBtn.place(x=300, y=100)
        decBtn.pack()
        decBtn.place(x=350, y=100)

        club_edits = tk.Text(employee, width=50, height=1.5)
        club_edits.insert("1.0", "Modifications:")
        club_edits.pack()
        club_edits.place(x=400, y=100)

        #Avocado Toast Menu Item

        toast_label = tk.Label(employee, text="0", font=("Georgia", 20), bg="light blue")
        toast_label.pack()
        toast_label.place(x=250, y=200)

        def inc_toast():
            current = int(toast_label["text"])
            toast_label["text"] = str(current + 1)

        def dec_toast():
            current = int(toast_label["text"])
            if current > 0:
                toast_label["text"] = str(current - 1)

        avocado_price = tk.Label(employee, text="2. Avocado Toast: $8.50 ", font=subheading_font, bg="light blue")
        avocado_price.pack()
        avocado_price.place(x=0, y=200)

        incBtn_toast = tk.Button(employee, text="+", command=inc_toast, bg="light blue")
        decBtn_toast = tk.Button(employee, text="-", command=dec_toast, bg="light blue")
        incBtn_toast.pack()
        incBtn_toast.place(x=300, y=200)
        decBtn_toast.pack()
        decBtn_toast.place(x=350, y=200)

        toast_edits = tk.Text(employee, width=50, height=1.5)
        toast_edits.insert("1.0", "Modifications:")
        toast_edits.pack()
        toast_edits.place(x=400, y=200)

        #Chicken Ceasar Salad Menu Item
        salad_label = tk.Label(employee, text="0", font=("Georgia", 20), bg="light blue")
        salad_label.pack()
        salad_label.place(x=250, y=300)

        def inc_salad():
            current = int(salad_label["text"])
            salad_label["text"] = str(current + 1)

        def dec_salad():
            current = int(salad_label["text"])
            if current > 0:
                salad_label["text"] = str(current - 1)

        salad_price = tk.Label(employee, text="3. Chicken Salad: $10.75 ", font=subheading_font, bg="light blue")
        salad_price.pack()
        salad_price.place(x=0, y=300)

        incBtn_salad = tk.Button(employee, text="+", command=inc_salad, bg="light blue")
        decBtn_salad = tk.Button(employee, text="-", command=dec_salad, bg="light blue")
        incBtn_salad.pack()
        incBtn_salad.place(x=300, y=300)
        decBtn_salad.pack()
        decBtn_salad.place(x=350, y=300)

        salad_edits = tk.Text(employee, width=50, height=1.5)
        salad_edits.insert("1.0", "Modifications:")
        salad_edits.pack()
        salad_edits.place(x=400, y=300)

        #Water Cup Menu Item

        water_label = tk.Label(employee, text="0", font=("Georgia", 20), bg="light blue")
        water_label.pack()
        water_label.place(x=250, y=400)

        def inc_water():
            current = int(water_label["text"])
            water_label["text"] = str(current + 1)

        def dec_water():
            current = int(water_label["text"])
            if current > 0:
                water_label["text"] = str(current - 1)

        water_price = tk.Label(employee, text="4. Water Cup: FREE", font=subheading_font, bg="light blue")
        water_price.pack()
        water_price.place(x=0, y=400)

        incBtn_water = tk.Button(employee, text="+", command=inc_water, bg="light blue")
        decBtn_water = tk.Button(employee, text="-", command=dec_water, bg="light blue")
        incBtn_water.pack()
        incBtn_water.place(x=300, y=400)
        decBtn_water.pack()
        decBtn_water.place(x=350, y=400)

        water_edits = tk.Text(employee, width=50, height=1.5)
        water_edits.insert("1.0", "Modifications:")
        water_edits.pack()
        water_edits.place(x=400, y=400)

        #Iced Coffee Menu Item
        iced_label = tk.Label(employee, text="0", font=("Georgia", 20), bg="light blue")
        iced_label.pack()
        iced_label.place(x=250, y=500)

        def inc_iced():
            current = int(iced_label["text"])
            iced_label["text"] = str(current + 1)

        def dec_iced():
            current = int(iced_label["text"])
            if current > 0:
                iced_label["text"] = str(current - 1)

        iced_price = tk.Label(employee, text="5. Iced Coffee: $4.50", font=subheading_font, bg="light blue")
        iced_price.pack()
        iced_price.place(x=0, y=500)

        incBtn_iced = tk.Button(employee, text="+", command=inc_iced, bg="light blue")
        decBtn_iced = tk.Button(employee, text="-", command=dec_iced, bg="light blue")
        incBtn_iced.pack()
        incBtn_iced.place(x=300, y=500)
        decBtn_iced.pack()
        decBtn_iced.place(x=350, y=500)

        iced_edits = tk.Text(employee, width=50, height=1.5)
        iced_edits.insert("1.0", "Modifications:")
        iced_edits.pack()
        iced_edits.place(x=400, y=500)

        #Hot Coffee Menu Item
        hot_label = tk.Label(employee, text="0", font=("Georgia", 20), bg="light blue")
        hot_label.pack()
        hot_label.place(x=250, y=600)

        def inc_hot():
            current = int(hot_label["text"])
            hot_label["text"] = str(current + 1)

        def dec_hot():
            current = int(hot_label["text"])
            if current > 0:
                hot_label["text"] = str(current - 1)

        hot_price = tk.Label(employee, text="6. Hot Coffee: $3.50", font=subheading_font, bg="light blue")
        hot_price.pack()
        hot_price.place(x=0, y=600)

        incBtn_hot = tk.Button(employee, text="+", command=inc_hot, bg="light blue")
        decBtn_hot = tk.Button(employee, text="-", command=dec_hot, bg="light blue")
        incBtn_hot.pack()
        incBtn_hot.place(x=300, y=600)
        decBtn_hot.pack()
        decBtn_hot.place(x=350, y=600)

        hot_edits = tk.Text(employee, width=50, height=1.5)
        hot_edits.insert("1.0", "Modifications:")
        hot_edits.pack()
        hot_edits.place(x=400, y=600)

        email_label = tk.Label(employee, text="Customer Email (if applicable): ", font=subheading_font, bg="light blue")
        email_label.pack()
        email_label.place(x=0, y=700)
        customer_email = tk.Text(employee, width=50, height=1.5)
        customer_email.pack()
        customer_email.place(x=300, y=700)

        def on_select(event):
            global selected_value
            selected_item = tree.selection()[0]  # Get the selected item
            selected_values = tree.item(selected_item, 'values')  # Get the values of the selected item
            selected_value = selected_values[0]
            # Do something with the selected data
            print("Selected row:", selected_values[0])

        tree = ttk.Treeview(employee, show="headings")
        tree["columns"] = ("Item", "Quantity")
        tree.heading("Item", text="Item")
        tree.heading("Quantity", text="Quantity")
        tree.pack(fill="none", side="right", anchor='n')
        tree.place(x=957, y=100)
        tree.bind("<ButtonRelease-1>", on_select)

        def view_table(table_name):
            # Fetch data from the database
            rows = Main.view_table(table_name)
            # Clear existing data in the Treeview
            for row in tree.get_children():
                tree.delete(row)
            # Insert fetched data into the Treeview
            for row in rows:
                tree.insert('', 'end', values=row)

        # View Inventory Items
        inventory_items = tk.Label(employee, text="Inventory", font=subheading_font, bg="light blue")
        inventory_items.pack()
        inventory_items.place(x=1100, y=50)
        view_table("Inventory")

        tree2 = ttk.Treeview(employee, show="headings")
        tree2["columns"] = ("Customer Name", "Cat Name")
        tree2.heading("Customer Name", text="Customer Name")
        tree2.heading("Cat Name", text="Cat Name")
        tree2.pack(fill="none", side="right", anchor='n')
        tree2.place(x=957, y=390)

        employee_label = tk.Label(employee, text="Employee Info", font=subheading_font, bg="light blue")
        employee_label.pack()
        employee_label.place(x=1100, y=625)
        tree3 = ttk.Treeview(employee, show="headings")
        tree3["columns"] = ("ID", "First Name", "Last Name", "Role", "Email", "Age",
                           "Phone Number", "Bank Account Number", "Available Item")  # Replace with your column names
        tree3.column("ID", width=55)
        tree3.heading("ID", text="ID")
        tree3.column("First Name", width=55)
        tree3.heading("First Name", text="First")
        tree3.column("Last Name", width=55)
        tree3.heading("Last Name", text="Last")
        tree3.column("Role", width=55)
        tree3.heading("Role", text="Role")
        tree3.column("Email", width=55)
        tree3.heading("Email", text="Email")
        tree3.column("Age", width=55)
        tree3.heading("Age", text="Age")
        tree3.column("Phone Number", width=55)
        tree3.heading("Phone Number", text="Phone #")
        tree3.column("Bank Account Number", width=55)
        tree3.heading("Bank Account Number", text="Bank #")
        tree3.column("Available Item", width=55)
        tree3.heading("Available Item", text="Item")
        tree3.pack(fill="none", expand=True)
        tree3.place(x=900,y=675)

        print(str(id))
        # Fetch data from the database
        rows = Main.view_employee(id)
        print(str(rows))
        # Clear existing data in the Treeview
        for row in tree3.get_children():
            tree3.delete(row)
        # Insert fetched data into the Treeview
        for row in rows:
            tree3.insert('', 'end', values=row)

        def view_join_table():
            # Fetch data from the database
            rows = Main.view_join_table()
            # Clear existing data in the Treeview
            for row in tree2.get_children():
                tree2.delete(row)
            # Insert fetched data into the Treeview
            for row in rows:
                tree2.insert('', 'end', values=row)

        # View Inventory Items
        customercat = tk.Label(employee, text="Customer and Cat:", font=subheading_font, bg="light blue")
        customercat.pack()
        customercat.place(x=1075, y=340)
        view_join_table()

        def complete_order():
            entered_email = customer_email.get("1.0", "end-1c")
            print(entered_email)
            total_cost = 0
            total_points = 0
            if int(turkeyclub_label["text"]) > 0:
                turkey_cost = (round((int(turkeyclub_label["text"]) * 12.25), 2))
                total_cost = total_cost + turkey_cost
                turkey_points = (int(turkeyclub_label["text"]) * 100)
                total_points = total_points + turkey_points

            if int(toast_label["text"]) > 0:
                toast_cost = (round((int(toast_label["text"]) * 8.50), 2))
                total_cost = total_cost + toast_cost
                toast_points = (int(toast_label["text"]) * 50)
                total_points = total_points + toast_points

            if int(salad_label["text"]) > 0:
                salad_cost = (round((int(salad_label["text"]) * 10.75), 2))
                total_cost = total_cost + salad_cost
                salad_points = (int(salad_label["text"]) * 75)
                total_points = total_points + salad_points

            if int(iced_label["text"]) > 0:
                iced_cost = (round((int(iced_label["text"]) * 4.50), 2))
                total_cost = total_cost + iced_cost
                iced_points = (int(iced_label["text"]) * 25)
                total_points = total_points + iced_points

            if int(hot_label["text"]) > 0:
                hot_cost = (round((int(hot_label["text"]) * 3.50), 2))
                total_cost = total_cost + hot_cost
                hot_points = (int(hot_label["text"]) * 15)
                total_points = total_points + hot_points

            if entered_email:
                if (Main.check_customer(entered_email)):
                    Main.add_customer_points(entered_email, total_points)

            Main.inventory_remove((int(turkeyclub_label["text"])), (int(toast_label["text"])),
                                  (int(salad_label["text"])), (int(water_label["text"])), (int(iced_label["text"])),
                                  (int(hot_label["text"])));

            hot_label["text"] = 0
            water_label["text"] = 0
            iced_label["text"] = 0
            salad_label["text"] = 0
            toast_label["text"] = 0
            turkeyclub_label["text"] = 0

            if Main.inventory_low():
                low_items = tk.Label(employee, text="LOW INVENTORY ITEMS: ", font=subheading_font, foreground='red',
                                     bg="light blue")
                low_items.pack()
                low_items.place(x=100, y=900)
                result = Main.inventory_low()
                my_string = ' , '.join([str(x) for x in result])
                low_items_list = tk.Label(employee, text=my_string, font=subheading_font, foreground='red',
                                          bg="light blue")
                low_items_list.pack()
                low_items_list.place(x=350, y=900)

            final_cost_label = tk.Label(employee, text="Total Cost: $" + str(total_cost), font=subheading_font,
                                        bg="light blue")
            final_cost_label.pack()
            final_cost_label.place(x=200, y=775)
            earned_points_label = tk.Label(employee,
                                           text="Total Points Earned from Order: " + str(total_points) + " points",
                                           font=subheading_font, bg="light blue")
            earned_points_label.pack()
            earned_points_label.place(x=200, y=825)

            view_table("Inventory")

        complete_order_btn = tk.Button(employee, text="Complete Order!", command=complete_order, bg="light blue")
        complete_order_btn.pack()
        complete_order_btn.place(x=750, y=705)

        employee.mainloop()

    def customer():
        def on_select(event):
            global selected_value
            selected_item = tree.selection()[0]  # Get the selected item
            selected_values = tree.item(selected_item, 'values')  # Get the values of the selected item
            selected_value = selected_values[0]
            # Do something with the selected data
            print("Selected row:", selected_values[0])

        def select_cat():
            global email
            global selected_value
            Main.select_cat(email, selected_value)
            view_table("Cat")

        def adopt_cat():
            global email
            global selected_value
            Main.adopt_cat(selected_value)
            view_table("Cat")

        def view_table(table_name):
            # Fetch data from the database
            rows = Main.view_table(table_name)
            # Clear existing data in the Treeview
            for row in tree.get_children():
                tree.delete(row)

            # Insert fetched data into the Treeview
            for row in rows:
                tree.insert('', 'end', values=row)

        window1.destroy()
        # Customer Window
        customer = tk.Tk()
        customer.configure(bg="light blue")
        customer.geometry("1420x1200")
        # Header saying name of window
        label2 = tk.Label(customer, text="Cat Adoption Information", font=heading_font, foreground="white",
                          bg="light blue")
        label2.pack()
        customer.title("Employee View")

        tree = ttk.Treeview(customer, show="headings")
        tree["columns"] = ("Cat Name", "Breed", "Sex", "Age", "Weight", "Adoption Phone",
                           "Customer Name")  # Replace with your column names
        tree.heading("Cat Name", text="Cat Name")
        tree.heading("Breed", text="Breed")
        tree.heading("Sex", text="Sex")
        tree.heading("Age", text="Age")
        tree.heading("Weight", text="Weight")
        tree.heading("Adoption Phone", text="Adoption Phone")
        tree.heading("Customer Name", text="Customer Name")
        tree.pack(fill="x", expand=True, side="top")

        tree.bind("<ButtonRelease-1>", on_select)

        view_table("Cat")

        adopt_button = tk.Button(customer, text="Adopt Cat", command=adopt_cat)
        adopt_button.pack()
        adopt_button.place(x=680, y=700)

        select_button = tk.Button(customer, text="Select Cat", command=select_cat)
        select_button.pack()
        select_button.place(x=680, y=725)

        def back():
            customer.destroy()
            create_window1()

        backBtn = tk.Button(customer, text="Back", command=back, bg="light blue")
        backBtn.pack()
        backBtn.place(x=680, y=750)
        customer.mainloop()

    def exit():
        window1.destroy()

    customerBtn = tk.Button(window1, text="Customer", command=customer_check, bg="light blue")
    employeeBtn = tk.Button(window1, text="Employee", command=employee_check, bg="light blue")
    manageBtn = tk.Button(window1, text="Manage Employees", command=manage_check, bg="light blue")
    exitBtn = tk.Button(window1, text="Exit", command=exit, bg="light blue")

    employeeBtn.pack()
    employeeBtn.place(x=670, y=100)
    customerBtn.pack()
    customerBtn.place(x=670, y=200)
    manageBtn.pack()
    manageBtn.place(x=670, y=300)
    exitBtn.pack()
    exitBtn.place(x=670, y=750)

    window1.mainloop()


create_window1()
