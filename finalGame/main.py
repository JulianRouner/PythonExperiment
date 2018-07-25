#import rounerPrinter
import enemy
import weapon
import protagonist as protag
from random import randint

#1 = Gun; 2 = shield, 3 = laser

shield   = weapon.Weapon("Shield", 10, 1)
laserGun = weapon.Weapon("Laser gun", 10, 2)
gun      = weapon.Weapon("Gun", 10, 3)

mainPlayer = protag.Player(20, [0], [0], 0)
mainEnemy  = enemy.Enemy("Robot", 15, [0], 0, [0])


mainPlayer.inventory.append(gun)
mainPlayer.inventory.append(laserGun)
mainPlayer.inventory.append(shield)

mainEnemy.inventory.append(gun)
mainEnemy.inventory.append(laserGun)
mainEnemy.inventory.append(shield)


battleOption = input("Would you like to: \n a) Shoot a laser \n b) Raise your shield \n c) Shoot a gun \n") 
enemyBattleOption = randint(1, 3)

if battleOption == "a":
    mainPlayer.equipHand(laserGun)
    print("Player shot a laser.")
elif battleOption == "b":
    mainPlayer.equipHand(shield)
    print("Player raised shields.")
elif battleOption == "c":
    mainPlayer.equipHand(gun)

if enemyBattleOption == 1:
    mainEnemy.equipHand(laserGun)
    print("Enemy shot a laser.")
elif enemyBattleOption == 2:
    mainEnemy.equipHand(shield)
    print("Enemy raised shields.")
elif enemyBattleOption == 3:
    mainEnemy.equipHand(gun)
    print("Enemy shot a gun.")
    
mainPlayer.fightEnemy(mainEnemy)
mainEnemy.fightPlayer(mainPlayer)

#print("Player dealt " + str(mainPlayer.activeWeapon.damage) + " damage.")
print("Enemy now has " + str(mainEnemy.health) + " health.")
#print(mainEnemy.name + " dealt " + str(mainEnemy.activeWeapon.damage) + " damage.")
print("Player now has " + str(mainPlayer.health) + " health.")

#print(battle())