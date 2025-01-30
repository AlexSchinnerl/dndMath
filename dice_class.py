import numpy as np

class Dice:
    def __init__(self, minRoll, maxRoll):
        self.name = "d{}".format(maxRoll)
        self.minRoll = minRoll
        self.maxRoll = maxRoll
        self.dice = np.arange(minRoll,maxRoll+1)
    def calcDiceMean(self):
        diceMean = self.dice.mean()
        return diceMean

gwf_d6 = Dice(1,6)
gwf_d6.dice = np.array([3.5,3.5,3,4,5,6])

gwf_d10 = Dice(1,10)
gwf_d10.dice = np.array([5.5,5.5,3,4,5,6,7,8,9,10])

gwf_d12 = Dice(1,12)
gwf_d12.dice = np.array([6.5,6.5,3,4,5,6,7,8,9,10,11,12])

dice_dictionary = {
    "d2":Dice(1,2),
    "d4":Dice(1,4),
    "d6":Dice(1,6),
    "d8":Dice(1,8),
    "d10":Dice(1,10),
    "d12":Dice(1,12),
    "d20":Dice(1,20),
    "d100":Dice(1,100),
    "gwf_d6":gwf_d6,
    "gwf_d10":gwf_d10,
    "gwf_d12":gwf_d12
}

weapon_dictionary = {
    "1d4":(1, dice_dictionary["d4"]),
    "1d6":(1, dice_dictionary["d6"]),
    "1d8":(1, dice_dictionary["d8"]),
    "1d10":(1, dice_dictionary["d10"]),
    "1d12":(1, dice_dictionary["d12"]),
    "2d6":(2, dice_dictionary["d6"]),
    "gwf_2d6":(2, dice_dictionary["gwf_d6"]),
    "gwf_1d10":(1, dice_dictionary["gwf_d10"]),
    "gwf_1d12":(1, dice_dictionary["gwf_d12"]),
}