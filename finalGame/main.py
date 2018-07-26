from rounerPrinter import *
import enemy
import weapon
import protagonist as protag
from random import randint

#1 = Gun; 2 = shield, 3 = laser

coordinates = [0,0]

shield   = weapon.Weapon("Shield", 10, 1)
laserGun = weapon.Weapon("Laser gun", 10, 2)
gun      = weapon.Weapon("Gun", 10, 3)

mainPlayer = protag.Player(20, [0], weapon.Weapon("Default Weapon", 0, 0), 0)
mainEnemy  = enemy.Enemy("Robot", 15, [0], weapon.Weapon("Default Weapon", 0, 0), [0])

mainPlayer.inventory.append(gun)
mainPlayer.inventory.append(laserGun)
mainPlayer.inventory.append(shield)

mainEnemy.inventory.append(gun)
mainEnemy.inventory.append(laserGun)
mainEnemy.inventory.append(shield)

def walk(xCoord, yCoord):
    coordinates[1] = xCoord
    coordinates[2] = yCoord

def chooseWeapons():
    battleOption = input("Would you like to: \n a) Shoot a laser \n b) Raise your shield \n c) Shoot a gun \n") 
    enemyBattleOption = randint(1, 3)
    
    if battleOption == "a":
        mainPlayer.equipHand(laserGun)
        slowPrint("Player shot a laser.", 0.06)
    elif battleOption == "b":
        mainPlayer.equipHand(shield)
        slowPrint("Player raised shields.", 0.06)
    elif battleOption == "c":
        mainPlayer.equipHand(gun)
        slowPrint("Player shot a gun.", 0.06)
    
    if enemyBattleOption == 1:
        mainEnemy.equipHand(laserGun)
        slowPrint("Enemy shot a laser.", 0.06)
    elif enemyBattleOption == 2:
        mainEnemy.equipHand(shield)
        slowPrint("Enemy raised shields.", 0.06)
    elif enemyBattleOption == 3:
        mainEnemy.equipHand(gun)
        slowPrint("Enemy shot a gun.", 0.06)
        
def battle(myPlayer, myEnemy):
    slowPrint("You have encountered " + colorPrint(myEnemy.name, RED, BOLD) + ".", 0.06)
    while (myPlayer.health > 0 or myEnemy.health > 0): #while one opponent alive
        chooseWeapons()
        if myPlayer.fightEnemy(myEnemy):
            myEnemy.health -= myPlayer.activeWeapon.damage
        elif not myPlayer.fightEnemy(myEnemy):
            myPlayer.health -= myEnemy.activeWeapon.damage
        else:
            slowPrint("You used the same weapon. No damage was dealt.", 0.06)
            print("")
        #print("Player dealt " + str(mainPlayer.activeWeapon.damage) + " damage.")
        slowPrint("Enemy now has " + str(myEnemy.health) + " health.", 0.06)
        #print(mainEnemy.name + " dealt " + str(mainEnemy.activeWeapon.damage) + " damage.")
        slowPrint("Player now has " + str(myPlayer.health) + " health.", 0.06)
        print("")
        
        myEnemy.putAway()
        myPlayer.putAway()
        #chooseWeapons()
    slowPrint("The game has ended.", 0.06)

battle(mainPlayer, mainEnemy)