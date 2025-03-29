print("Welcome to Treasure Island. Your mission is to find the treasure.")

left_or_right = input("Would you like to go left or right? ")
if left_or_right != "left":
    print("You fall into a hole. Game over")
else:
    swim_or_wait = input("Would you like to swim or wait? ")
    if swim_or_wait != "wait":
        print("Attacked by trout. Game Over")
    else:
        red_or_blue = input("Do you choose the red or the blue door? ")
        if red_or_blue == "red":
            print("Burned by fire. Game Over")
        elif red_or_blue == "blue":
            print("Eaten by beasts. Game Over")
        elif red_or_blue == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
