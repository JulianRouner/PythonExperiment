#import rounerPrinter
import enemy
import weapon
import protagonist as protag
from random import randint

laserGun = weapon.Weapon("Laser gun", 10, [0], [0])
mainPlayer = protag.Player(20, [0], laserGun, [0])
mainEnemy  = enemy.Enemy("Robot", 15, [0], laserGun, [0])

mainPlayer.fightEnemy(mainEnemy)
print("Player dealt " + str(mainPlayer.activeWeapon.damage) + " damage.")
print("Enemy now has " + str(mainEnemy.health) + " health.")

#print("Player now has ")

mainEnemy.fightPlayer(mainPlayer)

print(mainEnemy.name + " dealt " + str(mainEnemy.activeWeapon.damage) + " damage.")
print("Player now has " + str(mainPlayer.health) + " health.")

#print(battle())