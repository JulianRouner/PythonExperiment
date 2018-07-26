import enemy
from weapon import Weapon

#import rounerPrinter
#1 = Gun, 2 = shield, 3 = laser

class Player:
    def __init__(self, health, inventory, activeWeapon, activeArmor):
        self.health = float(health)
        self.inventory = inventory
        self.activeWeapon = activeWeapon
        self.activeArmor = activeArmor
    def fightEnemy(self, enemyName):
        if self.activeWeapon.weaponType == 1 and enemyName.activeWeapon.weaponType == 2 or self.activeWeapon.weaponType == 2 and enemyName.activeWeapon.weaponType == 3 or self.activeWeapon.weaponType == 3 and enemyName.activeWeapon.weaponType == 1:
            return 1
        else:
            return 0
    def equipHand(self, weaponName):
        self.activeWeapon = weaponName
        self.inventory.remove(weaponName)
        return self.activeWeapon
    def putAway(self):
        self.inventory.append(self.activeWeapon)
        self.activeWeapon = Weapon("Default Weapon", 0, 0)