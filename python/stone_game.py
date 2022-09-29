
import math

def stone_game(n:int ) -> bool:
    if not n:
        return False
    #print(reversed(range(1,math.floor(math.sqrt(n))+1)))

    for i in (range(1,math.floor(math.sqrt(n))+1)):
        if not stone_game(n -1 **2 ):
            return True

    return False


bol=stone_game(4)
print(bol)
