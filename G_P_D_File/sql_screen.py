def getScreens(c, screen_id):
	query = """SELECT screens.screen_id, movies.movie_name, movies.released, movies.duration, movies.rating, movies.description, movies.age_rating, movies.publisher, movies.genre
	FROM movies INNER JOIN screens ON movies.movie_id = screens.movie_id
	WHERE (((screens.screen_id)=""" + str(screen_id) + """));"""
	#print(query)
	c.execute(query)
	row = c.fetchone()
	#print(row)
	return row