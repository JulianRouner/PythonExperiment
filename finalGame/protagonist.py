#import rounerPrinter
#1 = Gun; 2 = sheild, 3 = lazer

class Player:
    def __init__(self, health, inventory, activeWeapon, activeArmor):
        self.health = health
        self.inventory = inventory
        self.activeWeapon = activeWeapon
        self.activeArmor = activeArmor
    def fightEnemy(self, enemyName):
        if enemyName.activeWeapon.weaponType == "1" and self.activeWeapon.weaponType == "3" or enemyName.activeWeapon.weaponType == "2" and self.activeWeapon.weaponType == "1" or enemyName.activeWeapon.weaponType == "1" and self.activeWeapon.weaponType == "2":
            enemyName.health = enemyName.health - self.activeWeapon.damage
    def equipHand(self, weaponName):
        self.activeWeapon = weaponName
        self.inventory.remove(weaponName)
        