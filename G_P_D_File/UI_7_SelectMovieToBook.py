 

from tkinter import *
from tkinter import ttk
from Cinema import Cinema
import Show
from datetime import datetime
from _7_SelectMovieToBook import *
from User import User
from UI_8_CreateBooking import *

#This took years. Please forgive me for my sins

_user = None
_master = None

def Close(master):
    master.destroy()

def Check_If_TimePassed(time, date):
    time = datetime.datetime.strptime(str(date) + " " + str(time), "%Y-%m-%d %H:%M:%S")
    #print(datetime.datetime.now(), "Time:", time)
    #time = datetime.datetime.strptime(time, "%H:%M:%S")
    
    if(datetime.datetime.now() < time):
        return False
    else:
        return True
    

def Select_and_Book(show):
    #print(_user)
    if(_user != None and _master != None):
        _master.destroy()
        Booking_Form(show, _user)
    else:
        print("Error in global variables...")

def assemble_showbutton(frame, show):
    var = StringVar()

    start_time = datetime.datetime.strptime(str(show.Time), "%H:%M:%S")
    start_time = start_time.strftime("%H:%M")
    
    show_time = str(start_time) + "\nLW: " + str(show.LH_booked) +" \nUH: " + str(show.UH_booked) +" \nVIP: " + str(show.VIP_booked)
    var.set(show_time)
    if((show.LH_booked + show.UH_booked + show.VIP_booked) <= 0 or Check_If_TimePassed(show.Time, show.Date)):
        return Button(frame, textvariable=var, width=10, height=5, state=DISABLED)
    else:
        return Button(frame, textvariable=var, width=10, height=5, command=lambda: Select_and_Book(show))
 
def movieDetails_row(top, group):
    header = str(group[0][2]) + "  |  " + str(group[0][1])
    frame = LabelFrame(top, text=header)

    var = StringVar()
    var.set("Publisher:")
    label_publisher = Label(frame, textvariable=var)
    label_publisher.grid(column=0, row=0, sticky=W)

    var = StringVar()
    var.set(group[0][7])
    publisher = Label(frame, textvariable=var)
    publisher.grid(column=1, row=0, sticky=W)

    var = StringVar()
    var.set("Duration:")
    label_rating = Label(frame, textvariable=var)
    label_rating.grid(column=0, row=1, sticky=W)
 
    var = StringVar()
    duration = str(group[0][3]) #datetime.strptime(str(group[0][3]), "%H:%M")
    duration = datetime.datetime.strptime(duration, "%H:%M:%S")
    var.set(str(duration.hour) + ":" + str(duration.minute))
    label_duration = Label(frame, textvariable=var)
    label_duration.grid(column=1, row=1, sticky=W)
 
    var = StringVar()
    var.set("Age rating:")
    label_age = Label(frame, textvariable=var)
    label_age.grid(column=0, row=2, sticky=W)
    
    var = StringVar()
    var.set(group[0][6])
    label_age_rating = Label(frame, textvariable=var)
    label_age_rating.grid(column=1, row=2, sticky=W)
 
    var = StringVar()
    var.set(group[0][8])
    genres = Label(frame, textvariable=var)
    genres.grid(column=0, columnspan=2, row=3, sticky=W)

    for i in range(1, len(group)):
        show_button = assemble_showbutton(frame, group[i])
        show_button.grid(column=2 + i, row=0, rowspan=4, sticky=E, padx=5, pady=5)
    
    frame.columnconfigure(0, minsize=100)
    frame.columnconfigure(1, weight=1, minsize=50)
    
    return frame

def draw_shows(shows_grouped, date):
    master = Toplevel()
    master.title('Creating a Booking')
    global _master
    _master = master
    #top.geometry("550x600")
    _master.resizable(0, 0)
    _master.columnconfigure(0, weight=1)

    mainframe = Frame(master=_master)

    mainframe.grid(column=0, row=0, sticky=NSEW)

    mainframe.grid_columnconfigure(0, weight=1)

    canvasframe = Frame(master=mainframe)
    canvasframe.grid(column=0, row=2, columnspan=10)
    canvasframe.grid_propagate(FALSE)
    
    can = Canvas(master=canvasframe)
    can.grid(column=0, row=0)
    
    sb = Scrollbar(canvasframe, command=can.yview, orient=VERTICAL)
    sb.grid(column=2, row=0, sticky=NS)
    can.configure(yscrollcommand=sb.set)
    
    parentframe = Frame(master=can)
    # parentframe.grid(column=0, row=0)
    can.create_window((0,0),window=parentframe, anchor=NW)
    
    headerframe = Frame(master=mainframe)
    headerframe.grid(column=0, row=0, sticky=NSEW)
    headerframe.grid_columnconfigure(2, weight=1)
    headerframe.grid_propagate()
    var = StringVar()
    var.set("Exit")
    Backbutton = Button(headerframe, textvariable=var, width=10, height=2, command=lambda: Close(master))
    Backbutton.grid(column=0, row=0, rowspan=2, sticky=W)

    var = StringVar()
    var.set(datetime.datetime.now().strftime("%Y/%m/%d"))
    date_now = Label(headerframe, textvariable=var)
    date_now.grid(column=1, row=0, sticky=W)
    
    var = StringVar()
    #timenow = timenow.
    var.set(datetime.datetime.now().strftime("%H:%M"))
    time_now = Label(headerframe, textvariable=var)
    time_now.grid(column=1, row=1, sticky=W)

    var = StringVar()
    var.set(str(_user.Location))
    cinemaname = Label(headerframe, textvariable=var)
    cinemaname.grid(column=2,  row=0, sticky=E)
    
    var = StringVar()
    var.set(str(_user.Username) + "  [" + str(_user.Type) + "]")
    name_role = Label(headerframe, textvariable=var)
    name_role.grid(column=2, row=1, sticky=E)
    
    if(len(shows_grouped) != 0):
        for i in range(0, len(shows_grouped)):
            #print(shows[i].__str__())
            #frame_child = movieDetails_row(parentframe, "Movie name that is really really long: " + str(i), "18:00", show1_seats)
            frame_child = movieDetails_row(parentframe, shows_grouped[i])
            frame_child.grid(column=0, row=i+2, pady=3, sticky=EW)
            
            frame_child.update()
            #print("Wifo:", frame_child.winfo_width())

            min_size = max(0, 500 - frame_child.winfo_width())
            #print("Min size:", min_size)

            frame_child.grid_columnconfigure(1, minsize=min_size, weight=1)
    else:
        var = StringVar()
        var.set("No Shows found...")
        name_role = Label(mainframe, textvariable=var)
        name_role.grid(column=0, columnspan=5, row=0, rowspan=10, sticky=EW)

    parentframe.update_idletasks()
    
    footerframe = Frame(master=mainframe)
    footerframe.grid(column=0, row=3, sticky='SEW')
    footerframe.grid_columnconfigure(1, weight=1)

    var = StringVar()
    var.set("<- Previous Day")
    prev_day = Button(footerframe, textvariable=var, height=2, command=lambda: PrevDay(_master, date))
    prev_day.grid(column=0, row=0, sticky=W)

    var = StringVar()
    var.set(str(date))
    day_selected = Label(footerframe, textvariable=var)
    day_selected.grid(column=1, row=0)

    var = StringVar()
    var.set("Next Day ->")
    next_day = Button(footerframe, textvariable=var, height=2, command=lambda: NextDay(_master, date))
    next_day.grid(column=2, row=0, sticky=E)

    #print("Mainframe !!!: ", parentframe.winfo_width())

    canvasframe.configure(width=parentframe.winfo_width()+100, height=500)
    
    width = 500
    _master.geometry(str(width) + "x600")
    can.configure(scrollregion=can.bbox("all"), width=width, height=500)
    
    
    if(parentframe.winfo_width()+40 < 300):
        _master.geometry(str(width) + "x600")
        can.configure(scrollregion=can.bbox("all"), width=width, height=500)

    else:
        _master.geometry(str(parentframe.winfo_width()+40) + "x" + "600")
        #print(parentframe.winfo_width())
        can.configure(scrollregion=can.bbox("all"), width=parentframe.winfo_width(), height=500)
    
    headerframe.configure(width=mainframe.winfo_width())

    _master.mainloop()


def Check_If_TimeToofar(date):
    #time = datetime.datetime.strptime(str(date) + " " + str(time), "%Y-%m-%d %H:%M:%S")
    #print(datetime.datetime.now(), "Time:", date)
    if(datetime.datetime.now().date() + datetime.timedelta(days=7) <= date):
        messagebox.showinfo("Failed", "Can't book more than a week in a advance")
        return False
    return True

def Check_If_DatePast(current_time):
    if current_time <= datetime.datetime.now().date():
        messagebox.showinfo("Failed", "Can't book for past dates")
        return False
    return True

def NextDay(root, date):
    if(not Check_If_TimeToofar(date)):
        return
    con = dbConnection.get_connection()
    c = con.cursor()
    root.destroy()
    print(date)
    date += datetime.timedelta(days=1)
    shows_grouped = Generate_List(c, _user.Cinema_ID, show_date=date)
    draw_shows(shows_grouped, date)
    con.close()

def PrevDay(root, date):
    if(not Check_If_DatePast(date)):
        return 
    con = dbConnection.get_connection()
    c = con.cursor()
    root.destroy()
    date -= datetime.timedelta(days=1)
    shows_grouped = Generate_List(c, _user.Cinema_ID, show_date=date)
    draw_shows(shows_grouped, date)
    con.close()

def Innit(user):
    con = dbConnection.get_connection()
    c = con.cursor()
    global _user
    _user = user
    s_d = datetime.datetime.now().date()
    #print(s_d)
    shows_grouped = Generate_List(c, user.Cinema_ID, show_date=s_d)
    draw_shows(shows_grouped, s_d)
    con.close()
"""
con = dbConnection.get_connection()
c = con.cursor()

user = User(0, 0, "Username LastName", "Bristol", "Type")

Innit(c, user)
"""