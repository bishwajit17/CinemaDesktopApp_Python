from SeatTypes import SeatTypes
import dbConnection

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

# Returns seats left  
def CalSeatsLeft(c, show_id):
    # Gets all the bookings for that particular show.
    shows = getShow(c, show_id)

    # Gets the total seats for that particular show.
    total_seats = getTotalSeats(c, show_id)
    # [lower_hall, upper_hall, vip]
    seats_booked = [0, 0, 0]
    seats_left = [0, 0, 0]

    """
    if selected show is seat_type (LH, UH or VIP):
        then sum all booked seats for each seat_type
        example: LH=10, UH=25, VIP=2, so seats_booked = [10, 25, 2]

    repeat this process by the total bookings for selected show
    """
    for row in range(len(shows)):
        if shows[row][2] == SeatTypes.lower_hall.value:
            seats_booked[0] = seats_booked[0] + shows[row][3]
        elif shows[row][2] == SeatTypes.upper_hall.value:
            seats_booked[1] = seats_booked[1] + shows[row][3]
        else:
            seats_booked[2] = seats_booked[2] + shows[row][3]

    """
    Subtracts total_seats from booked_seats for each seat_type
    seats_left = [(total_LH - booked_LH), (total_UH - booked_UP), (total_VIP - booked_VIP)]

    checks if seat_count is less than or 0
    if LH, UH, or VIP seats_left is less than or equal to 0:
        then return None (NULL)
        example: LH_left = 0, UH_left=25, VIP_left=2: 
                 seats_left = [None, 25, 0]
    """
    for i in range(len(seats_left)):
        seats_left[i] = total_seats[0][i+1] - seats_booked[i]
    #print(seats_left)
    return seats_left

#con = dbConnection.get_connection()
#c = con.cursor()

#CalSeatsLeft(c, 12)
