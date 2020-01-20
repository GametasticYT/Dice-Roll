import random
import math

dice_sides = int(input("How many sides should the dice have?: "))
throw_amount = int(input("How often should the dice be rolled?: "))

while throw_amount > 0:
	counter = 1
	print("The result of the " + counter +
	      ". dice throw is: " + random.randrange(1, dice_sides))
	counter = counter + 1
    throw_amount = throw_amount - 1
