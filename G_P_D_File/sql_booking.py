from tkinter import messagebox
def getBooking(c, cinema_id):
    query = """
            SELECT bookings.booking_ID, bookings.cust_name, bookings.cust_email, bookings.cust_phone, bookings.seat_type, bookings.no_of_tickets, bookings.total_paid, bookings.date_paid
            FROM (shows INNER JOIN bookings ON shows.show_id = bookings.show_id) INNER JOIN (cinemas INNER JOIN screens ON cinemas.cinema_id = screens.cinema_id) ON shows.screen_id = screens.screen_id
            WHERE (((cinemas.cinema_id)=""" + str(cinema_id) + "));"

    c.execute(query)
    table = c.fetchall()
    return table

def updateBooking(c, booking_id, cust_name, cust_email, cust_phone):
    query = """
            UPDATE bookings SET bookings.cust_name= '""" + str(cust_name) + "', bookings.cust_email= '" + str(cust_email) + "', bookings.cust_phone= '" + str(cust_phone) + """' WHERE bookings.booking_id= """ + str(booking_id) + ";"
    
    c.execute(query)

def deleteBooking(c, booking_id):
    query = "DELETE FROM bookings WHERE bookings.booking_id=" + booking_id + ";"
    
    c.execute(query)

def selectBooking(c, booking_id):
    query = """
            SELECT bookings.booking_ID, bookings.cust_name, bookings.cust_email, bookings.cust_phone, bookings.seat_type, bookings.no_of_tickets, bookings.total_paid, bookings.date_paid
            FROM bookings
            WHERE (((bookings.booking_ID)=""" + str(booking_id) + "));"

    c.execute(query)
    table = c.fetchall()
    return table

def getShowID(c, booking_id):
    query="""
          SELECT bookings.show_id
          FROM bookings
          WHERE (((bookings.booking_ID)=""" + str(booking_id) + "));"
    c.execute(query)
    table = c.fetchall()
    return table

def InsertBooking(c, booking, user):
    messagebox.showinfo(title="Success", message="Booking inserted")
    
    query= """INSERT INTO bookings (user_id,
    show_id,
    cust_name,
    cust_email,
    cust_phone,
    seat_type,
    no_of_tickets,
    total_paid,
    date_paid)
    VALUES(""" + str(user.ID) + """, """ + str(booking.Show_ID) + """, '""" + str(booking.Cust_Details[0]) + """', '""" + str(booking.Cust_Details[1]) + """', '""" + str(booking.Cust_Details[2]) + """', '""" + str(booking.Seat_Type) + """', 
    '""" + str(booking.Bookings) + """', '""" + str(booking.Total_Paid) + """', '""" + str(booking.Date_Paid) + """');"""
    print(query)
    c.execute(query)