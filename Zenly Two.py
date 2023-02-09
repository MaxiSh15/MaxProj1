from tkinter import *
from tkinter import messagebox
import tkinter as tk
import pickle
import os

password = []
login = []


def voitybutton():
    root.destroy()


def regis_login():
    log = UserName_Entry.get()
    passw = User_password.get()

    if log in login:
        messagebox.showerror('Упс!', "Пользователь с таким именем существует!")

    elif not passw and not log:
        messagebox.showerror('Внимание!', """Вы не можете продолжить пока 
не введёте свои данные!""")
    elif not log:
        messagebox.showwarning("Внимание!", ' Введите ваш логин пожалуйста!')
    elif not passw:
        messagebox.showwarning('Внимание!', 'Введите пожалуйста свой пароль!')

    else:
        password.append(passw)
        login.append(log)
        messagebox.showinfo('Поздравляем!', "Регистрация прошла успешно!")

        with open("password_save.pkl", "wb") as f:
            pickle.dump(password, f)
        with open("login_save.pkl", "wb") as f:
            pickle.dump(login, f)

        root.destroy()

    print(password, login)


root = tk.Tk()
root.title('Zenly Registration')
root.geometry('300x300')
root.resizable(False, False)
root.configure(bg='grey')
root.iconbitmap('D:\PyProj\Zenlytwo\ZenlyTwoico.ico')

Hi_Text = Label(root, text='Добро Пожаловать!', bg='grey',
                fg='white', font=('Arial Black', 20)).grid()

Text = Label(root, text='Введите ваш логин', bg='grey',
             fg='white').grid()

UserName_Entry = Entry(root,)
UserName_Entry.grid(pady=10)
Text = Label(root, text='Введите ваш Пароль', bg='grey',
             fg='white').grid()
User_password = Entry(root)
User_password.grid()

Button(root, text='Зарегистрироваться', command=regis_login).grid(pady=10)
Button(root, text='войти', command=voitybutton).grid(sticky=S)

root.mainloop()


with open("password_save.pkl", "rb") as f:
    user_password_saved = pickle.load(f)

with open("login_save.pkl", "rb") as f:
    user_login_saved = pickle.load(f)


inpu = tk.Tk()
inpu.title('Zenly Registration')
inpu.geometry('300x300')
inpu.resizable(False, False)
inpu.configure(bg='grey')
inpu.iconbitmap('D:\PyProj\Zenlytwo\ZenlyTwoico.ico')


def login_pass_check():
    password_check = User_pass.get()
    login_check = UserName.get()

    if not password_check and not login_check:
        messagebox.showerror('Внимание!', """Вы не можете продолжить пока 
не введёте свои данные!""")

    elif not password_check:
        messagebox.showwarning('Внимание!', 'Введите пожалуйста свой пароль!')

    elif not login_check:
        messagebox.showwarning("Внимание!", ' Введите ваш логин пожалуйста!')

    elif password_check in user_password_saved and login_check in user_login_saved:
        os.startfile("ZenlyTwo\ZenlyTwoMap.py")

    elif password_check not in password:
        messagebox.showerror('Упс!', "Неверный пароль!")

    elif login_check not in login:
        messagebox.showerror('Упс!', 'Неверный логин')

    else:
        messagebox.showerror('TECHNICAL ERROR', 'EROR ')


Label(inpu, text='ZenlyTwo', bg='grey', fg='yellow',
      font=('Arial Black', 20)).grid(padx=80)

Label(inpu, text='Введите ваш логин', bg='grey', fg='white').grid()

UserName = Entry(inpu)
UserName.grid(pady=10)
Label(inpu, text='Введите ваш Пароль', bg='grey',
      fg='white').grid()
User_pass = Entry(inpu)
User_pass.grid()

vhodbut = Button(inpu, text='Войти', command=login_pass_check).grid(pady=10)


inpu.mainloop()
