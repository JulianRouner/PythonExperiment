#import rounerPrinter

class Enemy:
    def __init__(self, name, health, inventory, activeWeapon, activeArmor):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.activeWeapon = activeWeapon
        self.activeArmor = activeArmor
    def fightPlayer(self, playerName):
        playerName.health = playerName.health - self.activeWeapon.damage 