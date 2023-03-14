
from tkinter import *
from tkinter import ttk, messagebox
# import cinemaClass
import dbConnection
import Screen

def screenGUI():
    show = Tk()
    show.title('Screen Details')
            
    show.geometry('900x600')

    style = ttk.Style()
            # pick a theme
    style.theme_use('default')

    style.configure("Treeview",
                            background="#D3D3D3",
                            foreground="black",
                            rowheight=25,
                            fieldbackground="#D3D3D3")

    style.map('Treeview', background=[('selected', "#347083")])

    tree_frame = Frame(show)
    tree_frame.pack(pady=10)
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(
                    tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()
    tree_scroll.config(command=my_tree.yview)

    my_tree['columns'] = ("Screen ID", "Cinema ID", "Movie ID", "Total Seats", "LH Seats", "UP Seats", "VIP Seats")

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column("Screen ID", anchor=CENTER, width=140)
    my_tree.column("Cinema ID", anchor=CENTER, width=140)
    my_tree.column("Movie ID", anchor=CENTER, width=140)
    my_tree.column("Total Seats", anchor=CENTER, width=140)
    my_tree.column("LH Seats", anchor=CENTER, width=140)
    my_tree.column("UP Seats", anchor=CENTER, width=140)
    my_tree.column("VIP Seats", anchor=CENTER, width=140)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Screen ID", text="Screen ID", anchor=CENTER)
    my_tree.heading("Cinema ID", text="Cinema ID", anchor=CENTER)
    my_tree.heading("Movie ID", text="Movie ID", anchor=CENTER)
    my_tree.heading("Total Seats", text="Total Seats", anchor=CENTER)
    my_tree.heading("LH Seats", text="LH Seats", anchor=CENTER)
    my_tree.heading("UP Seats", text="UP Seats", anchor=CENTER)
    my_tree.heading("VIP Seats", text="VIP Seats", anchor=CENTER)


    my_tree.tag_configure('evenrow', background="lightblue")


    con = dbConnection.get_connection()
    c = con.cursor()
    c.execute("SELECT cinema_id FROM cinemas")
    idCinemas = c.fetchall()
    c.execute("SELECT movie_id FROM movies")
    idMovies = c.fetchall()


    screenId_label = Label(show, text='Screen Id :-')
    screenId_label.pack(fill='y', expand='no', padx=20)
    screenId_label_entry = Entry(show)
    screenId_label_entry.pack(fill='y', expand='no', padx=20)

    data_frame = LabelFrame(show, text='Details')
    data_frame.pack(fill='x', expand='yes', padx=20)

    cinemaId_label = Label(data_frame, text="Cinema ID :")
    cinemaId_label.grid(row=0, column=0, padx=0, pady=0)
    cinemaId_entry = ttk.Combobox(data_frame, values=idCinemas)
    cinemaId_entry.grid(row=0, column=1, padx=0, pady=0)

    moveiId = Label(data_frame, text="Movie ID :")
    moveiId.grid(row=0, column=2, padx=0, pady=10)
    moveiId_entry = ttk.Combobox(data_frame, values=idMovies)
    moveiId_entry.grid(row=0, column=3, padx=0, pady=10)

    totalSeats_label = Label(data_frame, text="Total Seats :")
    totalSeats_label.grid(row=0, column=4, padx=10, pady=10)
    totalSeats_entry = Entry(data_frame)
    totalSeats_entry.grid(row=0, column=5, padx=10, pady=10)

    def query_database():
                    con = dbConnection.get_connection()
                    c = con.cursor()

                    c.execute("SELECT * FROM screens")
                    records = c.fetchall()
                    global count
                    count = 0
                    for record in records:
                        my_tree.insert(parent='', index='end', iid=count, text='', value=(record[0],record[1], record[2], record[3],record[4],record[5],record[6]), tags=('evenrow',))
                        count += 1

                    con.commit()
                    con.close()

    def select_Record(e):
                    screenId_label_entry.delete(0,END)
                    cinemaId_entry.delete(0,END)
                    moveiId_entry.delete(0,END)
                    totalSeats_entry.delete(0,END)

                    selected = my_tree.focus()
                    values = my_tree.item(selected, 'value')

                    screenId_label_entry.insert(0,values[0])
                    cinemaId_entry.insert(0,values[1])
                    moveiId_entry.insert(0,values[2])
                    totalSeats_entry.insert(0,values[3])


    def clear_entries():
                    screenId_label_entry.delete(0,END)
                    cinemaId_entry.delete(0,END)
                    moveiId_entry.delete(0,END)
                    totalSeats_entry.delete(0,END)

    def addNewScreen():
                    con = dbConnection.get_connection()
                    c = con.cursor()
                    
                    cinemaID = cinemaId_entry.get()
                    movieId =moveiId_entry.get()
                    totalSeat =totalSeats_entry.get()
                    seats = Screen.CalculateSeats(float(totalSeat))
                    seatsLH = int(seats[0])
                    seatsUP = int(seats[1])
                    seatsVIP = int(seats[2])

                    query = 'INSERT INTO screens (cinema_id, movie_id, total_seats, lower_hall, upper_hall, vip) VALUES (%s,%s,%s,%s,%s,%s);'
                    c.execute(query,(cinemaID, movieId, totalSeat,seatsLH,seatsUP,seatsVIP))
                    print("Sucessfully added")
                    con.commit()
                    con.close()
                    clear_entries()
                    my_tree.delete(*my_tree.get_children())  
                    query_database()
                    messagebox.showinfo("Added !!!..", "Your Sucessfully Add New Cinemas ")

    def deleteScreen():
                    x = my_tree.selection()[0]
                    my_tree.delete(x)

                    con = dbConnection.get_connection()
                    c = con.cursor()
                    
                    c.execute("DELETE FROM screens where screen_id = "+screenId_label_entry.get())

                    con.commit()
                    con.close()

                    clear_entries()

                    messagebox.showinfo("Deleted !!!..", "Your Successfully Deleted Screen!")

    def updateScreen():
                    selected = my_tree.focus()
                    
                    con = dbConnection.get_connection()
                    c = con.cursor()
                    
                    screenID = screenId_label_entry.get()
                    cinemaId = cinemaId_entry.get()
                    movie_ID =moveiId_entry.get()
                    totalSeat =totalSeats_entry.get()
                    seats = Screen.CalculateSeats(float(totalSeat))
                    print(seats[0])
                    print(seats[1])
                    print(seats[2])
                    seatsLH = int(seats[0])
                    seatsUP = int(seats[1])
                    seatsVIP = int(seats[2])

                    my_tree.item(selected, text='', values=(screenId_label_entry.get(),cinemaId_entry.get(),moveiId_entry.get(),totalSeats_entry.get(),seatsLH, seatsUP, seatsVIP) )

                    query = 'UPDATE screens SET cinema_id = %s, movie_id = %s, total_seats =%s, lower_hall = %s, upper_hall = %s, vip=%s WHERE screen_id = %s;'
                    print('here')
                    c.execute(query, (cinemaId, movie_ID, totalSeat, seatsLH, seatsUP, seatsVIP, screenID))
                    print('here2')

                    messagebox.showinfo("Updated !!!..", "Your sucessfully able to update!")
                    con.commit()
                    con.close()
                    clear_entries()
                    # record = c.fetchone()
                    query_database()


    frame_button = LabelFrame(show, text='Buttons')
    frame_button.pack(fill='x', expand='yes', padx=20)

    add_button = Button(frame_button,text='Add New Screen', command = addNewScreen)
    add_button.grid(row=0, column=0, padx=10, pady=10)
    update_button = Button(frame_button,text='Update Screen Details', command = updateScreen)
    update_button.grid(row=0, column=1, padx=10, pady=10)
    delete_button = Button(frame_button,text='Delete Screen', command=deleteScreen)
    delete_button.grid(row=0, column=2, padx=10, pady=10)
    clear_button = Button(frame_button,text='Clear Entry', command=clear_entries)
    clear_button.grid(row=0, column=3, padx=10, pady=10)

    my_tree.bind("<ButtonRelease-1>",select_Record)  

    query_database()

    show.mainloop()

