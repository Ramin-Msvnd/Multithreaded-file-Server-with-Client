This is Multi-threaded server. The Client is using TkInter as the GUI and is connected to MYSQL.
It has different types of users with different privileges. Users must sign in to manipulate files. Super users can upload or remove files, the regular users can not remove file, they can only upload.
To add handle add, update or remove users use the Admin.py file.

How to use the App?

You need to have MySQL on your system

Install the requirements using pip, virtual env is recommended

SQL Script should be used to create the schema, copy and past it to build the schema and tables

There must be a directory called server_data that contains the files to share as there is in the repo 

The server should Run by command "python run server" CMD or terminal

create a file named ".env", paste the line below there and replace YourPassword with your database password 
databasePass=YourPassword

Admin.py is used to add,update, and remove users, run it by python Admin.py on CLI show the GUI, then add/remove users (Super users can upload and remove files, but regular users can only upload)

The Client must run "python Client.py" for clients to sign into their portal

After entering the portal, the client must press connect to get connected to the server
and press Logout to disconnect from the server