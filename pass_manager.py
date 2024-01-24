from tkinter import *
from tkinter import messagebox
from pass_gen import generate_password, password_config
import random

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Something has gone wrong", message="Please make sure you have filled all fields!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the credentials entered: \nEmail: {email}"
                           f"\nPassword: {password}"
                           "\nDo you want to save them? ")
        if is_ok:
            with open('passwords.txt', 'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

def generate_and_set_password():
    no_of_letters = random.randint(8, 10)
    no_of_symbols = random.randint(2, 4)
    no_of_numbers = random.randint(2, 4)

    generated_password = generate_password(no_of_letters, no_of_symbols, no_of_numbers)
    password_entry.config(state='normal')  # Set state to normal to allow changes
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)
    password_entry.config(state='readonly')  # Set state back to readonly
def toggle_password_visibility():
    current_state = password_entry.cget('show')
    password_entry.config(show='' if current_state == '*' else '*')


window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=512, width=512)
canvas.grid(row=0, column=1)

logo_img = PhotoImage(file='E:\\Tech\\Projects\\Python\\password-generator-and-manager\\password-512.png')
canvas.create_image(256, 256, anchor=CENTER, image=logo_img)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

website_entry = Entry(width=50)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=2)
email_entry = Entry(width=50)
email_entry.grid(row=2,column=1,columnspan=2)


password_entry = Entry(width=50, state='readonly')
password_entry.grid(row=3,column=1,columnspan=2)

show_hide_button = Button(window, text="Show/Hide", command=toggle_password_visibility)
show_hide_button.grid(row=3, column=3)

no_of_letters = random.randint (8, 10)
no_of_symbols = random.randint (2, 4)
no_of_numbers = random.randint (2, 4)

generate_password_button = Button(window, text="Generate Password", command=generate_and_set_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=40, command=save)
add_button.grid(row=4, column=1)

window.mainloop()
