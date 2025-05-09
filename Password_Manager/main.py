from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# (To be implemented)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# (To be implemented)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


website_label = Label(window, text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(window, width=35)
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()


email_label = Label(window, text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(window, width=35)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)


password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(window, width=25)
password_entry.grid(row=3, column=1, pady=5)

generate_button = Button(window, width=7, text="Generate")
generate_button.grid(row=3, column=2)


add_button = Button(window, width=36, text="Add")
add_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
