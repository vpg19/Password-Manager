from tkinter import * 
from tkinter import messagebox
import pyperclip
import json
#----------------------------- SEARCH PASSWORD -----------------------------------#
def search():
    website = webin.get()
    email = emailin.get()
    try:
        with open('Code\\Password Manager\\data.json') as data_file:
                data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Error',message='No data file found!')
    else:
        if len(website) == 0 or len(email) == 0:
            messagebox.showerror(title='Error',message='Please do not leave any fields empty!')
        else:
            try:
                passw = data[website]['password']
            except KeyError:
                messagebox.showerror(title = 'Error',message = f"No details for the website, '{website}', exists")
            else:
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {passw}\nPassword has been copied to clipboard!")
                pyperclip.copy(passw)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    passin.delete(0,END)
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    a = []
    for i in range(0,3):
        a.extend(random.choice(letters))
        a.extend(random.choice(numbers))
        a.extend(random.choice(symbols))
    random.shuffle(a)
    passw = ''.join(a)
    passin.insert(0,passw)
    pyperclip.copy(passw)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = webin.get()
    email = emailin.get()
    passw = passin.get()
    new_data = {
        website:{
            'email':email,
            'password':passw
            }
        }
    if len(website) == 0 or len(email) == 0 or len(passw) == 0:
        messagebox.showerror(title='Error',message='Please do not leave any fields empty')
    else:   
        ask = messagebox.askokcancel(title=website,message=f'These are the details you entered \n Email: {email} \n Password: {passw} \n Is it ok?')
        if ask:
            try:
                with open('Code\\Password Manager\\data.json','r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('Code\\Password Manager\\data.json','w') as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                if email == data[website]['email']:
                    messagebox.showwarning(title='Warning',message=f'Website password already exist for the email "{email}"')
                else:
                    data.update(new_data)
                    with open('Code\\Password Manager\\data.json','w') as data_file:
                        json.dump(data,data_file,indent=4)
            # file = open('Code\\Password Manager\\Data.txt','a')
            # file.write(f"{website} | {email} | {passw}\n")
            # file.close()
            finally:
                webin.delete(0,END)
                passin.delete(0,END)
                webin.focus()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
pass_img = PhotoImage(file='Code\\Password Manager\\logo.png')
canvas.create_image(100,100,image=pass_img)
canvas.grid(column=1,row=0)
#Labels
website = Label(text='Website:')
website.grid(column=0,row=1)
email = Label(text='Email/Username:')
email.grid(column=0,row=2)
passw = Label(text='Password:')
passw.grid(column=0,row=3)
#Entry
webin = Entry(width=33)
webin.focus()
webin.grid(column=1,row=1,columnspan=1)
emailin = Entry(width=51)
emailin.insert(0,'vpgjpr@gmail.com')
emailin.grid(column=1,row=2,columnspan=2)
passin = Entry(width=33)
passin.grid(column=1,row=3)
#Button
genbutt = Button(text='Generate Password',width=14,command=generate)
genbutt.grid(column=2,row=3) 
addbutt = Button(text='Add',width=43,command= save)
addbutt.grid(column=1,row=4,columnspan=2)
searchbutt = Button(text='Search',width=14,command=search)
searchbutt.grid(column=2,row=1)
window.mainloop()