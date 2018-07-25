#import rounerPrinter
#1 = Gun; 2 = shield, 3 = laser

class Enemy:
    def __init__(self, name, health, inventory, activeWeapon, activeArmor):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.activeWeapon = activeWeapon
        self.activeArmor = activeArmor
    def fightPlayer(self, playerName):
        if playerName.activeWeapon.weaponType == "1" and self.activeWeapon.weaponType == "3" or playerName.activeWeapon.weaponType == "2" and self.activeWeapon.weaponType == "1" or playerName.activeWeapon.weaponType == "1" and self.activeWeapon.weaponType == "2":
            playerName.health = playerName.health - self.activeWeapon.damage 
    def equipHand(self, weaponName):
        self.activeWeapon = weaponName
        self.inventory.remove(weaponName)