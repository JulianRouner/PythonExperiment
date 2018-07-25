#import rounerPrinter

class Enemy:
    def __init__(self, health, inventory, activeWeapon, activeArmor):
        self.health = health
        self.inventory = inventory
        self.activeWeapon = activeWeapon
        self.activeArmor = activeArmor
    def fightPlayer(self, playerName):
        enemyname.health = enemyName.health - self.activeWeapon.damage 