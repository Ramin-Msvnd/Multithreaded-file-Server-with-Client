from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import pymysql.cursors
#from dotenv import load_dotenv
import os
from tkinter.messagebox import showinfo
'''connection user, password,db name need modification based on your database'''
#load_dotenv()
#databasePass=os.getenv('databasePass')
databasePass='Fighter@007'
def user_update (name, password, user_type):
    connection = pymysql.connect(host='',user='root',password=databasePass,
                             db='networking_CMPE_207',charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor= connection.cursor()
    command="call user_update(\'%s\', \'%s\', \'%s\');"
    try:
        cursor.execute( command%(name, password, user_type) )
        connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Done!")
    except mysql.connector.IntegrityError as ie: 
        print("user name already exists in the data'base")



def user_delete (name):
    connection = pymysql.connect(host='',user='root',password=databasePass,
                             db='networking_CMPE_207',charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor= connection.cursor()
    command="call user_deletion(\'%s\');"
    cursor.execute( command%(name) )
    connection.commit()
    cursor.close()
    messagebox.showinfo("Success", "Done!")


def clear_user_list():
    connection = pymysql.connect(host='',user='root',password=databasePass,
                             db='networking_CMPE_207',charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    command='call user_list_clear();'
    cursor.execute(command)
    connection.commit()
    cursor.close()


win = Tk()
win.resizable(True,True)
win.title('Admin')
win.geometry("200x200")
win.resizable(False, False)



def openRemove():
    remove = Toplevel(win)
    remove.title('Remove a user')
    remove.geometry("400x100")
    remove.resizable(False,False)

    entry_username = Entry(remove,width = 40)
    entry_username.place(relx = 0.3,rely = 0.05)
    lb_username = Label(remove,text = 'username : ')
    lb_username.place(relx = 0.1,rely = 0.05)

    def userDeletion():
        u=entry_username.get()
        user_delete(u)
        messagebox.showinfo("Success", "Done!")
    def allUsersDeletion():
        clear_user_list()
        messagebox.showinfo("Success", "Done!")
    btn_remove = ttk.Button(remove,text ='Remove User', command=userDeletion )
    btn_remove.place(relx = 0.3,rely = 0.6)
    btn_clear = ttk.Button(remove,text ='Remove All Users', command=allUsersDeletion)
    btn_clear.place(relx = 0.6,rely = 0.6)



    btn_signup = ttk.Button(signup,text = 'Sign up' , command = opensignin) #connecttodb)
    btn_signup.place(relx = 0.5,rely =0.75)


def openUpdate():
    update = Toplevel(win)
    update.title('Add/ Update a user')
    update.geometry("400x300")
    update.resizable(False,False)
    entry_username = Entry(update,width = 40)
    entry_username.place(relx = 0.3,rely = 0.05)
    lb_username = Label(update,text = 'username : ')
    lb_username.place(relx = 0.1,rely = 0.05)
    entry_password = Entry(update,width = 40,show =  '*')
    entry_password.place(relx = 0.3 ,rely = 0.25)
    lb_password = Label(update,text = 'password : ')
    lb_password.place(relx = 0.1 , rely = 0.25)
    Option=StringVar( )
    rb1=Radiobutton(update, text='Regular', variable=Option, value='Regular')
    rb2=Radiobutton(update, text='Super', variable=Option, value='Super')
    rb1.place(relx=0.4, rely=0.55)
    rb2.place(relx=0.6, rely=0.55)
    Option.set('Regular')
    def Add():
        u=entry_username.get()
        p=entry_password.get()
        t=Option.get()
        user_update(u,p,t)
    btn_add = ttk.Button(update,text ='Add/Update', command=Add )
    btn_add.place(relx = 0.4,rely = 0.7)


btn_update = ttk.Button(win,text = 'Add/ Update User',command = openUpdate)
btn_update.place(relx = 0.25,rely = 0.35)


btn_login = ttk.Button(win,text = 'Remove User',command = openRemove)
btn_login.place(relx = 0.3,rely = 0.65)

mainloop() #Very important