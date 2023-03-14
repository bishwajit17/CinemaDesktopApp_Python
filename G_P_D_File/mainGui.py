
from tkinter import *
from tkinter import ttk , messagebox
import movieGUI
import cinemaGui
import dbConnection
import showGUI
import AdminReport
import LogOut
# import LoginUser
from User import User
import UI_4_5_6_ManageBooking
from selectCimenaAdminGUI import selectCinema
def omg(user,root):
    root.destroy()
    MainPage = Tk()
    MainPage.title("Main Page")
    MainPage.geometry('490x400')

    MainPage.resizable(0,0)
    # print(username)
    # con = connectionDatabase.get_connection()
    # c = con.cursor()
    # query = 'SELECT cinema_id FROM users where user_name = %s;'
    # # query = 'SELECT c.cinema_name, u.user_id FROM users u FULL JOIN cinemas c ON u.cinema_id = c.cinema_id  WHERE u.user_name IS %s'
    # c.execute(query, (username,))
    # records = c.fetchone()
    # print(records)
    # print(records[0])
    # q = 'SELECT cinema_name FROM cinemas where cinema_id =%s;'
    # c.execute(q,(records[0],))
    # record = c.fetchone()
    # print(record)
    

    # userlabel =  Label(MainPage, text=username)
    # userlabel.grid(row=0, column=0)
    # cinemalabel = Label(MainPage, text=record[0])
    # cinemalabel.grid(row=1, column=0)


    if user.Type == 'Staff':
        frame_button = LabelFrame(MainPage, text='Main Menu')
        frame_button.pack(fill='x', expand='yes', padx=60)
        userlabel =  Label(frame_button, text= user.Username +'[ '+ user.Type +" ]", font=("Helvetica", 15))
        userlabel.grid(row=0, column=0,sticky=E)
        cinemalabel = Label(frame_button, text=user.Location, font=("Helvetica", 15))
        cinemalabel.grid(row=1, column=0,sticky=E)
        logOut_button = Button(frame_button,text='LOG OUT', command=lambda: LogOut.logOut(MainPage), width=15 )
        logOut_button.grid(row=2, column=0, padx=100, pady=10, sticky=NS)
        booking_button = Button(frame_button,text='BOOKING MOVIES', command=lambda: UI_4_5_6_ManageBooking.RetrieveBooking(user), width=15)
        booking_button.grid(row=3, column=0, padx=100, pady=10, sticky=NS)

    if user.Type == 'Admin':
        frame_button = LabelFrame(MainPage, text='Main Menu')
        frame_button.pack(fill='x', expand='yes', padx=60)
        userlabel =  Label(frame_button, text=user.Username +' [ '+ user.Type +" ]", font=("Helvetica", 15))
        userlabel.grid(row=0, column=0,sticky=E)
        cinemalabel = Label(frame_button, text=user.Location ,font=("Helvetica", 15))
        cinemalabel.grid(row=1, column=0,sticky=E)
        logOut_button = Button(frame_button,text='LOG OUT',command=lambda: LogOut.logOut(MainPage), width=15)
        logOut_button.grid(row=2, column=0, padx=100, pady=10, sticky=NS)
        booking_button = Button(frame_button,text='BOOKING MOVIES', command=lambda: selectCinema(user), width=15)
        booking_button.grid(row=3, column=0, padx=100, pady=10, sticky=NS)
        movies_button = Button(frame_button,text='MOVIES', command=movieGUI.movie, width=15)
        movies_button.grid(row=4, column=0, padx=100, pady=10, sticky=NS)
        reports_button = Button(frame_button,text='REPORTS', command = AdminReport.adminReports, width=15)
        reports_button.grid(row=5, column=0, padx=100, pady=10, sticky=NS)
        showing_button = Button(frame_button,text='SHOWINGS', command=lambda: showGUI.show(user), width=15)
        showing_button.grid(row=6, column=0, padx=100, pady=10, sticky=NS)
    
    if user.Type == 'Manager':
        frame_button = LabelFrame(MainPage, text='Main Menu')
        frame_button.pack(fill='x', expand='yes', padx=60)
        userlabel =  Label(frame_button, text=user.Username +'[ '+ user.Type +" ]", font=("Helvetica", 15))
        userlabel.grid(row=0, column=0,sticky=E)
        cinemalabel = Label(frame_button, text=user.Location, font=("Helvetica", 15))
        cinemalabel.grid(row=1, column=0,sticky=E)
        logOut_button = Button(frame_button,text='LOG OUT', command=lambda: LogOut.logOut(MainPage), width=15)
        logOut_button.grid(row=2, column=0, padx=100, pady=10, sticky=NS)
        booking_button = Button(frame_button,text='BOOKING MOVIES',command=lambda: UI_4_5_6_ManageBooking.RetrieveBooking(user), width=15)
        booking_button.grid(row=3, column=0, padx=100, pady=10, sticky=NS)
        movies_button = Button(frame_button,text='MOVIES', command=movieGUI.movie, width=15)
        movies_button.grid(row=4, column=0, padx=100, pady=10, sticky=NS)
        reports_button = Button(frame_button,text='REPORTS', command = AdminReport.adminReports, width=15)
        reports_button.grid(row=5, column=0, padx=100, pady=10, sticky=NS)
        showing_button = Button(frame_button,text='SHOWINGS', command=lambda: showGUI.show(user), width=15)
        showing_button.grid(row=6, column=0, padx=100, pady=10, sticky=NS)
        cinemas_button = Button(frame_button,text='CINEMAS', command=cinemaGui.cinema, width=15)
        cinemas_button.grid(row=7, column=0, padx=100, pady=10, sticky=NS)


    MainPage.mainloop()