#from passlib.hash import sha256_crypt
class User():
    def __init__(self, user_id="N/A", cinema_id="N/A",  username = "N/A", location="N/A", staff_type="N/A"):
        self.ID = user_id
        self.Cinema_ID = cinema_id
        self.Username = username
        self.Location = location
        self.Type = staff_type