
from tkinter import *
from tkinter import ttk, messagebox
import Cinema
import dbConnection
import ScreenGUI
def cinema():
        cinema = Tk()
        cinema.title('Cinema Details')
        cinema.geometry('1100x600')

        style = ttk.Style()
        # pick a theme
        style.theme_use('default')

        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#D3D3D3")

        style.map('Treeview', background=[('selected', "#347083")])

        tree_frame = Frame(cinema)
        tree_frame.pack(pady=10)
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        my_tree = ttk.Treeview(
                tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        my_tree.pack()
        tree_scroll.config(command=my_tree.yview)

        my_tree['columns'] = ("ID", "Cinema Name", "Location", "MorningLHprice",
                                "MorningUHprice", "MorningVIPprice", "AfterNoonLHprice",
                                "AfterNoonUHprice", "AfterNoonVIPprice", "NightLHprice",
                                "NightUHprice", "NightVIPprice")

        my_tree.column('#0', width=0, stretch=NO)
        my_tree.column("ID", anchor=CENTER, width=80)
        my_tree.column("Cinema Name", anchor=CENTER, width=80)
        my_tree.column("Location", anchor=CENTER, width=80)
        my_tree.column("MorningLHprice", anchor=CENTER, width=80)
        my_tree.column("MorningUHprice", anchor=CENTER, width=80)
        my_tree.column("MorningVIPprice", anchor=CENTER, width=80)
        my_tree.column("AfterNoonLHprice", anchor=CENTER, width=80)
        my_tree.column("AfterNoonUHprice", anchor=CENTER, width=80)
        my_tree.column("AfterNoonVIPprice", anchor=CENTER, width=80)
        my_tree.column("NightLHprice", anchor=CENTER, width=80)
        my_tree.column("NightUHprice", anchor=CENTER, width=80)
        my_tree.column("NightVIPprice", anchor=CENTER, width=80)

        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("ID", text="ID", anchor=CENTER)
        my_tree.heading("Cinema Name", text="Cinema Name", anchor=CENTER)
        my_tree.heading("Location", text="Location", anchor=CENTER)
        my_tree.heading("MorningLHprice", text="MorningLHprice", anchor=CENTER)
        my_tree.heading("MorningUHprice", text="MorningUHprice", anchor=CENTER)
        my_tree.heading("MorningVIPprice", text="MorningVIPprice", anchor=CENTER)
        my_tree.heading("AfterNoonLHprice", text="AfterNoonLHprice", anchor=CENTER)
        my_tree.heading("AfterNoonUHprice", text="AfterNoonUHprice", anchor=CENTER)
        my_tree.heading("AfterNoonVIPprice", text="AfterNoonVIPprice", anchor=CENTER)
        my_tree.heading("NightLHprice", text="NightLHprice", anchor=CENTER)
        my_tree.heading("NightUHprice", text="NightUHprice", anchor=CENTER)
        my_tree.heading("NightVIPprice", text="NightVIPprice", anchor=CENTER)

        my_tree.tag_configure('evenrow', background="lightblue")

        cinemaId_label = Label(cinema, text='Cinema Id :-')
        cinemaId_label.pack(fill='y', expand='no', padx=20)
        cinemaId_label_entry = Entry(cinema)
        cinemaId_label_entry.pack(fill='y', expand='no', padx=20)

        data_frame = LabelFrame(cinema, text='Details')
        data_frame.pack(fill='x', expand='yes', padx=20)

        cinemaName_label = Label(data_frame, text="Cinema Name :")
        cinemaName_label.grid(row=0, column=0, padx=10, pady=10)
        cinemaName_entry = Entry(data_frame)
        cinemaName_entry.grid(row=0, column=1, padx=10, pady=10)

        release_label = Label(data_frame, text="Location :")
        release_label.grid(row=0, column=2, padx=10, pady=10)
        release_entry = Entry(data_frame)
        release_entry.grid(row=0, column=3, padx=10, pady=10)

        publisher_label = Label(data_frame, text="MorningLHprice :")
        publisher_label.grid(row=0, column=4, padx=10, pady=10)
        publisher_entry = Entry(data_frame)
        publisher_entry.grid(row=0, column=5, padx=10, pady=10)

        ageRating_label = Label(data_frame, text="AfterNoonLHprice :")
        ageRating_label.grid(row=1, column=0, padx=10, pady=10)
        ageRating_entry = Entry(data_frame)
        ageRating_entry.grid(row=1, column=1, padx=10, pady=10)

        NightLHprice_label = Label(data_frame, text="NightLHprice :")
        NightLHprice_label.grid(row=1, column=2, padx=10, pady=10)
        NightLHprice_entry = Entry(data_frame)
        NightLHprice_entry.grid(row=1, column=3, padx=10, pady=10)


        def query_database():
                con = dbConnection.get_connection()
                c = con.cursor()

                c.execute("SELECT * FROM cinemas")
                records = c.fetchall()
                global count
                count = 0
                for record in records:
                    my_tree.insert(parent='', index='end', iid=count, text='', value=(
                                record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11]), tags=('evenrow',))
                    count += 1

                con.commit()
                con.close()


        def select_Record(e):
                cinemaId_label_entry.delete(0,END)
                cinemaName_entry.delete(0,END)
                release_entry.delete(0,END)
                publisher_entry.delete(0,END)
                ageRating_entry.delete(0,END)
                NightLHprice_entry.delete(0, END)

                selected = my_tree.focus()
                values = my_tree.item(selected, 'value')

                cinemaId_label_entry.insert(0,values[0])
                cinemaName_entry.insert(0,values[1])
                release_entry.insert(0,values[2])
                publisher_entry.insert(0,values[3])
                ageRating_entry.insert(0,values[6])
                NightLHprice_entry.insert(0, values[9])


        def clear_entries():
                cinemaId_label_entry.delete(0,END)
                cinemaName_entry.delete(0,END)
                release_entry.delete(0,END)
                publisher_entry.delete(0,END)
                ageRating_entry.delete(0,END)
                NightLHprice_entry.delete(0, END)

        def addNewCinemas():

                con = dbConnection.get_connection()
                c = con.cursor()
                
                cinemaName = cinemaName_entry.get()
                ReleaseDate =release_entry.get()
                PublisherName =publisher_entry.get()
                Rating = Cinema.calculateUH_price(float(PublisherName))
                MoviesDescri =Cinema.calculateVIP_price(float(PublisherName))
                AgeRating =ageRating_entry.get()
                GenreMovie =Cinema.calculateUH_price(float(AgeRating))
                DurationTime = Cinema.calculateVIP_price(float(AgeRating))
                NightlHprice_entry = NightLHprice_entry.get()
                NightuHprice_entry = Cinema.calculateUH_price(float(NightlHprice_entry))
                NightvIPprice_entry = Cinema.calculateUH_price(float(NightlHprice_entry))

                query = 'INSERT INTO cinemas(cinema_name, location, morn_LH_price, morn_UH_price, morn_VIP_price, after_LH_price, after_UH_price, after_VIP_price, night_LH_price,night_UH_price, night_VIP_price) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                c.execute(query,(cinemaName, ReleaseDate, PublisherName,Rating, MoviesDescri, AgeRating, GenreMovie,DurationTime, NightlHprice_entry, NightuHprice_entry,NightvIPprice_entry))
                print("Sucessfully added")
                con.commit()
                con.close()
                clear_entries()
                my_tree.delete(*my_tree.get_children())  
                query_database()
                messagebox.showinfo("Added !!!..", "sucessfully add new Cinemas "+ cinemaName)

        def deleteCinemas():
                x = my_tree.selection()[0]
                my_tree.delete(x)

                con = dbConnection.get_connection()
                c = con.cursor()
                
                c.execute("DELETE FROM cinemas where cinema_id = "+cinemaId_label_entry.get())

                con.commit()
                con.close()

                clear_entries()

                messagebox.showinfo("Deleted !!!..", "movie has been deleted!")

        def updateCinema():
                selected = my_tree.focus()
                
                
                con = dbConnection.get_connection()
                c = con.cursor()
                
                cinemaID = cinemaId_label_entry.get()
                cinemaName = cinemaName_entry.get()
                ReleaseDate =release_entry.get()
                PublisherName =publisher_entry.get()
                Rating = Cinema.calculateUH_price(float(PublisherName))
                MoviesDescri =Cinema.calculateVIP_price(float(PublisherName))
                AgeRating =ageRating_entry.get()
                GenreMovie =Cinema.calculateUH_price(float(AgeRating))
                DurationTime = Cinema.calculateVIP_price(float(AgeRating))
                NightlHprice_entry = NightLHprice_entry.get()
                NightuHprice_entry = Cinema.calculateUH_price(float(NightlHprice_entry))
                NightvIPprice_entry = Cinema.calculateUH_price(float(NightlHprice_entry))

                my_tree.item(selected, text='', values=(cinemaId_label_entry.get(),cinemaName_entry.get(),release_entry.get(),publisher_entry.get(),Rating,MoviesDescri,ageRating_entry.get(),GenreMovie,DurationTime, NightLHprice_entry.get(),NightuHprice_entry,NightvIPprice_entry) )

                query = 'UPDATE cinemas SET cinema_name = %s, location = %s, morn_LH_price =%s, morn_UH_price= %s, morn_VIP_price= %s, after_LH_price= %s, after_UH_price= %s, after_VIP_price= %s, night_LH_price = %s, night_UH_price = %s, night_VIP_price = %s WHERE cinema_id = %s;'
                print('here')
                c.execute(query, (cinemaName, ReleaseDate, PublisherName,Rating, MoviesDescri, AgeRating, GenreMovie,DurationTime, NightlHprice_entry, NightuHprice_entry, NightvIPprice_entry,cinemaID,))
                print('here2')

                messagebox.showinfo("Updated !!!..", "sucessfully able to update!")
                con.commit()
                con.close()
                clear_entries()
                # record = c.fetchone()
                query_database()
        frame_button = LabelFrame(cinema, text='Buttons')
        frame_button.pack(fill='x', expand='yes', padx=20)

        add_button = Button(frame_button,text='Add New Cinema', command = addNewCinemas)
        add_button.grid(row=0, column=0, padx=10, pady=10)
        update_button = Button(frame_button,text='Update Cinema Details', command = updateCinema)
        update_button.grid(row=0, column=1, padx=10, pady=10)
        delete_button = Button(frame_button,text='Delete Cinemas', command=deleteCinemas)
        delete_button.grid(row=0, column=2, padx=10, pady=10)
        delete_button = Button(frame_button,text='Edit Screen', command=ScreenGUI.screenGUI)
        delete_button.grid(row=0, column=3, padx=10, pady=10)
        clear_button = Button(frame_button,text='Clear Entry', command=clear_entries)
        clear_button.grid(row=0, column=4, padx=10, pady=10)

        my_tree.bind("<ButtonRelease-1>",select_Record)  

        query_database()

        cinema.mainloop()

