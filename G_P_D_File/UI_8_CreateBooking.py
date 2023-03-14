
from tkinter import *
import dbConnection
from SeatTypes import SeatTypes
from User import User
from Show import Show
from sql_show import *
import UI_7_SelectMovieToBook
import CalSeatsLeft
from Booking import Booking
import CalTotalCost
import UI_9_paymentScreen
from Validations import *
from tkinter import messagebox

def Create_booking(user, show, c, name_var, email_var, phone_var, slider_val, master, Movie_Name):
    if(not Name_LastName(name_var.get())):
        messagebox.showwarning(title="Input Error", message="Name error. Make sure only Letters are used.\n[Firstname Lastname]")
        return
    if(not Email(email_var.get())):
        messagebox.showwarning(title="Input Error", message="Email error. Make sure email follows this format:\n[email@example.com]")
        return
    if(not PhoneNum(phone_var.get())):
        messagebox.showwarning(title="Input Error", message="Phone Number error. Make sure only numbers are used (+ can be used at start only)\n[+123456789]")
        return
    # if((CalSeatsLeft(c, show.ID, booking.Seat_Type)) > slider_val ):
    #     messagebox.showwarning(title="Input Error", message="Phone Number error. Make sure only numbers are used (+ can be used at start only)\n[+123456789]")
    #     return
    print("---------seat left------")
    print(slider_val)
    seatsss = CalSeatsLeft.CalSeatsLeft(c,show.ID)
    print(seatsss[0])
    print(seatsss[1])
    print(seatsss[2])

    if(_selection == "LH"):
        if(seatsss[0]< slider_val.get()):
            messagebox.showwarning(title="Input Error", message="Select Availabel Seats Number!")
            return
    if(_selection == "UH"):
        if(seatsss[1] < slider_val.get()):
            messagebox.showwarning(title="Input Error", message="Select Availabel Seats Number!")
            return

    if(_selection == "VIP"):
        if(seatsss[2]< slider_val.get()):
            messagebox.showwarning(title="Input Error", message="Select Availabel Seats Number!")
            return

    print(seatsss)
    
    
    
    cost = CalTotalCost.CalTotalCost(c, user.Cinema_ID, show.ID, _selection, slider_val.get())
    booking = Booking(show_id=show.ID, cust_details=[name_var.get(), email_var.get(), phone_var.get()], bookings=slider_val.get(), seat_type=_selection)
    booking.Total_Paid = cost
    print("Sent to cal:", user.Cinema_ID, show.ID, booking.Seat_Type, booking.Bookings)
    print("cost:", CalTotalCost.CalTotalCost(c, user.Cinema_ID, show.ID, booking.Seat_Type, booking.Bookings))
    print(booking.__str__())

    master.destroy()
    UI_9_paymentScreen.Draw_PaymentScreen(user, booking, show, Movie_Name)


def Go_Back(master, user):
    master.destroy()
    UI_7_SelectMovieToBook.Innit(user)

_selection = SeatTypes.lower_hall.value

def ChangeSeatType(selection):
    global _selection
    _selection = selection

def Booking_Form(show, user):
    con = dbConnection.get_connection()
    c = con.cursor()

    Movie_Name = GetMovieName(c, show.ID)[1]

    top = Toplevel()
    #top = 
    top.geometry("600x400")
    top.resizable(0, 0)
    top.columnconfigure(0, weight=1)

    mainframe = Frame(master=top)
    mainframe.grid(column=0, row=0, sticky=NSEW)
    mainframe.grid_columnconfigure(0, weight=1)
    mainframe.configure(width=top.winfo_width())


    header = Frame(master=mainframe)
    header.grid(column=0, row=0, columnspan=2, sticky=NSEW)
    
    mainframe.grid_columnconfigure(0, weight=1)
    mainframe.grid_columnconfigure(1, weight=1)

    var = StringVar()
    var.set("Back")
    Backbutton = Button(header, textvariable=var, width=10, height=2, command=lambda: Go_Back(top, user))
    Backbutton.grid(column=0, row=0, rowspan=3)

    var = StringVar()
    var.set("Creating a booking for")
    createbookingfor = Label(header, textvariable=var)
    createbookingfor.grid(column=1,  row=0)

    var = StringVar()
    var.set(str(Movie_Name))
    movie = Label(header, textvariable=var)
    movie.grid(column=1,  row=1)

    var = StringVar()
    #var.set("on 2022-11-20 at 12:00")
    var.set("on " + str(show.Date) + " at " + str(show.Time))
    date_time = Label(header, textvariable=var)
    date_time.grid(column=1,  row=2)

    var = StringVar()
    var.set(user.Location)
    cin_location = Label(header, textvariable=var)
    cin_location.grid(column=2,  row=0, sticky=E)

    var = StringVar()
    var.set(str(user.Username) + "  [" + str(user.Type) + "]")
    user_name = Label(header, textvariable=var)
    user_name.grid(column=2,  row=1, sticky=E)
    
    header.columnconfigure(1, weight=1)

    SeatType_TicketNum = Frame(master=mainframe)
    SeatType_TicketNum.grid(column=0, row=1)

    var = StringVar()
    var.set("Select Seat Type")
    seat_Type = Label(SeatType_TicketNum, textvariable=var)
    seat_Type.grid(column=0,  row=0)

    seat_type_val = StringVar()
    seat_type_val.set(SeatTypes.lower_hall.value)
    seat_Type_value = OptionMenu(SeatType_TicketNum, seat_type_val, SeatTypes.lower_hall.value, SeatTypes.upper_hall.value, SeatTypes.vip.value, command=ChangeSeatType)
    seat_Type_value.grid(column=0,  row=1)

    #CalSeatsLeft(c, )

    var = StringVar()
    var.set("# Of Tickets")
    ticket_num = Label(SeatType_TicketNum, textvariable=var)
    ticket_num.grid(column=0,  row=2)

    slider_val = IntVar()
    slider = Scale(SeatType_TicketNum, from_=1, to=10, orient=HORIZONTAL, variable=slider_val)
    slider.grid(column=0,  row=3)

    # if((seat_Type_value) == 'LH'):
    #     if(CalSeatsLeft(SeatType_TicketNum, show.ID, "LH") > slider_val):
    #         messagebox.showinfo("Failed! ", "Check Correct Number Of Seat!")
    #         return False
    # if((seat_Type_value) == 'UH'):
    #         if(CalSeatsLeft(SeatType_TicketNum, show.ID,"UP") > slider_val):
    #             messagebox.showinfo("Failed! ", "Check Correct Number Of Seat!")
    #             return False
    # if((seat_Type_value) == 'VIP'):
    #         if(CalSeatsLeft(SeatType_TicketNum, show.ID, "VIP") > slider_val):
    #             messagebox.showinfo("Failed! ", "Check Correct Number Of Seat!")
    #             return False



    cust_details = Frame(master=mainframe)
    cust_details.grid(column=1, row=1)


    var = StringVar()
    var.set("Name Lastname:")
    name = Label(cust_details, textvariable=var)
    name.grid(column=0,  row=0)

    name_var = StringVar()
    name_entry = Entry(cust_details, textvariable=name_var)
    name_entry.grid(column=1,  row=0)


    var = StringVar()
    var.set("Email:")
    email = Label(cust_details, textvariable=var)
    email.grid(column=0,  row=1)

    email_var = StringVar()
    email_entry = Entry(cust_details, textvariable=email_var)
    email_entry.grid(column=1,  row=1)

    var = StringVar()
    var.set("Phone:")
    phone = Label(cust_details, textvariable=var)
    phone.grid(column=0,  row=2)

    phone_var = StringVar()
    phone_entry = Entry(cust_details, textvariable=phone_var)
    phone_entry.grid(column=1,  row=2, sticky=EW)


    footer = Frame(mainframe)
    footer.grid(column=0, row=2, columnspan=2)
    
    var = StringVar()
    var.set("Create Booking")
    makebooking = Button(footer, textvariable=var, width=15, height=2, command=lambda: Create_booking(user, show, c, name_var, email_var, phone_var, slider_val, top, Movie_Name))
    makebooking.grid(column=0, row=0, sticky=NSEW)

    top.mainloop()

"""
sh = Show(2)

Booking_Form(sh, None)"""