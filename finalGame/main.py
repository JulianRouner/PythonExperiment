#import rounerPrinter
import enemy
import weapon
import protagonist as protag

laserGun = weapon.Weapon("Laser gun", 10, [0], [0])
mainPlayer = protag.Player(20, [0], laserGun, [0])
mainEnemy  = enemy.Enemy(15, [0], laserGun, [0])

def battle():
    mainPlayer.fightEnemy(mainEnemy)
    return("Player dealt %s damage.") % (mainPlayer.activeWeapon.damage)
    
print(battle())