import random
import math

dice_sides = int(input("How many sides should the dice have?: "))
throw_amount = int(input("How often should the dice be rolled?: "))
counter = 1

while throw_amount > 0:
    stringcounter = str(counter)
    print("The result of the", stringcounter +
          ". dice throw is: ", random.randrange(1, dice_sides))
    counter = counter + 1
    throw_amount = throw_amount - 1
