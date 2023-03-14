import dbConnection
from sql_show import *
from sql_screen import *
from Show import Show
import datetime
import sql_screen
import array
#Edgaras Levinskas 21065305 
def Generate_List(c, cinema_id, show_date):
    #shows = getShowsObject(c, cinema_id, show_date)
    shows = getShowsObject(c, cinema_id, show_date)
    shows_grouped = []

    for show in shows:
        if(len(shows_grouped) == 0 and len(shows) > 0):
            shows_grouped.append([show])
            #print("Added first")
            continue
        
        #print("Array len: ", len(shows_grouped))
        #print(shows_grouped)
        for i in range(0, len(shows_grouped)):
            #print(shows_grouped[i][0].Screen_ID)
            #print(show.Screen_ID, " :Screen id  groups:", shows_grouped[i].__str__())
            if(show.Screen_ID == shows_grouped[i][0].Screen_ID):
                #print("Matched screen")
                shows_grouped[i].append(show)
                break
            elif(i == len(shows_grouped) - 1):
                #print("Show loop")
                shows_grouped.append([show])

    for i in range(0, len(shows_grouped)):
        #print("Movie: ", sql_screen.getScreens(c, group[0].Screen_ID))
        Movie = sql_screen.getScreens(c, shows_grouped[i][0].Screen_ID)
        shows_grouped[i].insert(0, Movie)

    #print(shows_grouped)

    return shows_grouped
