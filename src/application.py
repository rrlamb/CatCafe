import tkinter as tk
import random

window1= tk.Tk()
window1.configure(bg="light blue")

window1.geometry("1420x1200")
heading_font=("Arial", 36, "bold")
subheading_font=("Arial", 16)


label1=tk.Label(window1, text="CAT CAFE", font=heading_font, foreground="white", bg= "light blue")
label1.pack()
window1.title("CAT CAFE")

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
    employee.mainloop()


def customer():
    window1.destroy()
    # Customer Window
    customer = tk.Tk()
    customer.configure(bg="light blue")
    customer.geometry("1420x1200")
    # Header saying name of window
    label2 = tk.Label(customer, text="Cat Adoption Information", font=heading_font, foreground="white", bg="light blue")
    label2.pack()
    customer.title("Employee View")
    customer.mainloop()


customerBtn = tk.Button(window1, text="Customer", command=customer, bg="pink")
employeeBtn = tk.Button(window1, text="Employee", command=employee, bg="pink")

employeeBtn.pack()
employeeBtn.place(x=300,y=100)
customerBtn.pack()
customerBtn.place(x=300,y=200)

window1.mainloop()