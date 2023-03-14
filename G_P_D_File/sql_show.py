from Show import Show
from CalSeatsLeft import *

def getShow(c, show_id):
	query = """
			SELECT bookings.booking_ID, bookings.show_id, bookings.seat_type, bookings.no_of_tickets 
			FROM bookings WHERE (((bookings.show_id)="""+ str(show_id) + "));"

	c.execute(query)
	table = c.fetchall()
	return table

def getTotalSeats(c, show_id):
	query = """
			SELECT shows.show_id, screens.lower_hall, screens.upper_hall, screens.vip
			FROM screens INNER JOIN shows ON screens.screen_id = shows.screen_id
			WHERE (((shows.show_id)="""+ str(show_id) +"));"

	c.execute(query)
	table = c.fetchall()
	return table

def getShowTable(c, show_id):
	query = """
			SELECT * FROM shows WHERE (((shows.show_id)="""+ str(show_id) + "));"

	c.execute(query)
	table = c.fetchall()
	return table

def getShows(c, cinema_id, show_date):
	query = """SELECT cinemas.cinema_id, shows.show_id, shows.show_start, shows.show_date, shows.screen_id
	FROM cinemas INNER JOIN (shows INNER JOIN screens ON shows.screen_id = screens.screen_id) ON cinemas.cinema_id = screens.cinema_id
	WHERE (((cinemas.cinema_id)=""" + str(cinema_id) + """) AND ((shows.show_date)='""" + str(show_date) + """'));"""

	c.execute(query)
	table = c.fetchall()
	return table

def getShowsObject(c, cinema_id, show_date):
	rows = getShows(c, cinema_id, show_date)
	shows = []

	for	row in rows:
		seatsleft = CalSeatsLeft(c, row[1])
		
		if(seatsleft != None):
			sh = Show(row[1], row[2], row[3], seatsleft[0], seatsleft[1], seatsleft[2], row[4])
			shows.append(sh)
		else:
			print("None detected!")
			print(Show(row[1], row[2], row[3]).__str__())
	return shows

def GetMovieName(c, show_id):
	query = """SELECT shows.show_id, movies.movie_name
	FROM shows INNER JOIN (movies INNER JOIN screens ON movies.movie_id = screens.movie_id) ON shows.screen_id = screens.screen_id
	WHERE (((shows.show_id)=""" + str(show_id) + """));"""

	c.execute(query)
	row = c.fetchone()
	return row
