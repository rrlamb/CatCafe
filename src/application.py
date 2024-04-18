import tkinter as tk
from tkinter import ttk
import random
import Main

email = ""
selected_value = ""

def create_window1():
    global selected_value
    global email
    window1= tk.Tk()
    window1.configure(bg="light blue")

    window1.geometry("1420x1200")
    heading_font=("Georgia", 38, "bold")
    subheading_font=("Georgia", 15)


    label1=tk.Label(window1, text="CAT CAFE", font=heading_font, foreground="white", bg= "light blue")
    label1.pack()
    window1.title("CAT CAFE")

    def customer_check():
        customer_check = tk.Tk()
        customer_check.configure(bg="light blue")
        customer_check.geometry("1420x1200")

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

    def create_customer():
        create_customer_window = tk.Tk()
        create_customer_window.configure(bg="light blue")
        create_customer_window.geometry("1420x1200")

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

        backBtn = tk.Button(employee, text="Back", command=back, bg="light blue")
        backBtn.pack()
        backBtn.place(x=680, y=750)

        #Turkey Club Menu Item
        turkeyclub_label = tk.Label(employee, text="0", font=("Georgia", 20), bg="light blue")
        turkeyclub_label.pack()
        turkeyclub_label.place(x=200, y=100)

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
        incBtn.place(x=250, y=100)
        decBtn.pack()
        decBtn.place(x=300, y=100)

        club_edits = tk.Text(employee, width=50, height=1.5)
        club_edits.insert("1.0", "Modifications:")
        club_edits.pack()
        club_edits.place(x=400, y=100)

        #Avocado Toast Menu Item

        toast_label = tk.Label(employee, text="0", font=("Georgia", 20), bg="light blue")
        toast_label.pack()
        toast_label.place(x=200, y=200)

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
        incBtn_toast.place(x=250, y=200)
        decBtn_toast.pack()
        decBtn_toast.place(x=300, y=200)

        toast_edits = tk.Text(employee, width=50, height=1.5)
        toast_edits.insert("1.0", "Modifications:")
        toast_edits.pack()
        toast_edits.place(x=400, y=200)


        #Chicken Ceasar Salad Menu Item
        salad_label = tk.Label(employee, text="0", font=("Georgia", 20), bg="light blue")
        salad_label.pack()
        salad_label.place(x=200, y=300)

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
        incBtn_salad.place(x=250, y=300)
        decBtn_salad.pack()
        decBtn_salad.place(x=300, y=300)

        salad_edits = tk.Text(employee, width=50, height=1.5)
        salad_edits.insert("1.0", "Modifications:")
        salad_edits.pack()
        salad_edits.place(x=400, y=300)


        #Water Cup Menu Item

        water_label = tk.Label(employee, text="0", font=("Georgia", 20), bg="light blue")
        water_label.pack()
        water_label.place(x=200, y=400)

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
        incBtn_water.place(x=250, y=400)
        decBtn_water.pack()
        decBtn_water.place(x=300, y=400)

        water_edits = tk.Text(employee, width=50, height=1.5)
        water_edits.insert("1.0", "Modifications:")
        water_edits.pack()
        water_edits.place(x=400, y=400)

        #Iced Coffee Menu Item
        iced_label = tk.Label(employee, text="0", font=("Georgia", 20), bg="light blue")
        iced_label.pack()
        iced_label.place(x=200, y=500)


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
        incBtn_iced.place(x=250, y=500)
        decBtn_iced.pack()
        decBtn_iced.place(x=300, y=500)

        iced_edits = tk.Text(employee, width=50, height=1.5)
        iced_edits.insert("1.0", "Modifications:")
        iced_edits.pack()
        iced_edits.place(x=400, y=500)

        #Hot Coffee Menu Item
        hot_label = tk.Label(employee, text="0", font=("Georgia", 20), bg="light blue")
        hot_label.pack()
        hot_label.place(x=200, y=600)

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
        incBtn_hot.place(x=250, y=600)
        decBtn_hot.pack()
        decBtn_hot.place(x=300, y=600)

        hot_edits = tk.Text(employee, width=50, height=1.5)
        hot_edits.insert("1.0", "Modifications:")
        hot_edits.pack()
        hot_edits.place(x=400, y=600)

        def complete_order():
            total_cost=0
            total_points= 0
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

            Main.inventory_remove((int(turkeyclub_label["text"])), (int(toast_label["text"])), (int(salad_label["text"])), (int(water_label["text"])), (int(iced_label["text"])), (int(hot_label["text"])));
            final_cost_label = tk.Label(employee, text="Total Cost: $" + str(total_cost), font=subheading_font, bg="light blue")
            final_cost_label.pack()
            final_cost_label.place(x=800, y=700)
            earned_points_label = tk.Label(employee, text="Total Points Earned from Order: " + str(total_points) + " points", font=subheading_font, bg="light blue")
            earned_points_label.pack()
            earned_points_label.place(x=800, y=750)


        complete_order_btn = tk.Button(employee, text="Complete Order!", command=complete_order, bg="light blue")
        complete_order_btn.pack()
        complete_order_btn.place(x=650, y=700)


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
        label2 = tk.Label(customer, text="Cat Adoption Information", font=heading_font, foreground="white", bg="light blue")
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
    employeeBtn = tk.Button(window1, text="Employee", command=employee, bg="light blue")
    exitBtn = tk.Button(window1, text="Exit", command=exit, bg="light blue")

    employeeBtn.pack()
    employeeBtn.place(x=670,y=100)
    customerBtn.pack()
    customerBtn.place(x=670,y=200)
    exitBtn.pack()
    exitBtn.place(x=670, y=750)

    window1.mainloop()


create_window1()