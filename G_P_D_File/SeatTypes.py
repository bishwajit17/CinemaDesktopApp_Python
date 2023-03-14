#Correct way to import:
#   from SeatTypes import SeatTypes

from enum import Enum

class SeatTypes(Enum):
    lower_hall = 'LH'
    upper_hall = 'UH'
    vip = 'VIP'