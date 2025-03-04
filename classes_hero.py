class Hero:
    def __init__(self, name, toHitBonus, critOn=20, critMultiplier=2):
        # toHitBonus: z.B. Archery Fighting Style
        # critOn: change if e.g. Fighter/Champion
        self.name = name
        self.toHitBonus = toHitBonus
        self.critOn = critOn
        self.critMultiplier = critMultiplier

        self.damageSources = {} # stores different types of damage

    def calcCritDamage(self):
        for s in self.damageSources:
            if self.damageSources[s].is_static:                
                self.damageSources[s].critDamage = self.damageSources[s].baseDamage
            else:
                self.damageSources[s].critDamage = self.damageSources[s].baseDamage*self.critMultiplier
               
    def addDamageSource(self, source):
        self.damageSources[source.name] = source
        self.calcCritDamage()
    
    def calcToHitChance(self, monsterAC, checkAdvantage=False):
        toHitAC = monsterAC - self.toHitBonus
        if toHitAC < 2:
            toHitAC = 2
        if toHitAC > 19:
            toHitAC = 21
        if checkAdvantage:
            self.chance2Hit = 1 - ((toHitAC-1)/20)**2
            self.chance2Crit = 1-((self.critOn-1)/20)**2
        else:
            self.chance2Hit = 1 - (toHitAC-1)/20
            self.chance2Crit = 1-((self.critOn-1)/20)
            
    def damageCalculator(self):
        self.base_damage = {} # base Damage of each damage Source
        self.crit_damage = {} # crit Damage of each damage Source
        self.expected_damage = {} # expected Damage of each damage Source
        
        for s in self.damageSources:
            self.expected_damage[s] = self.damageSources[s].baseDamage*self.chance2Hit + self.damageSources[s].critDamage*self.chance2Crit
            self.base_damage[s] = self.damageSources[s].baseDamage
            self.crit_damage[s] = self.damageSources[s].critDamage
        
        self.heroValues = { # sums up damage types
            "Expected Damage":sum(self.expected_damage.values()),
            "Base Damage":sum(self.base_damage.values()),
            "Crit Damage":sum(self.crit_damage.values()),
            "Chance to Hit":self.chance2Hit,
            "Chance to Crit":self.chance2Crit
        }          
    
    def show_hero_stats(self, full=False):
        print(f"Helden Name: {self.name}")
        print(f"ToHit-Bonus: {self.toHitBonus:+}")
        print(f"Trefferwahrscheinlichkeit: {self.chance2Hit}")
        print(f"Zu erwartender Schaden: {sum(self.expected_damage.values()):.2f}")
        if full:
            print("-"*10)
            print("Detailaufschlüsselung:")
            for key in self.expected_damage:
                print(f"  * {key}")
                print(f"      Zu erwartender Schaden: {self.expected_damage[key]}")
                print(f"      Base Damage: {self.base_damage[key]}")
                print(f"      Crit Damage: {self.crit_damage[key]}")  
        
                      