
from tkinter import *
from tkinter import ttk, messagebox
import dbConnection
from User import User

def show(user):
    show = Tk()
    show.title('Shows Details')
            
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

    my_tree['columns'] = ("Show ID", "Screen ID", "Show Date", "Show Start")

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column("Show ID", anchor=CENTER, width=140)
    my_tree.column("Screen ID", anchor=CENTER, width=140)
    my_tree.column("Show Date", anchor=CENTER, width=140)
    my_tree.column("Show Start", anchor=CENTER, width=140)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Show ID", text="Show ID", anchor=CENTER)
    my_tree.heading("Screen ID", text="Screen ID", anchor=CENTER)
    my_tree.heading("Show Date", text="Show Date", anchor=CENTER)
    my_tree.heading("Show Start", text="Show Start", anchor=CENTER)

    con = dbConnection.get_connection()
    c = con.cursor()
    c.execute("SELECT screen_id FROM screens WHERE cinema_id = " + str(user.Cinema_ID))
    idScreen = c.fetchall()


    showId_label = Label(show, text='Show Id :-')
    showId_label.pack(fill='y', expand='no', padx=20)
    showId_label_entry = Entry(show)
    showId_label_entry.pack(fill='y', expand='no', padx=20)

    data_frame = LabelFrame(show, text='Details')
    data_frame.pack(fill='x', expand='yes', padx=20)

    screenId_label = Label(data_frame, text="Screen ID :")
    screenId_label.grid(row=0, column=0, padx=0, pady=0)
    screenId_entry = ttk.Combobox(data_frame, values=idScreen)
    screenId_entry.grid(row=0, column=1, padx=0, pady=0)

    showDate_label = Label(data_frame, text="Show Date :")
    showDate_label.grid(row=0, column=2, padx=0, pady=10)
    showDate_entry = Entry(data_frame)
    showDate_entry.grid(row=0, column=3, padx=0, pady=10)
    showDate_entry.insert(0, "YYYY-MM-DD")

    showStart_label = Label(data_frame, text="ShowStart Time :")
    showStart_label.grid(row=0, column=4, padx=10, pady=10)
    showStart_entry = Entry(data_frame)
    showStart_entry.grid(row=0, column=5, padx=10, pady=10)

    my_tree.tag_configure('evenrow', background="lightblue")

    def query_database():
                    con = dbConnection.get_connection()
                    c = con.cursor()
                    query = "SELECT shows.* FROM shows INNER JOIN (cinemas INNER JOIN screens ON cinemas.cinema_id = screens.cinema_id) ON shows.screen_id = screens.screen_id WHERE (((cinemas.cinema_id)= %s));"
                    c.execute(query, (user.Cinema_ID,))
                    records = c.fetchall()
                    global count
                    count = 0
                    for record in records:
                        my_tree.insert(parent='', index='end', iid=count, text='', value=(
                                    record[0], record[1], record[2], record[3]), tags=('evenrow',))
                        count += 1

                    con.commit()
                    con.close()

    def select_Record(e):
                    showId_label_entry.delete(0,END)
                    screenId_entry.delete(0,END)
                    showDate_entry.delete(0,END)
                    showStart_entry.delete(0,END)

                    selected = my_tree.focus()
                    values = my_tree.item(selected, 'value')

                    showId_label_entry.insert(0,values[0])
                    screenId_entry.insert(0,values[1])
                    showDate_entry.insert(0,values[2])
                    showStart_entry.insert(0,values[3])


    def clear_entries():
                    showId_label_entry.delete(0,END)
                    screenId_entry.delete(0,END)
                    showDate_entry.delete(0,END)
                    showStart_entry.delete(0,END)

    def addNewShow():

                    con = dbConnection.get_connection()
                    c = con.cursor()
                    
                    showID = showId_label_entry.get()
                    screenId =screenId_entry.get()
                    dateShow =showDate_entry.get()
                    showStart = showStart_entry.get()

                    query = 'INSERT INTO shows (screen_id, show_date, show_start) VALUES (%s,%s,%s);'
                    c.execute(query,(screenId, dateShow, showStart))
                    print("Sucessfully added")
                    con.commit()
                    con.close()
                    clear_entries()
                    my_tree.delete(*my_tree.get_children())  
                    query_database()
                    messagebox.showinfo("Added !!!..", "You sucessfully added a new show")

    def deleteShow():
                    x = my_tree.selection()[0]
                    my_tree.delete(x)

                    con = dbConnection.get_connection()
                    c = con.cursor()
                    
                    c.execute("DELETE FROM shows where show_id = "+showId_label_entry.get())

                    con.commit()
                    con.close()

                    clear_entries()

                    messagebox.showinfo("Deleted !!!..", "The show has been deleted!")

    def updateShow():
                    selected = my_tree.focus()
                    my_tree.item(selected, text='', values=(showId_label_entry.get(),screenId_entry.get(),showDate_entry.get(),showStart_entry.get()) )
                    con = dbConnection.get_connection()
                    c = con.cursor()
                    
                    showID = showId_label_entry.get()
                    screenId = screenId_entry.get()
                    showDateDate =showDate_entry.get()
                    showStart =showStart_entry.get()
                    query = 'UPDATE shows SET screen_id = %s, show_date = %s, show_start =%s WHERE show_id = %s;'
                    print('here')
                    c.execute(query, (screenId, showDateDate, showStart, showID,))
                    print('here2')

                    
                    con.commit()
                    con.close()
                    messagebox.showinfo("Updated !!!..", "Your sucessfully able to update!")
                    clear_entries()
                    # record = c.fetchone()
                    query_database()


    frame_button = LabelFrame(show, text='Buttons')
    frame_button.pack(fill='x', expand='yes', padx=20)

    add_button = Button(frame_button,text='Add New Show', command = addNewShow)
    add_button.grid(row=0, column=0, padx=10, pady=10)
    update_button = Button(frame_button,text='Update Show Details', command = updateShow)
    update_button.grid(row=0, column=1, padx=10, pady=10)
    delete_button = Button(frame_button,text='Delete Show', command=deleteShow)
    delete_button.grid(row=0, column=2, padx=10, pady=10)
    clear_button = Button(frame_button,text='Clear Entry', command=clear_entries)
    clear_button.grid(row=0, column=3, padx=10, pady=10)

    my_tree.bind("<ButtonRelease-1>",select_Record)  

    query_database()
    con.commit()
    con.close()
    show.mainloop()