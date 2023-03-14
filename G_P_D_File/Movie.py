#Correct way to import:
#   from CLASSES.Movie import Movie
class Movie:
    """
    Movie class

    Constructor:
        id=(int) def:N/A            id of movie;
        movie_details=(str[])       Movie details, list: [0]Movie Name [1]Description [2]Rating (Audience) [3]Duration [4]Rating (Age) [5]Genres;

    Variables:
        As constructor, but
        ❗ Pay attention to ordering of Movie_Details variable ❗

    Use __str__ to print values to console
    """
    def __init__(self, id="N/A", movie_details=["N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]):
        self.ID = id
        self.Movie_Details = movie_details

    
    

    def __str__(self):
        print("_____Booking str_____")
        print("ID:                  ", self.ID)
        print("Movie Dets:          ", self.Movie_Details)