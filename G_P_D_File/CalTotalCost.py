from SeatTypes import SeatTypes
from sql_show import *
from sql_cinema import *
import datetime

"""
checks the start time of the movie and returns the index which corresponds to the timings i.e [morning, afternoon, night]

if movie start_time is between 12am-8am:
    then return None

else if start time is before or at 12pm:
    then return index 0 (morning prices)

else if start time is before 5pm:
    then return index 1 (afternoon prices)

else:
    then return index 3 (night prices)
"""
def CheckTime(start):
    # time range which is used to get prices for seats at different times [00:00:00, 08:00:00, 12:00:00, 17:00:00, 23:59:59]
    timings = [datetime.time(0, 0, 0), datetime.time(8, 0, 0), datetime.time(12, 0, 0), datetime.time(17, 0, 0), datetime.time(23, 59, 59)]
    if timings[0] < start < timings[1]:
        print("Error: Show cannot start between 12-8am.")
        return None
    elif(start <= timings[2]):
        return 0
    elif(start <= timings[3]):
        return 1
    elif(start <= timings[4]):
        return 2

def CalTotalCost(c, cinema_id, show_id, seat_type, no_of_tickets):
    # Gets the cinema object
    cinema = getCinemaObject(c, cinema_id)
    # Gets show table from database
    shows = getShowTable(c, show_id)

    # Imports show start_time from show table (database) and converts the time format from datetime.timedelta to datetime.time
    # This is done beacause CheckTime function only accepts datetime.time format for its argument. 
    d = datetime.datetime.strptime(str(shows[0][3]), "%H:%M:%S")
    # Checks show_start time and returns an index [morn, afternoon, night, None] based on time of day, which is then used to find price of booking at selected time.
    index = CheckTime(datetime.time(d.hour, d.minute, d.second))

    #if index is None (show between 12-8am) then return None
    if index == None:
        return None
    """
    if seat_type is LH:
        then return price of booking for LH timings
    
    else if seat_type is UH:
        then return price of booking for UH timings 
    
    else:
        return price of bookng for VIP timings
    """
    if seat_type == SeatTypes.lower_hall.value:
        print("Here1")
        return cinema.LH_prices[index] * no_of_tickets
    elif seat_type == SeatTypes.upper_hall.value:
        print("Here2")
        return cinema.UH_prices[index] * no_of_tickets
    else:
        print("Here3", cinema.VIP_prices)
        return cinema.VIP_prices[index] * no_of_tickets


