#Correct way to import:
#   from CLASSES.Booking import Booking
#Edgaras Levinskas 21065305 
class Booking:
    """
    Booking class 

    Constructor:
        id=(int) def:N/A            id of booking;
        show_id=(int) def:N/A       id of show;
        cust_details=(str[])        Customer details, list: [0]Name Lastname, [1]Email, [2]Phone;
        bookings=(int)              Number of bookings;
        total_paid=(float)          Total amount paid;
        seattype=(enum: SeatTypes)  Seat type from enums: LH, UH, VIP;
        datepaid=(str)              Date the payment was done (Used to check for refunds) also datetime.date can be used;

    Variables:
        As constructor, however
        ❗ Date_Paid should use datetime.date format ❗ 
        ❗ pay attention to Cust_Details ordering ❗

    Use __str__ to print values to console
    """
    def __init__(self, id="N/A", show_id="N/A", cust_details=["N/A", "N/A", "N/A"], 
                bookings=0, total_paid=0, seat_type="N/A", date_paid="N/A"):
        self.ID = id
        self.Show_ID = show_id
        self.Cust_Details = cust_details
        self.Bookings = bookings
        self.Total_Paid = total_paid
        self.Seat_Type = seat_type
        self.Date_Paid = date_paid

    def __str__(self):
        print("_____Booking str_____")
        print("ID:                  ", self.ID)
        print("Show ID:             ", self.Show_ID)
        print("Customer Dets:       ", self.Cust_Details)
        print("Number of Bookings:  ", self.Bookings)
        print("Total Paid:          ", self.Total_Paid)
        print("Seat Type:           ", self.Seat_Type)
        print("Date Paid:           ", self.Date_Paid)