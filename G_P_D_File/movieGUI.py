# Name: Bishwajit Sonar
# Student Id:- 21063833
from tkinter import *
from tkinter import ttk, messagebox
import dbConnection


def movie():
        movie = Tk()
        movie.title('Movies Details')
        movie.geometry('1000x600')

        style = ttk.Style()
        # pick a theme
        style.theme_use('default')

        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#D3D3D3")

        style.map('Treeview', background=[('selected', "#347083")])

        tree_frame = Frame(movie)
        tree_frame.pack(pady=10)
        # scroll bar in left side
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        my_tree = ttk.Treeview(
                tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        my_tree.pack()
        tree_scroll.config(command=my_tree.yview)

        my_tree['columns'] = ("ID", "Movie Name", "Release Date", "Publisher",
                                "Rating", "Description", "Age Rateing", "Gener", "Duration")

        my_tree.column('#0', width=0, stretch=NO)
        my_tree.column("ID", anchor=CENTER, width=80)
        my_tree.column("Movie Name", anchor='w', width=140)
        my_tree.column("Release Date", anchor=CENTER, width=80)
        my_tree.column("Publisher", anchor='w', width=140)
        my_tree.column("Rating", anchor=CENTER, width=80)
        my_tree.column("Description", anchor=W, width=500)
        my_tree.column("Age Rateing", anchor=CENTER, width=80)
        my_tree.column("Gener", anchor=CENTER, width=140)
        my_tree.column("Duration", anchor=CENTER, width=140)

        # Creating Heading

        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("ID", text="ID", anchor=CENTER)
        my_tree.heading("Movie Name", text="Movie Name", anchor=CENTER)
        my_tree.heading("Release Date", text="Release Date", anchor=CENTER)
        my_tree.heading("Publisher", text="Publisher", anchor=CENTER)
        my_tree.heading("Rating", text="Rating", anchor=CENTER)
        my_tree.heading("Description", text="Description", anchor=W)
        my_tree.heading("Age Rateing", text="Age Rateing", anchor=CENTER)
        my_tree.heading("Gener", text="Gener", anchor=CENTER)
        my_tree.heading("Duration", text="Duration", anchor=CENTER)

        my_tree.tag_configure('oddrow', background="lightblue")
        my_tree.tag_configure('evenrow', background="lightblue")

        movieId_label = Label(movie, text='Movie Id :-')
        movieId_label.pack(fill='y', expand='no', padx=20)
        movieId_label_entry = Entry(movie)
        movieId_label_entry.pack(fill='y', expand='no', padx=20)

        data_frame = LabelFrame(movie, text='Details')
        data_frame.pack(fill='x', expand='yes', padx=20)

        movieName_label = Label(data_frame, text="Movie Name :")
        movieName_label.grid(row=0, column=0, padx=10, pady=10)
        movieName_entry = Entry(data_frame)
        movieName_entry.grid(row=0, column=1, padx=10, pady=10)

        release_label = Label(data_frame, text="Release Date :")
        release_label.grid(row=0, column=2, padx=10, pady=10)
        release_entry = Entry(data_frame)
        release_entry.grid(row=0, column=3, padx=10, pady=10)
        release_entry.insert(0, "YYYY")

        publisher_label = Label(data_frame, text="Publisher :")
        publisher_label.grid(row=0, column=4, padx=10, pady=10)
        publisher_entry = Entry(data_frame)
        publisher_entry.grid(row=0, column=5, padx=10, pady=10)

        rating_label = Label(data_frame, text="Rating :")
        rating_label.grid(row=1, column=0, padx=10, pady=10)
        rating_entry = Entry(data_frame)
        rating_entry.grid(row=1, column=1, padx=10, pady=10)
        rating_entry.insert(4, "0.0 to 10")

        description_label = Label(data_frame, text="Description :")
        description_label.grid(row=1, column=2, padx=10, pady=10)
        description_entry = Entry(data_frame)
        description_entry.grid(row=1, column=3, padx=10, pady=10)

        ageRating_label = Label(data_frame, text="Age Rating :")
        ageRating_label.grid(row=1, column=4, padx=10, pady=10)
        ageRating_entry = ttk.Combobox(data_frame, values=["PG8","PG12", "PG16", "PG18"])
        ageRating_entry.grid(row=1, column=5, padx=10, pady=10)

        genre_label = Label(data_frame, text="Genre :")
        genre_label.grid(row=2, column=0, padx=10, pady=10)
        genre_entry = Entry(data_frame)
        genre_entry.grid(row=2, column=1, padx=10, pady=10)

        duration_label = Label(data_frame, text="Duration :")
        duration_label.grid(row=2, column=2, padx=10, pady=10)
        duration_entry = Entry(data_frame)
        duration_entry.grid(row=2, column=3, padx=10, pady=10)
        duration_entry.insert(8, "HH:MM:SS")

        # frame_button = LabelFrame(movie, text='Buttons')
        # frame_button.pack(fill='x', expand='yes', padx=20)

        # add_button = Button(frame_button, text='Add Movie')
        # add_button.grid(row=0, column=0, padx=10, pady=10)
        # update_button = Button(frame_button, text='Update Movie Details')
        # update_button.grid(row=0, column=1, padx=10, pady=10)
        # delete_button = Button(frame_button, text='Delete Movie')
        # delete_button.grid(row=0, column=2, padx=10, pady=10)
        # clear_button = Button(frame_button, text='Clear Entry')
        # clear_button.grid(row=0, column=3, padx=10, pady=10)

    # my_tree.bind("<ButtonRelease-1>",select_Record)
    # Commit change

    # query_database()
        def query_database():
                con = dbConnection.get_connection()
                c = con.cursor()

                c.execute("SELECT * FROM movies")
                records = c.fetchall()
                global count
                count = 0
                for record in records:
                        if count % 2 == 0:
                                my_tree.insert(parent='', index='end', iid=count, text='', value=(
                                record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
                        else:
                                my_tree.insert(parent='', index='end', iid=count, text='', value=(
                                record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
                        count += 1

                con.commit()
                con.close()
        # Select Record

#Select Record
        def select_Record(e):
                movieId_label_entry.delete(0,END)
                movieName_entry.delete(0,END)
                release_entry.delete(0,END)
                publisher_entry.delete(0,END)
                rating_entry.delete(0,END)
                description_entry.delete(0,END)
                ageRating_entry.delete(0,END)
                genre_entry.delete(0,END)
                duration_entry.delete(0,END)

                selected = my_tree.focus()
                values = my_tree.item(selected, 'value')

                movieId_label_entry.insert(0,values[0])
                movieName_entry.insert(0,values[1])
                release_entry.insert(0,values[2])
                publisher_entry.insert(0,values[3])
                rating_entry.insert(0,values[4])
                description_entry.insert(0,values[5])
                ageRating_entry.insert(0,values[6])
                genre_entry.insert(0,values[7])
                duration_entry.insert(0,values[8])


        def clear_entries():
                movieId_label_entry.delete(0,END)
                movieName_entry.delete(0,END)
                release_entry.delete(0,END)
                publisher_entry.delete(0,END)
                rating_entry.delete(0,END)
                description_entry.delete(0,END)
                ageRating_entry.delete(0,END)
                genre_entry.delete(0,END)
                duration_entry.delete(0,END)    

        def update():
                con = dbConnection.get_connection()
                c = con.cursor()

                selected = my_tree.focus()
                my_tree.item(selected, text='', values=(movieId_label_entry.get(),movieName_entry.get(),release_entry.get(),publisher_entry.get(),rating_entry.get(),description_entry.get(),ageRating_entry.get(),genre_entry.get(),duration_entry.get()) )

                MovieName = movieName_entry.get()
                ReleaseDate =release_entry.get()
                PublisherName =publisher_entry.get()
                Rating =rating_entry.get()
                MoviesDescri =description_entry.get()
                AgeRating =ageRating_entry.get()
                GenreMovie =genre_entry.get()
                DurationTime = duration_entry.get()

                movieId = movieId_label_entry.get()
                if (float(Rating) < 0 or float(Rating) > 10): 
                        messagebox.showinfo("Error !!!..", "Rating Must Be between 0 to 10")
                        return 0
                if (ReleaseDate != int):
                        messagebox.showinfo("Error !!!..", "Release Must Be YYYY Formate")
                        return 0
                query = 'UPDATE movies SET movie_name = %s, released = %s, publisher =%s, rating= %s, description= %s, age_rating= %s, genre= %s, duration= %s WHERE movie_id = %s;'
                print('here')
                c.execute(query, (MovieName, ReleaseDate, PublisherName,Rating, MoviesDescri, AgeRating, GenreMovie,DurationTime, movieId,))
                print('here2')
                messagebox.showinfo("Updated !!!..", "Your sucessfully able to update!")
                con.commit()
                con.close()
                movieId_label_entry.delete(0,END)
                movieName_entry.delete(0,END)
                release_entry.delete(0,END)
                publisher_entry.delete(0,END)
                rating_entry.delete(0,END)
                description_entry.delete(0,END)
                ageRating_entry.delete(0,END)
                genre_entry.delete(0,END)
                duration_entry.delete(0,END)
                # record = c.fetchone()
                query_database()
                

        #Add Record into database
        def addNewMovies():
                con = dbConnection.get_connection()
                c = con.cursor()

                MovieName = movieName_entry.get()
                ReleaseDate =release_entry.get()
                PublisherName =publisher_entry.get()
                Rating =rating_entry.get()
                MoviesDescri =description_entry.get()
                AgeRating =ageRating_entry.get()
                GenreMovie =genre_entry.get()
                DurationTime = duration_entry.get()
                if (float(Rating) < 0 or float(Rating) > 10): 
                        messagebox.showinfo("Error !!!..", "Rating Must Be between 0 to 10")
                        return 0
                if (ReleaseDate != int):
                        messagebox.showinfo("Error !!!..", "Release Must Be YYYY Formate")
                        return 0
                        
                query = 'INSERT INTO movies(movie_name, released, publisher, rating, description, age_rating, genre,duration) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);'
                c.execute(query,(MovieName, ReleaseDate, PublisherName,Rating, MoviesDescri, AgeRating, GenreMovie,DurationTime))
                print("Sucessfully added")
                con.commit()
                con.close()
                clear_entries()
                my_tree.delete(*my_tree.get_children())  
                query_database()
                messagebox.showinfo("Added !!!..", "Your are able to add new movie!")

        #Add Button 

        def deleteMovies():
                x = my_tree.selection()[0]
                my_tree.delete(x)

                con = dbConnection.get_connection()
                c = con.cursor()
                
                c.execute("DELETE FROM movies where movie_id = "+movieId_label_entry.get())

                con.commit()
                con.close()

                clear_entries()

                messagebox.showinfo("Deleted !!!..", "Your movie has been deleted!")
        
        frame_button = LabelFrame(movie, text='Buttons')
        frame_button.pack(fill='x', expand='yes', padx=20)

        add_button = Button(frame_button,text='Add Movie', command=addNewMovies)
        add_button.grid(row=0, column=0, padx=10, pady=10)
        update_button = Button(frame_button,text='Update Movie Details', command=update)
        update_button.grid(row=0, column=1, padx=10, pady=10)
        delete_button = Button(frame_button,text='Delete Movie', command=deleteMovies)
        delete_button.grid(row=0, column=2, padx=10, pady=10)
        clear_button = Button(frame_button,text='Clear Entry', command=clear_entries)
        clear_button.grid(row=0, column=3, padx=10, pady=10)

        my_tree.bind("<ButtonRelease-1>",select_Record)

        query_database()
        movie.mainloop()
