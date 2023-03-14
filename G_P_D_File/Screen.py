#Correct way to import:
#   from CLASSES.Screen import Screen
def CalculateSeats(total_seats):
    return [round(total_seats * 0.3), round((total_seats * 0.7) - 10), 10]

class Screen:
    """
    Screen class

    Constructor:
        id=(int) def:N/A      id of screen;
        lh=(int) def=0        number of seats for Lower Hall;
        uh=(int) def=0        number of seats for Upper Hall;
        vip=(int) def=0       number of seats for VIP Hall;

    Variables:
        As constructor

    Use __str__ to print values to console
    """
    def __init__(self, id="N/A", lh=0):
        self.ID = id
        self.LH_seats = lh
        self.UH_seats = lh * 1.5
        self.VIP_seats = 10

    def __str__(self):
        print("_____Screen str_____")
        print("ID:          ", self.ID)
        print("LH  Seats:   ", self.LH_seats)
        print("UH  Seats:   ", self.UH_seats)
        print("VIP  Seats:  ", self.VIP_seats)