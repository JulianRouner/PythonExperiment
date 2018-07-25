#import rounerPrinter

class Player:
    def __init__(self, health, inventory, activeWeapon, activeArmor):
        self.health = health
        self.inventory = inventory
        self.activeWeapon = activeWeapon
        self.activeArmor = activeArmor
    def fightEnemy(self, enemyName):
        enemyName.health = enemyName.health - self.activeWeapon.damage 