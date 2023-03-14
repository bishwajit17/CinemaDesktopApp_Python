# Name: Bishwajit Sonar
# Student Id:- 21063833

from tkinter import *
from tkinter import ttk, messagebox
# import cinemaClass
import dbConnection
from User import User
import UI_4_5_6_ManageBooking
con = dbConnection.get_connection()
c = con.cursor()

def Go_To_Bookings(cinema_id, user, admin):
    user.Cinema_ID = cinema_id
    UI_4_5_6_ManageBooking.RetrieveBooking(user, admin)



def selectCinema(user):

    admin = Tk()
    admin.title("Select Cinemas")
    admin.geometry("500x400")
    admin.resizable(False,False)

        # name = Label(admin, text=user.Username  ,font=("Helvetica", 20))
        # name.pack(anchor=E,padx=10,pady=5)
        # cinemaLocation = Label(admin, text=user.Location  ,font=("Helvetica", 20))
        # cinemaLocation.pack(anchor=E,padx=10,pady=5)

    dataFrame = LabelFrame(admin, text='Select Cinema')
    dataFrame.pack(fill='both', expand='yes', padx=20, ipadx=20, ipady=20)


    mainFrame = Frame(dataFrame)
    mainFrame.pack(fill=BOTH, expand=1)

    myCanvas = Canvas(mainFrame)
    myCanvas.pack(side=LEFT, fill=BOTH, expand=1)

    myScrollBar = ttk.Scrollbar(mainFrame,orient=VERTICAL, command=myCanvas.yview)
    myScrollBar.pack(side=RIGHT, fill=Y)

    myCanvas.configure(yscrollcommand=myScrollBar.set)
    myCanvas.bind('<Configure>', lambda e:myCanvas.configure(scrollregion=myCanvas.bbox("all")))

    secondFrame = Frame(myCanvas)
    myCanvas.create_window((0,0), window=secondFrame, anchor="nw")

    query = 'SELECT cinema_id, cinema_name FROM cinemas;'
    c.execute(query)
    records = c.fetchall()
    print(records)
    print(records[0])

    def bton(rec):

        #return Button(secondFrame, text = rec[1], command=lambda: UI_4_5_6_ManageBooking.RetrieveBooking(rec[0], user))
        return Button(secondFrame, text = rec[1], command=lambda: Go_To_Bookings(rec[0], user, admin))

    for record in records:
        button = bton(record)
        button.pack(anchor=CENTER, padx=150, pady=5, ipadx=10, ipady=10)
        print(record[0])
        print("hello")
        button.update()

    admin.mainloop()
