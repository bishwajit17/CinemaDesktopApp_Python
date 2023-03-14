
def bookings_per_cinema(c):
    # Query of bookings from each cinema using cinema_id.  
    query1 = """
             SELECT cinemas.cinema_id, cinemas.cinema_name
             FROM (movies INNER JOIN ((cinemas INNER JOIN 
             (screens INNER JOIN shows ON screens.screen_id = 
             shows.screen_id) ON cinemas.cinema_id = screens.cinema_id) 
             INNER JOIN users ON cinemas.cinema_id = users.cinema_id) 
             ON movies.movie_id = screens.movie_id) INNER JOIN bookings 
             ON (users.user_id = bookings.user_id) AND (shows.show_id = bookings.show_id);
             """
    # Query of cinema table
    query2 = """
             SELECT cinemas.cinema_id, cinemas.cinema_name
             FROM cinemas;
             """
    # Executing query1
    c.execute(query1)
    # Stores the contents of query1
    table1 = c.fetchall()

    # Executing query2
    c.execute(query2)
    # Stores the contents of query2
    table2 = c.fetchall()

    # To count the number of bookings per each cinema
    count = 0

    # Appends contents of table1 into Q1T and converts the tuples into a 2D list
    Q1T = []
    for row in range(len(table1)):
        Q1T.append(list(table1[row]))

    # Q2T appends the cinema table from table2 because table2 is a list of tuples and it cannot be modified 
    # Adds a new column in Q2T which is set to 0 (this column will store the number of bookings for each cinema)
    Q2T = [[0 for i in range(3)]for j in range(len(table2))]
    for row in range(len(table2)):
         Q2T[row][0] = table2[row][0]
         Q2T[row][1] = table2[row][1]

    # Iterating through Q2T and Q1T rows and links the cinema_id. It then counts how many cinema_ids are being
    # linked between Q1T and Q2T and counts them which is then stored inside Q2T 2nd column (total_bookings) 
    for x in range(len(Q2T)):
        for y in range(len(Q1T)):
            if Q2T[x][0] == Q1T[y][0]:
                count += 1
                Q2T[x][2] = count
        count = 0
    return Q2T

def revenue_per_cinema(c):
    # Query of total_revenue for each cinema using cinema_id. 
    # So cinema_id from cinema table and total_paid (per customer) from bookings table
    query1 = """
             SELECT cinemas.cinema_id, bookings.total_paid
             FROM cinemas INNER JOIN ((shows INNER JOIN bookings 
             ON shows.show_id = bookings.show_id) INNER JOIN screens 
             ON shows.screen_id = screens.screen_id) ON cinemas.cinema_id = screens.cinema_id;
             """
    
    # Query of cinema table
    query2 = """
             SELECT cinemas.cinema_id, cinemas.cinema_name
             FROM cinemas;
             """
    
    # Executing query1
    c.execute(query1)
    # Stores the contents of query1
    table1 = c.fetchall()

    # Executing query2
    c.execute(query2)
    # Stores the contents of query2
    table2 = c.fetchall()

    # Stores the revenue of each cinema
    revenue = []
    
    # Appends contents of table1 into Q1T and converts the tuples into a 2D list
    Q1T = []
    for row in range(len(table1)):
        Q1T.append(list(table1[row]))

    # Q2T appends the cinema table from table2 because table2 is a list of tuples and it cannot be modified 
    # Adds a new column in Q2T which is set to 0 (this column will store the total revenues for each cinema)
    Q2T = [[0 for i in range(3)]for j in range(len(table2))]
    for row in range(len(table2)):
         Q2T[row][0] = table2[row][0]
         Q2T[row][1] = table2[row][1]

    # Iterating through Q2T and Q1T rows and links the cinema_ids. It then appends the revenues (per cinema) inside 
    # the revenue list. We then sum the elements of the revenue list and the result is then stored inside Q2T 3nd 
    # column (total_revenue).
    for x in range(len(Q2T)):
        for y in range(len(Q1T)):
            if Q2T[x][0] == Q1T[y][0]:
                revenue.append(Q1T[y][1])
                Q2T[x][2] = sum(revenue)
        revenue.clear()
        
    for row in range(len(Q2T)):
        pass
    return Q2T

def top_revenue_movie(c):
    # Query of movie_id from the movie table and total_paid from bookings table
    query1 = """
             SELECT movies.movie_id, bookings.total_paid FROM movies INNER JOIN 
             ((shows INNER JOIN bookings ON shows.show_id = bookings.show_id) 
             INNER JOIN screens ON shows.screen_id = screens.screen_id) ON movies.movie_id = screens.movie_id;
             """

    # Query of all movie ids and movie names
    query2 = """
             SELECT movies.movie_id, movies.movie_name FROM movies;
             """

    # Executing query1
    c.execute(query1)
    # Stores the contents of query1
    table1 = c.fetchall()

    # Executing query2
    c.execute(query2)
    # Stores the contents of query2
    table2 = c.fetchall()

    # Stores the revenue of each movie
    movie_revenue = []

    # Appends contents of table1 into Q1T and converts the tuples into a 2D list
    Q1T = []
    for row in range(len(table1)):
        Q1T.append(list(table1[row]))

    # Q2T appends the movie_id and movie name from table2 because table2 is a list of tuples and it cannot be modified 
    # Adds a new column in Q2T which is set to 0 (this column will store the total revenue for each movie)
    Q2T = [[0 for i in range(3)]for j in range(len(table2))]
    for row in range(len(table2)):
         Q2T[row][0] = table2[row][0]
         Q2T[row][1] = table2[row][1]

    # Iterating through Q2T and Q1T rows and links the movie_ids. It then appends the revenues (per movie) inside 
    # the movie_revenue list. We then sum the elements of the movie_revenue list and the result is then stored inside Q2T 3nd 
    # column (revenue for each movie).
    for x in range(len(Q2T)):
        for y in range(len(Q1T)):
            if Q2T[x][0] == Q1T[y][0]:
                movie_revenue.append(Q1T[y][1])
                Q2T[x][2] = sum(movie_revenue)
        movie_revenue.clear()
    
    # Sorting the Q2T list by decending order in the 3nd column
    Q2T = sorted(Q2T,key=lambda l:l[2], reverse=True)
    return Q2T

def staff_bookings(c):
    # Query of bookings made by each Staff member
    query1 = """
             SELECT bookings.user_id, users.user_type
             FROM users INNER JOIN bookings ON users.user_id = bookings.user_id
             WHERE (((users.user_type)="Staff"));
             """

    # Query of all Staff user_ids and user_names
    query2 = """
             SELECT users.user_id, users.user_name
             FROM users WHERE (((users.user_type)='Staff'));
             """

    # Executing query1
    c.execute(query1)
    # Stores the contents of query1
    table1 = c.fetchall()

    # Executing query2
    c.execute(query2)
    # Stores the contents of query2
    table2 = c.fetchall()

    # To count the number of bookings made per Staff member
    count = 0

    # Appends contents of table1 into Q1T and converts the tuples into a 2D list
    Q1T = []
    for row in range(len(table1)):
        Q1T.append(list(table1[row]))

    # Q2T appends the user_id and user_name from table2 because table2 is a list of tuples and it cannot be modified 
    # Adds a new column in Q2T which is set to 0 (this column will store bookings made by Staff)
    Q2T = [[0 for i in range(3)]for j in range(len(table2))]
    for row in range(len(table2)):
         Q2T[row][0] = table2[row][0]
         Q2T[row][1] = table2[row][1]


    # Iterating through Q2T and Q1T rows and links the user_ids. It then counts how many user_ids are being
    # linked between Q1T and Q2T and counts them which is then stored inside Q2T 3nd column (total_bookings) 
    for x in range(len(Q2T)):
        for y in range(len(Q1T)):
            if Q2T[x][0] == Q1T[y][0]:
                count += 1
                Q2T[x][2] = count
        count = 0
    
    # Sorting the Q2T list by decending order in the 3nd column
    Q2T = sorted(Q2T,key=lambda l:l[2], reverse=True)
    return Q2T

#calling all functions
"""
print("---------------------------------")
print(bookings_per_cinema())
print("---------------------------------")
print(revenue_per_cinema())
print("---------------------------------")
print(top_revenue_movie())
print("---------------------------------")
print(staff_bookings())
print("---------------------------------")
"""