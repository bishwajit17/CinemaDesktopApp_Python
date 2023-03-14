#Correct way to import:
#   from CLASSES.Cinema import Cinema
def calculateUH_price(base_price):
    """
    Calculates UH hall price
    Inputs:
        base_price=(float)
    Returns:
        float rounded to 2 nums
    """
    return round(float(base_price) * 1.2, 2)


def calculateVIP_price(base_price):
    """
    Calculates VIP hall price
    Inputs:
        base_price=(float)
    Returns:
        float rounded to 2 nums
    """
    return round(calculateUH_price(base_price) * 1.2, 2)
    
class Cinema:
    """
    Cinema class

    Constructor:
        id=(int) def:N/A            id of cinema;
        name=(str) def:N/A          name of cinema;
        location=(str) def:N/A      location of cinema;
        morn_LH=(float) def:0       morning lower hall price;
        after_LH=(float) def:0      afternoon lower hall price;
        night_LH=(float) def:0      evening lower hall price;
        Other prices are calculated in constructor using LH price;

    Variables:
        As constructor, except prices are 3 arrays (LH, UH, VIP) of 3 prices (MORN, AFTER, NIGHT)
        example: night price of VIP: cinema.VIP_prices[2]
        ❗ Upon setting LH_prices variable, UH and VIP prices will be set automatically ❗

    Use __str__ to print values to console
    """
    def __init__(self, id="N/A", name="N/A", location="N/A", morn_LH=0, after_LH=0, night_LH=0):
        self.ID = id
        self.Name = name
        self.Location = location
        self.LH_prices = [morn_LH, after_LH, night_LH]
        self.UH_prices = [calculateUH_price(morn_LH), calculateUH_price(after_LH), calculateUH_price(night_LH)]
        self.VIP_prices = [calculateVIP_price(morn_LH), calculateVIP_price(after_LH), calculateVIP_price(night_LH)]

    def __str__(self):
        print("_____Cinema str_____")
        print("ID:       ", self.ID)
        print("Name:     ", self.Name)
        print("Location: ", self.Location)
        print("LH  prices (MORN; AFT; NIGHT): ", self.LH_prices[0], self.LH_prices[1], self.LH_prices[2])
        print("UH  prices (MORN; AFT; NIGHT): ", self.UH_prices[0], self.UH_prices[1], self.UH_prices[2])
        print("VIP prices (MORN; AFT; NIGHT): ", self.VIP_prices[0], self.VIP_prices[1], self.VIP_prices[2])
