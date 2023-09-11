import tkinter as tk

def click_button(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget for displaying the result
entry = tk.Entry(root, width=16, font=('Arial', 20), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Add buttons to the grid
row = 1
col = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 15),
              command=lambda button=button: click_button(button)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text='Clear', padx=20, pady=20, font=('Arial', 15), command=clear_entry).grid(row=row, column=col)

# Equal button
tk.Button(root, text='=', padx=20, pady=20, font=('Arial', 15), command=calculate).grid(row=row, column=col + 1)

# Run the main loop
root.mainloop()
