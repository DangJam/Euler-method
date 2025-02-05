import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Initialize global variables
delta_x = 1
x = 0
y = 0
steps = 10  # Default steps
slope_function_str = "x"  # Default function for slope

# Initialize dictionary
xy_dict = {x: y}


# Define the slope function (evaluates the function dynamically)
def slope_function(x, y):
    try:
        # Dynamically evaluate the slope function entered by the user
        return eval(slope_function_str)
    except Exception as e:
        messagebox.showerror("Error", f"Error in function: {e}")
        return 0


# Euler's method calculation
def euler_method():
    global x, y, delta_x, steps
    # Perform the Euler method for the specified number of steps
    for _ in range(steps):
        slope = slope_function(x, y)
        x += delta_x
        y = y + slope * delta_x
        xy_dict.update({x: y})

    # Update the output label to show the latest x, y values
    output_label.config(text=f"Current x: {x}, y: {y}")
    update_table()


# Function to update the parameters from the GUI
def update_parameters():
    global delta_x, x, y, steps, slope_function_str
    try:
        delta_x = float(delta_x_entry.get())
        x = float(x_entry.get())
        y = float(y_entry.get())
        steps = int(steps_entry.get())  # Get the number of steps as an integer
        slope_function_str = slope_function_entry.get()  # Get the function as a string
        # Reinitialize the dictionary with the new values
        xy_dict.clear()
        xy_dict[x] = y
        output_label.config(text=f"Current x: {x}, y: {y}")
        update_table()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")
    except Exception as e:
        messagebox.showerror("Function Error", f"Invalid function expression: {e}")


# Function to update the table with xy_dict values
def update_table():
    # Clear existing table entries
    for row in treeview.get_children():
        treeview.delete(row)

    # Insert new rows from xy_dict
    for key, value in xy_dict.items():
        treeview.insert("", "end", values=(key, value))


# Initialize the Tkinter window
root = tk.Tk()
root.title("Euler's Method Configuration")

# Set the size of the window (width x height)
window_width = 400
window_height = 400

# Set the window's geometry (width x height)
root.geometry(f"{window_width}x{window_height}")

# Define the widgets
tk.Label(root, text="Delta x:").grid(row=0, column=0)
delta_x_entry = tk.Entry(root)
delta_x_entry.grid(row=0, column=1)
delta_x_entry.insert(tk.END, str(delta_x))  # Set default value

tk.Label(root, text="Initial x:").grid(row=1, column=0)
x_entry = tk.Entry(root)
x_entry.grid(row=1, column=1)
x_entry.insert(tk.END, str(x))  # Set default value

tk.Label(root, text="Initial y:").grid(row=2, column=0)
y_entry = tk.Entry(root)
y_entry.grid(row=2, column=1)
y_entry.insert(tk.END, str(y))  # Set default value

tk.Label(root, text="Steps:").grid(row=3, column=0)
steps_entry = tk.Entry(root)
steps_entry.grid(row=3, column=1)
steps_entry.insert(tk.END, str(steps))  # Set default value

# Add a new label and entry for the slope function
tk.Label(root, text="Slope Function:").grid(row=4, column=0)
slope_function_entry = tk.Entry(root)
slope_function_entry.grid(row=4, column=1)
slope_function_entry.insert(tk.END, slope_function_str)  # Default function

# Button to update parameters
update_button = tk.Button(root, text="Update Parameters", command=update_parameters)
update_button.grid(row=5, column=0, columnspan=2)

# Button to run the Euler method
euler_button = tk.Button(root, text="Run Euler's Method", command=euler_method)
euler_button.grid(row=6, column=0, columnspan=2)

# Output label to display the current x and y
output_label = tk.Label(root, text=f"Current x: {x}, y: {y}")
output_label.grid(row=7, column=0, columnspan=2)

# Treeview widget for displaying the xy_dict as a table
treeview = ttk.Treeview(root, columns=("x", "y"), show="headings")
treeview.heading("x", text="x")
treeview.heading("y", text="y")
treeview.grid(row=8, column=0, columnspan=2)

# Initialize the table with the current values in xy_dict
update_table()

# Run the Tkinter event loop
root.mainloop()
