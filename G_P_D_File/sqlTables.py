#Correct way to import:
#   from CLASSES.sqlTables import sqlTables

from enum import Enum

class T(Enum):
    """
    All DATABASE tables mapped to their names
    PLEASE use this file in ALL SQL queries in case tables need to be renamed and to avoid typos in QUERIES!
    """
    bookings = "bookings"
    cinemas = "cinemas"
    movies = "movies"
    screens = "screens"
    shows = "shows"
    users = "users"