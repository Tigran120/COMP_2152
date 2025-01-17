import random

weapon=["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
wp_strength=[1,2,3,4,5,6]
weaponRoll = random.randint(0,5)
heroStrength=0
heroStrength +=weaponRoll

if weaponRoll <=2:
    print("You rolled a weak weapon, friend")
elif weaponRoll <=4:
    print("Your weapon is meh")
else:
    print("Nice weapon, friend!")
if weaponRoll !=0:
    print ("Thank goodness you didn't roll the Fist...")




