import numpy as np

class Dice:
    def __init__(self, minRoll, maxRoll):
        self.name = "d{}".format(maxRoll)
        self.minRoll = minRoll
        self.maxRoll = maxRoll
        self.dice = np.arange(minRoll,maxRoll+1)
        self.diceMean = self.dice.mean()
        
    @property
    def dice(self):
        return self._dice
    @dice.setter
    def dice(self, value):
        self._dice = value
        self.diceMean = self.dice.mean()
    
dice_dictionary = {
    "d2":Dice(1,2),
    "d4":Dice(1,4),
    "d6":Dice(1,6),
    "d8":Dice(1,8),
    "d10":Dice(1,10),
    "d12":Dice(1,12),
    "d20":Dice(1,20),
    "d100":Dice(1,100),
}