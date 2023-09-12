import tkinter as tk
from tkinter import messagebox
import smtplib

def send_email():
    sender_email = sender_entry.get()
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password_entry.get())
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Email Sender")

# Create labels and entry widgets
tk.Label(root, text="Sender Email:").pack()
sender_entry = tk.Entry(root, width=50)
sender_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, width=50, show="*")
password_entry.pack()

tk.Label(root, text="Receiver Email:").pack()
receiver_entry = tk.Entry(root, width=50)
receiver_entry.pack()

tk.Label(root, text="Subject:").pack()
subject_entry = tk.Entry(root, width=50)
subject_entry.pack()

tk.Label(root, text="Body:").pack()
body_text = tk.Text(root, height=10, width=50)
body_text.pack()

# Create a button to send the email
send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.pack()

# Start the main loop
root.mainloop()
