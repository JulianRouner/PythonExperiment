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
    slowPrint("Would you like to: \n a) Shoot a laser \n b) Raise your shield \n c) Shoot a gun", 0.06)
    battleOption = input("") 
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
    slowPrint("You have encountered \033[1;31m" + str(myEnemy.name)  + ".", 0.06)
    print(RESET)
    while (True): #while one opponent alive
        chooseWeapons()
        if myPlayer.fightEnemy(myEnemy) and not myEnemy.fightEnemy(myPlayer):
            myEnemy.health -= myPlayer.activeWeapon.damage
            slowPrint("\033[1;32mPlayer dealt " + str(mainPlayer.activeWeapon.damage) + " damage." + RESET, 0.06)
            print(RESET)
        elif not myPlayer.fightEnemy(myEnemy) and myEnemy.fightEnemy(myPlayer):
            myPlayer.health -= myEnemy.activeWeapon.damage
            slowPrint("\033[1;31m" + mainEnemy.name + " dealt " + str(mainEnemy.activeWeapon.damage) + " damage." + RESET, 0.06)
        else:
            slowPrint("\033[1;33mYou used the same weapon. No damage was dealt." + RESET, 0.06)
            print("")
        
        if myPlayer.health <= 0:
            slowPrint(colorPrint("The enemy has penetrated your armor. You must retreat now for your own survival.", RED, [BOLD]), 0.06)
            break
        elif myEnemy.health <= 0:
            slowPrint(colorPrint("You have defeated the enemy.", GREEN, [BOLD]), 0.06)
            break
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