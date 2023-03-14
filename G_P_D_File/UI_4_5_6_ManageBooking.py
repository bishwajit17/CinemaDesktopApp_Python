from tkinter import *
from tkinter import ttk, messagebox
import dbConnection
from sql_booking import *
from sql_show import *
from Validations import *
import datetime
import UI_7_SelectMovieToBook
import re 


con = dbConnection.get_connection()
c = con.cursor()

def Create_Booking(master, user):
    master.destroy()

def clearTree(tree):
   # clear treeview table
   for item in tree.get_children():
      tree.delete(item)

def sendRow(tree, table):
    tree.tag_configure('oddrow', background='white')
    tree.tag_configure('evenrow', background='lightblue')

    # send rows of the table (argument)
    count = 0
    # clear the tree before sending new rows
    clearTree(tree)
    for row in table:
        if count % 2 == 0:
            tree.insert('', END, values=row, tags=('evenrow',))
        else:
            tree.insert('', END, values=row, tags=('oddrow'))
        count +=1

def selectRecord(e, entries, booking_tree):
    # deletes the previous entries
    entries[0].delete(0, END)
    entries[1].delete(0, END)
    entries[2].delete(0, END)
    entries[3].delete(0, END)

    selected = booking_tree.focus()
    values = booking_tree.item(selected, 'value')
    
    if len(values) < 3:
        return
    
    # inserts the selected records
    entries[0].insert(0,values[1])
    entries[1].insert(0,values[2])
    entries[2].insert(0,values[3])
    entries[3].insert(0,values[0])

def updateRecord(c, entries):
    # gets the folowing records from treeview table
    cust_name = entries[0].get()
    cust_email = entries[1].get()
    cust_phone = entries[2].get()
    booking_id = entries[3].get()

    # validate user input 
    if cust_name == '':
        messagebox.showwarning("Failed", "Please Fill in Name")
        return
    elif (not Name_LastName(cust_name)):
        messagebox.showwarning("Failed", "Invalid Name Format")
        return
    
    if cust_email == '':
        messagebox.showwarning("Failed", "Please Fill in Email")
        return
    elif (not Email(cust_email)):
        messagebox.showwarning("Failed", "Invalid Email Address")
        return

    if cust_phone == '':
        messagebox.showwarning("Failed", "Please Fill in Phone")
        return
    elif (not PhoneNum(cust_phone)):
        messagebox.showwarning("Failed", "Invalid Phone Number")
        return
    
    # calls updateBooking function to update the selected record using sql query
    updateBooking(c, booking_id, cust_name, cust_email, cust_phone)
    # commits the changes to the database
    con.commit()
    messagebox.showinfo("Success", "Booking Updated Successfully")

    entries[0].delete(0, END)
    entries[1].delete(0, END)
    entries[2].delete(0, END)
    entries[3].delete(0, END)

def deleteRecord(c, booking_id_entry):
    # used to delete the selected record from the database (using sql query inside deleteBooking function)
    booking_id = booking_id_entry.get()
    deleteBooking(c, booking_id)
    con.commit()
    messagebox.showinfo("Success", "Booking Deleted Successfully")

def findRecord(booking_id_entry, table, booking_tree):
    # get the selected booking_id entry
    typed = booking_id_entry.get()
    booking_table = []

    for rows in range(len(table)):
        booking_table.append(table[rows][0])

    # validate booking_id user input
    if typed == '':
        messagebox.showerror("Error", "No Values Entered")
        return
    else:
        if re.fullmatch(re.compile(r'[1-9][0-9]?$|^10000$'), typed) == None:
            messagebox.showerror("Error", "Invalid Booking ID")
            return
    
        elif int(typed) in booking_table:
            entry = selectBooking(c, typed)
            sendRow(booking_tree, entry)
        else:
            messagebox.showerror("Error", "Booking ID not found")
            return

def refundRecord(c, booking_id_entry):
    # gets booking and show ID (using sql queries from selectBooking and getShowID functions)
    booking_id = booking_id_entry.get()
    record = selectBooking(c, booking_id)
    get_show_id = getShowID(c, booking_id)
    show_id = get_show_id[0][0]

    # used to get the show start date and time
    show_table = getShowTable(c, show_id)

    # combine show_start date and show_start time into one format
    show_start = datetime.datetime.strptime("{} {}".format(show_table[0][2], show_table[0][3]), "%Y-%m-%d %H:%M:%S")

    # get current date time
    current_time = datetime.datetime.now()

    # calculate time left for selected show to start.
    # this is done to avoid issuing refunds 1 day before the show starts
    time_left_for_show = show_start - current_time

    """
    if show time is past the date:
        then display messagebox saying "Show over"

    else if time left for show is less than 1 day:
        then display messagebox saying "Refund Unavailable"

    else:
        display messagebox saying the Refunded amount and customer name
        calling deleteBooking function which deletes the record in the database
        commit changes  
    """

    if current_time > show_start:
        messagebox.showinfo("Failed", "Show Over")
    elif time_left_for_show < datetime.timedelta(0, 0, 0, 23, 59, 59):
        messagebox.showinfo("Failed", "Refund Unavailable")
    else:
        messagebox.showinfo("Success", "Refunded " + str(record[0][1]) + " £" + str(record[0][6]/2))
        deleteBooking(c, booking_id)
        con.commit()

def refreshButton(booking_tree, cinema_ID):
    # used to update the treeview table
    con.commit()
    sendRow(booking_tree, getBooking(c, cinema_ID))

def RetrieveBooking(user, admin=None):
    if admin != None:
        admin.destroy()
    master = Toplevel()
    master.title('Bookings Details')
    master.geometry('1000x600') 

    # add style
    style = ttk.Style()
    # add theme
    style.theme_use('default')
    style.configure("Treeview",
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="#D3D3D3")

    style.map('Treeview', background=[('selected', "#347083")])


    # tree_frame for treeview table
    tree_frame = Frame(master)
    tree_frame.pack(pady = 10)
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    booking_tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="extended")
    booking_tree.pack()

    # creating columns
    tree_scroll.config(command=booking_tree.yview)
    booking_tree['columns']=("Booking ID", "Cust Name", "Cust Email", "Cust Phone", "Seat type", "# Tickets", "Total Paid £", "Date Paid")
    booking_tree.column('#0',width=0,stretch=NO)
    booking_tree.column("Booking ID", anchor=CENTER, width=90)
    booking_tree.column("Cust Name", anchor='w', width=140)
    booking_tree.column("Cust Email", anchor='w', width=180)
    for i in range(4):
        list = ["Cust Phone", "Seat type", "# Tickets", "Total Paid £"]
        booking_tree.column(list[i], anchor=CENTER, width=90)
    booking_tree.column("Date Paid", anchor='w', width=120)

    # creating heading
    booking_tree.heading("#0", text="", anchor=W)
    for i in range(8):
        list = ["Booking ID", "Cust Name", "Cust Email", "Cust Phone", "Seat type", "# Tickets", "Total Paid £", "Date Paid"]
        booking_tree.heading(list[i], text=list[i], anchor=CENTER)
    booking_tree.tag_configure('oddrow', background="lightblue")
    booking_tree.tag_configure('evenrow', background="lightblue")
    
    # add booking data to the tree 
    GBD = getBooking(c, user.Cinema_ID)
    GBD_1 = []
    for i in GBD:
        GBD_1.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
    sendRow(booking_tree, GBD_1)

    
    # to refresh the booking table records
    refresh_button = Button(master, text='Refresh', command=lambda:  refreshButton(booking_tree, user.Cinema_ID))
    refresh_button.pack(fill='y', padx=10, pady=10)


    # search_frame used to search for bookings using booking ID
    search_frame = LabelFrame(master)
    search_frame.pack(fill='x', expand='yes',padx=20)

    booking_id_label = Label(search_frame, text=" Search Booking ID")
    booking_id_label.grid(row=0,column=0,padx=10, pady=10)
    booking_id_entry = Entry(search_frame, width=10)
    booking_id_entry.grid(row=0,column=1,padx=10, pady=10) 

    # search button
    booking_id_button = Button(search_frame, text='Search', command=lambda:  findRecord(booking_id_entry, GBD_1, booking_tree))
    booking_id_button.grid(row=0,column=2,padx=10, pady=10)


    # edit_frame for editing customer details
    edit_frame = LabelFrame(master, text='Edit Details')
    edit_frame.pack(fill='x', expand='yes',padx=20)

    # used for updating cust_name details
    cust_name_label = Label(edit_frame, text="Customer Name:")
    cust_name_label.grid(row=0,column=0,padx=10, pady=10)
    cust_name_entry = Entry(edit_frame, width=20)
    cust_name_entry.grid(row=0,column=1, padx=10, pady=10)

    # used for updating cust_email details
    cust_email_label = Label(edit_frame, text="Customer Email:")
    cust_email_label.grid(row=0,column=2,padx=10, pady=10) 
    cust_email_entry = Entry(edit_frame, width=35)
    cust_email_entry.grid(row=0,column=3, padx=10, pady=10)

    # used for updating cust_phone details 
    cust_phone_label = Label(edit_frame, text="Customer Phone:")
    cust_phone_label.grid(row=0,column=4,padx=10, pady=10)
    cust_phone_entry = Entry(edit_frame, width=15)
    cust_phone_entry.grid(row=0,column=5, padx=10, pady=10)

    # update_ button used to update booking details (only cust_name, cust_email, cust_phone)
    update_button = Button(edit_frame, text='Update Booking', command=lambda:  updateRecord(c, entries=[cust_name_entry, cust_email_entry, cust_phone_entry, booking_id_entry]))
    update_button.grid(row=1, column=0, padx=10, pady=10)

    # delete_button used for deleting bookings
    delete_button = Button(edit_frame, text='Delete Booking', command=lambda:  deleteRecord(c, booking_id_entry))
    delete_button.grid(row=1, column=2, padx=10, pady=10)

    # refund_button used for refunding bookings 1 day before show starts
    refund_button = Button(edit_frame, text='Refund Booking', command= lambda:  refundRecord(c, booking_id_entry))
    refund_button.grid(row=1, column=4, padx=10, pady=10)


    # other_frame which contains a button called create_button which is used to create new bookings
    others_frame = LabelFrame(master)
    others_frame.pack(fill='x', expand='yes', padx=20)

    booking_tree.bind("<ButtonRelease-1>", lambda event:  selectRecord(e=event, entries=[cust_name_entry, cust_email_entry, cust_phone_entry, booking_id_entry,], booking_tree=booking_tree))

    create_button = Button(others_frame, text='Create Booking', command=lambda: UI_7_SelectMovieToBook.Innit(user))
    create_button.grid(row=0, column=0, padx=10, pady=10)

    master.mainloop()


#from User import User
#user = User(1, 1, "Ali", "Bristol", "Admin")
#RetrieveBooking(user)
