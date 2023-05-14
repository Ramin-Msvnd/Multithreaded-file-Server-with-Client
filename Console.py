from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import socket
from tkinter import ttk
from tkinter.messagebox import askyesno
def console(isSuper, window):
    IP = socket.gethostbyname(socket.gethostname())
    PORT = 4456
    ADDR = (IP, PORT)
    FORMAT = "utf-8"
    SIZE = 1024
    global connectionStatus
    global client
    connectionStatus=False
    
    win = Tk()
    win.resizable(True,True)
    win.title('File Management')
    win.geometry("400x400")
    win.resizable(False, False)
                    
    def sendListRequest():
        client.send("LIST".encode(FORMAT))
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@")  
        return (cmd,msg)
    
    
    
    
    
    
    def CONNECT():
    
        global connectionStatus    
        if connectionStatus==False:
                global client
                client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(ADDR)
                data = client.recv(SIZE).decode(FORMAT)
                connectionStatus=TRUE
    
    
    
    def LOGOUT():
        global connectionStatus
        if connectionStatus==TRUE:
            client.send("LOGOUT".encode(FORMAT))
          #      break
            #print("Disconnected from the server.")
            client.close()
            connectionStatus=FALSE
    
    def LIST():
        #client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #client.connect(ADDR)    
        
        cmd, msg = sendListRequest()
        #print(msg)
        global FileList
        FileList=msg.split('\n')
        listbox = Listbox(win) 
        x=.6
        y=.4
        varTitle=StringVar()
        labelTitle=Label(win, textvariable=varTitle)
        varTitle.set("Server Files\n__________")
        labelTitle.place(relx=x, rely=(y))
        #global varNames
        for i,v in enumerate(FileList):
            listbox.insert(i,v)
        listbox.place(relx=x-.1, rely=(y+.1))
        
    
        
    def openDelete(FileList):
        delWin = Toplevel(win)
        delWin.title('File Removal')
        delWin.geometry("400x300")
        delWin.resizable(False,False)    
        cb=ttk.Combobox(delWin, values=(FileList)) 
        cb.place(relx = 0.3,rely = 0.05)
        cb.config(state='readonly')
        def confirmRemoval(fN):
            answer = askyesno(title='confirmation', message=f'Are you sure that you want to delete the file {fN}?')
            #print(fN)
            if answer:
             
                 #print(fN)
           
                 cmd="DELETE"
                 client.send(f"{cmd}@{fN}".encode(FORMAT))
                 bull = client.recv(SIZE).decode(FORMAT)
                 LIST()
       
        
        btn_delete = ttk.Button(delWin,text = 'Delete File',command = lambda: confirmRemoval(fN))
        btn_delete.place(relx = .4,rely = 0.15)
        def callbackFunc(event):
            global fN
            
            fN = event.widget.get()
            btn_delete.configure(command= lambda: confirmRemoval(fN))
            #print(fN)
        cb.bind("<<ComboboxSelected>>", callbackFunc)    
       
    
    
    
    def UPLOAD():
        cmd='UPLOAD'
        filePath=askopenfilename(filetypes= (("Text File", "*.txt"), ("All Files", "*.*")))
        ##print(filePath)
        
        with open(filePath, "r") as f:
            text = f.read()
    
        filename = filePath.split("/")[-1]
        send_data = f"{cmd}@{filename}@{text}"
        client.send(send_data.encode(FORMAT))
        bull = client.recv(SIZE).decode(FORMAT)
        LIST()
        
    
        
    x=0.1
    global FileList
    btn_login = ttk.Button(win,text = 'File Removal',command = lambda: openDelete(sendListRequest()[1]))
    if isSuper:
        btn_login.place(relx = x,rely = 0.15)
    
    btn_login = ttk.Button(win,text = 'File Upload',command = UPLOAD)
    btn_login.place(relx = x,rely = 0.35)
    
    btn_login = ttk.Button(win,text = 'Connect',command = CONNECT)
    btn_login.place(relx = x,rely = 0.50)
    
    
    btn_login = ttk.Button(win,text = 'File List',command = LIST)
    btn_login.place(relx = x,rely = 0.65)
    
    btn_logout = ttk.Button(win,text = 'Log Out',command = LOGOUT)
    btn_logout.place(relx = x,rely = 0.8)
    #window.destroy()
    mainloop()    

