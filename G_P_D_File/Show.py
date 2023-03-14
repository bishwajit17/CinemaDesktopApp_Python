#Correct way to import:
#   from CLASSES.Show import Show
class Show:
    """
    Show class 

    Constructor:
        id=(int) def:N/A                id of show;
        start_time=(string) def:N/A     Hour and minute when the show starts (Can be used with datetime.time and not str);
        show_date=(string) def:N/A      Year Month Day when the show takes place (Can be used with datetime.date and not str);
        left_lh=(int) def=0             number of seats left for Lower Hall;
        left_uh=(int) def=0             number of seats left for Upper Hall;
        left_vip=(int) def=0            number of seats left for VIP Hall;
        screen_id=(int) def:N/A         Screen id the show is assigned to; (Used for UI screen 7)

    Variables:
        As constructor, ❗ however Time and Date should use datetime.time and datetime.date formats respectively ❗

    Use __str__ to print values to console
    """
    def __init__(self, id="N/A", start_time="N/A", show_date="N/A", booked_lh=0, booked_uh=0, booked_vip=0, screen_id="N/A"):
        self.ID = id
        self.Time = start_time
        self.Date = show_date
        self.LH_booked = booked_lh
        self.UH_booked = booked_uh
        self.VIP_booked = booked_vip
        self.Screen_ID = screen_id

    def __str__(self):
        print("_____Shows str_____")
        print("ID:                 ", self.ID)
        print("Time:               ", self.Time)
        print("Date:               ", self.Date)
        print("LH  Seats booked:   ", self.LH_booked)
        print("UH  Seats booked:   ", self.UH_booked)
        print("VIP  Seats booked:  ", self.VIP_booked)
        print("Screen_ID:          ", self.Screen_ID)