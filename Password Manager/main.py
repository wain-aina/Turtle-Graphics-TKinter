from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for l in range(randint(8, 10))]
    password_symbols = [choice(symbols) for s in range(randint(2,4))]
    password_numbers = [choice(numbers) for n in range(randint(2,4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_place = web_entry.get()
    person = user_entry.get()
    pin = pass_entry.get()

    new_data = {
        web_place: {
            "email": person,
            "password":pin,
         }
    }

    if len(web_place) == 0 or len(pin) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=web_place,
                               message=f"These are the details entered: \nEmail: {person}\nPassword: {pin}"
                                       f"Is it ok to save?")

        if is_ok:
            try:
                with open("password.json", 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("password.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("password.json", "a") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_entry.delete(0, END)
                pass_entry.send(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_entry.get()
    try:
        with open("password.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#Labels
website = Label(text="Website: ")
website.grid(row=1, column=0)

user = Label(text="Email/Username: ")
user.grid(row=2, column=0)

password = Label(text="Password: ")
password.grid(row=3, column=0)

#Entries
web_entry = Entry(width=33)
web_entry.grid(row=1, column=1)
web_entry.focus()

user_entry = Entry(width=43)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(END, "snowflakeske@gmail.com")

pass_entry = Entry(width=33)
pass_entry.grid(row=3, column=1)

#Buttons
gen = Button(text='Generate',command=generate_password)
gen.grid(row=3, column=2)

add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)

search = Button(text="Search: ", command=find_password)
search.grid(row=1,column=2)

window.mainloop()