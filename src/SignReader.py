from enum import Enum
class Sign(Enum):
    NONE = 0
    STOP = 1
    GO = 2
class Color(Enum):
    NONE = 0
    RED = 1
    BLACK = 2
    GREEN = 3
    BLUE = 4
    YELLOW = 5
class SignReader:
    def read_sign(this,color):
        if(color == 0):
            current_sign = Sign.NONE
        elif(color == 1):
            current_sign = Sign.STOP
        else:
            current_sign = Sign.GO
        return current_sign
    current_sign = Sign.NONE
