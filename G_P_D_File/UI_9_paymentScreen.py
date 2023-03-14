
from tkinter import *
from Booking import Booking
from datetime import date
import dbConnection
import datetime
import UI_8_CreateBooking 
import sql_booking
my_date = datetime.datetime.now()    # Get current datetime
# print(my_date)
# 2022-07-05 09:55:34.814728                    # Import datetime module
dates = date.today()
current_hour = my_date.hour
current_minute = my_date.minute          # Applying hour attribute of datetime module
# print(current_hour)                  # Print hour
# 9

def Go_Back(top, user, show):
    top.destroy()
    UI_8_CreateBooking.Booking_Form(show, user)

def Confirm_Booking(booking, user):
    booking.Date_Paid = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    booking.__str__()
    con = dbConnection.get_connection()
    c = con.cursor()
    sql_booking.InsertBooking(c, booking, user)
    con.commit()
    

def Draw_PaymentScreen(user, booking, show, movie_name):
    app = Toplevel()

    # Give a title to your app
    app.title("Payment Screen")
    app.geometry("730x400")
    app.resizable(False,False)
    app.columnconfigure(0, weight=1)

    mainframe = Frame(master=app)
    mainframe.grid(column=0, row=0, sticky=NSEW)
    mainframe.grid_columnconfigure(0, weight=1)
  
    mainframe.grid_columnconfigure(0, weight=1)
    mainframe.grid_columnconfigure(1, weight=1)


    header = Frame(master=mainframe)
    header.grid(column=0, row=0, columnspan=2, sticky=NSEW)
    header.grid_columnconfigure(2, weight=1)

    var = StringVar()
    var.set("Back")
    Backbutton = Button(header, textvariable=var, width=10, height=2, command=lambda: Go_Back(app, user, show))
    Backbutton.grid(column=0, row=0, rowspan=3)

    var = StringVar()
    var.set("Creating a booking for")
    createbookingfor = Label(header, textvariable=var)
    createbookingfor.grid(column=1,  row=0)

    var = StringVar()
    var.set(str(movie_name))
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
    
    # Constructing the first frame, frame1
    frame1 = LabelFrame(mainframe, text="Booking Details", padx=15, pady=15, )

    # Displaying the frame1 in row 0 and column 0
    frame1.grid(column=0, row=1, sticky="NSEW")

    name = Label(frame1, text='Full Name :')
    name.grid(row=0, column=0, sticky=E)
    nameValue = Label(frame1, text=str(booking.Cust_Details[0]))
    nameValue.grid(row=0, column=1, padx=10, pady=10, sticky=W)

    phoneNumber = Label(frame1, text='Phone Number :' )
    phoneNumber.grid(row=1, column=0, sticky=E)
    naphoneNumberValue = Label(frame1, text=str(booking.Cust_Details[2]))
    naphoneNumberValue.grid(row=1, column=1, padx=10, pady=10, sticky=W)

    email = Label(frame1, text='Email :' )
    email.grid(row=2, column=0, sticky=E)
    emailValue = Label(frame1, text=str(booking.Cust_Details[1]))
    emailValue.grid(row=2, column=1, padx=10, pady=10, sticky=W)

    noOfTicket = Label(frame1, text='Number Of Tickets :' )
    noOfTicket.grid(row=3, column=0, sticky=E)
    noOfTicket = Label(frame1, text=str(booking.Bookings))
    noOfTicket.grid(row=3, column=1, padx=10, pady=10, sticky=W)

    seatType = Label(frame1, text='Seat Type :' )
    seatType.grid(row=4, column=0, sticky=E)
    seatTypeValue = Label(frame1, text=str(booking.Seat_Type))
    seatTypeValue.grid(row=4, column=1, padx=10, pady=10, sticky=W)

    # Constructing the second frame, frame2
    frame2 = LabelFrame(mainframe, text="Payment Details", padx=15, pady=15)

    # Displaying the frame2 in row 0 and column 1
    frame2.grid(column=1, row=1, sticky="NSEW")

    cardNumber = Label(frame2, text='Card Number :' )
    cardNumber.grid(row=0, column=0)
    cardNumberEntry = Entry(frame2 )
    cardNumberEntry.grid(row=0, column=1, padx=10, pady=10)
    cardNumberEntry.insert(0, "")

    expireDate = Label(frame2, text='Expiration Date :' )
    expireDate.grid(row=1, column=0)
    expireDateEntry = Entry(frame2 )
    expireDateEntry.grid(row=1, column=1, padx=10, pady=10)
    expireDateEntry.insert(0, "MM/YY")

    ccv = Label(frame2, text='CSC :' )
    ccv.grid(row=2, column=0)
    ccvEntry = Entry(frame2)
    ccvEntry.grid(row=2, column=1, padx=10, pady=10)
    ccvEntry.insert(0, "###")

    confirm = Button(frame2, text="Confirm", width=10, height=2, command=lambda: Confirm_Booking(booking, user))
    confirm.grid(column=1, row=4, pady=10)

    #app.update()
    #print("Width: ", app.winfo_width())
    #mainframe.configure(width=app.winfo_width())


    mainframe.update()
    #mainframe.configure(width=1000, background='red')

    # Make the loop for displaying app
    app.mainloop()

