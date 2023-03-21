from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import pymysql.cursors
import os
from dotenv import load_dotenv
from Console import console

load_dotenv()
databasePass=os.getenv('databasePass')


def auth(username, password, user_type):
    
    connection = pymysql.connect(host='',user='root',password=databasePass,
                             db='networking_CMPE_207',charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    '''connection user, password,db name need modification based on your database'''
    try:
        with connection.cursor() as cursor:

            command = "call get_pass(\'%s\', \'%s\', \'%s\')"
            cursor.execute(command%(username, password, user_type) )
            result = cursor.fetchone()

            return(result['count(user_name)'])
    except Exception:
        pass
    finally:
        connection.close()

def Login():
    login = Tk()
    login.title('Login')
    login.geometry("400x300")
    login.resizable(False,False)
    entry_username = Entry(login,width = 40)
    entry_username.place(relx = 0.3,rely = 0.05)
    lb_username = Label(login,text = 'username : ')
    lb_username.place(relx = 0.1,rely = 0.05)
    entry_password = Entry(login,width = 40,show =  '*')
    entry_password.place(relx = 0.3 ,rely = 0.25)
    lb_password = Label(login,text = 'password : ')
    lb_password.place(relx = 0.1 , rely = 0.25)
    Option=StringVar( )
    rb1=Radiobutton(login, text='Regular', variable=Option, value='Regular')
    rb2=Radiobutton(login, text='Super', variable=Option, value='Super')
    rb1.place(relx=0.4, rely=0.55)
    rb2.place(relx=0.6, rely=0.55)
    Option.set('Regular')
    def check():
        u=entry_username.get()#username field
        p=entry_password.get()#password field
        t=Option.get()
        isAuthenticated=bool(auth(u,p,t))
        isSuper = t == 'Super'
        if isAuthenticated:
            login.destroy()
            console( isSuper, login)

        else:
            messagebox.showerror('Error', 'Error: Incorrect Username or Password!')

    btn_add = ttk.Button(login,text ='Login', command=check )
    btn_add.place(relx = 0.4,rely = 0.7)
    mainloop()


Login()