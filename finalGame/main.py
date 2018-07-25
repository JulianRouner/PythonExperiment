#import rounerPrinter
import enemy
import weapon
import protagonist as protag
from random import randint

#1 = Gun; 2 = shield, 3 = laser

shield   = weapon.Weapon("Shield", 10, 1)
laserGun = weapon.Weapon("Laser gun", 10, 2)
gun      = weapon.Weapon("Gun", 10, 3)

mainPlayer = protag.Player(20, [0], [shield, laserGun, gun], 0)
mainEnemy  = enemy.Enemy("Robot", 15, [shield, laserGun, gun], 0, [0])

battleOption = input("Would you like to: \n a) Shoot a laser \n b) Raise your shield \n c) Shoot a gun") 

if battleOption == "a":
    mainPlayer.equipHand(laserGun)
    print("Player shot a laser.")
elif battleOption == "b":
    mainPlayer.equipHand(shield)
    print("Player raised shields.")
elif battleOption == "c":
    mainPlayer.equipHand(gun)

mainEnemy.fightPlayer(mainPlayer)
mainPlayer.fightEnemy(mainEnemy)

print("Player dealt " + str(mainPlayer.activeWeapon.damage) + " damage.")
print("Enemy now has " + str(mainEnemy.health) + " health.")
print(mainEnemy.name + " dealt " + str(mainEnemy.activeWeapon.damage) + " damage.")
print("Player now has " + str(mainPlayer.health) + " health.")

#print(battle())