import tkinter as tk

# Underweight: BMI less than 18.5
# Normal weight: BMI between 18.5 and 24.9
# Overweight: BMI between 25 and 29.9
# Obese: BMI of 30 or higher

def calculate_bmi():
    height = float(height_entry.get()) / 100
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    result_label.config(text=f"BMI: {bmi:.2f}", font=("Helvetica", 16, "bold"), fg="#007BFF")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")

# Create labels and entry widgets with some padding
tk.Label(root, text="Height (cm):", font=("Helvetica", 12)).pack(pady=5)
height_entry = tk.Entry(root, font=("Helvetica", 12))
height_entry.pack(pady=5)

tk.Label(root, text="Weight (kg):", font=("Helvetica", 12)).pack(pady=5)
weight_entry = tk.Entry(root, font=("Helvetica", 12))
weight_entry.pack(pady=5)

# Create a button to calculate BMI with some styling
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, font=("Helvetica", 12), bg="#28A745", fg="#FFFFFF")
calculate_button.pack(pady=10)

# Create a label to display the result with styling
result_label = tk.Label(root, font=("Helvetica", 14, "bold"))
result_label.pack()

# Start the main loop
root.mainloop()
