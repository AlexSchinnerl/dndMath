class DamageSource:
    def __init__(self, name, staticBonus=None, damageDice=None, diceAmount=None):
        self.name = name
        self.is_static = False
        self._staticBonus = staticBonus
        self._damageDice = damageDice
        self._diceAmount = diceAmount

        if staticBonus != None:
            self.baseDamage = self.staticBonus
            self.is_static = True
        else:
            self.baseDamage = self.damageDice.diceMean*self.diceAmount

    @property
    def staticBonus(self):
        return self._staticBonus
    @staticBonus.setter
    def staticBonus(self, value):
        self._staticBonus = value
        self.baseDamage = self.staticBonus
        self.is_static = True
    @property
    def damageDice(self):
        return self._damageDice
    @damageDice.setter
    def damageDice(self, value):
        self._damageDice = value
        self.baseDamage = self.damageDice.diceMean*self.diceAmount
    @property
    def diceAmount(self):
        return self._diceAmount
    @diceAmount.setter
    def diceAmount(self, value):
        self._diceAmount = value
        self.baseDamage = self.damageDice.diceMean*self.diceAmount
