
from tkinter import *
from tkinter import ttk , messagebox
import dbConnection
import mainGui
from User import User
import hashlib
from Validations import *

class UserAccount():
    
    def __init__(self):
        self.__user_name = ""
        self.__password = ""
    
    def getUser(self):
        return self.__user_name

    def setUser(self, user):
        # if self.validateUsernameSyntax(user):   #validating pattern
        self.__user_name = user
    
    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        # if self.validateUserpasswordSyntax(password):
        self.__password = password
            # return 1
        # else:
        #     return 0
    
    def checkUserNamePassword(un, pw):
        if un == '' or User_Name(un) == False:
            messagebox.showerror("Failed! ", "Invalid Username")
            return

        con = dbConnection.get_connection()
        c = con.cursor()
        query = 'SELECT * FROM users WHERE user_name = %s ;'
        c.execute(query, (un,))
        records = c.fetchone()

        if records == None:
            messagebox.showerror("Failed! ", "Check you UserName and Password its incorrect!")
            return

        k = 'SELECT cinema_name FROM cinemas WHERE cinema_id = %s;'
        c.execute(k,(records[1],))
        location = c.fetchone()

        user = User(user_id= records[0], cinema_id = records[1], username = records[2],location = location[0], staff_type = records[4])
        user.__str__()

        auth = pw.encode()
        auth_hash = hashlib.md5(auth).hexdigest().upper()
        print(auth_hash)
        if(un == records[2] and auth_hash == records[3]):
            return user
        else:
            messagebox.showerror("Failed! ", "Check you UserName and Password its incorrect!")

        
        # print(record)
        # print(record[2])
        # # if sha256_crypt.verity(pw, str(record[3])):
        # for record in records:
        #     # if len(record)  >0:
        #     # print(record[3])
        #     print(record)
        #     return record[4] #record exist
        #     # else:
        #     #     print('record does not exist')
        #     #     return 0    #record does not exist   
        con.close()
    # def fetchallinfo(un, pw):
    #     query = 'SELECT user_type FROM users WHERE user_name = %s and password = %s;'
    #     c.execute(query, (un, pw))
    #     row = c.fetchone()
    #     print(row)
    #     print(row[0])
    #     return row[0]

def loginverify(username, password, root):
        user = UserAccount.checkUserNamePassword(username, password)
        

        if user == None:
            return 
        elif (user.Type=='Admin'):
            return mainGui.omg(user, root)
        elif (user.Type =='Staff'):
            return mainGui.omg(user,root)
        elif (user.Type == 'Manager'):
            return mainGui.omg(user,root)
        else:
            return messagebox.showerror("Failed! ", "Invalid Login")


def frame():
    root=Tk()
    root.title("LogIn Required")
    root.geometry('400x400')
    root.resizable(0,0)

    HorizanCineam = Label(root, text = 'Horizon Cinema',font=("Helvetica", 30))
    HorizanCineam.grid(row=0, column=0, padx=10, pady=20)

    LoginFrame= LabelFrame(root, text='Login')
    LoginFrame.grid(row=1, column=0, padx=40, pady=10)
    # LoginFrame.pack(fill='x', expand='yes', padx=20)

    userName_label = Label(LoginFrame, text="User Name :")
    userName_label.grid(row=0,column=0,padx=10, pady=10)
    userName_entry = Entry(LoginFrame)
    userName_entry.grid(row=0,column=1, padx=10, pady=10)

    password_label = Label(LoginFrame, text="Password :", )
    password_label.grid(row=1,column=0,padx=10, pady=10) 
    password_entry = Entry(LoginFrame,show="*")
    password_entry.grid(row=1,column=1, padx=10, pady=10)

    add_button = Button(LoginFrame,text='Login', command=lambda: 
    loginverify(userName_entry.get(), password_entry.get(),root))
    
    add_button.grid(row=2, column=1, padx=10, pady=10,sticky=E)
    root.mainloop()
        




