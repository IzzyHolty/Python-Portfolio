# Playing around with array functions in python.

import random
import sys
import os
import matplotlib

Fish_name_list = ['Ned', 'Buffy Blubbers', 'Harley Finn', 'Sushi']
Fish_name_list.insert(4, 'Swim Shady')

print("The best fish name is", Fish_name_list[random.randint(0, len(Fish_name_list))])

newfishname = input("What do you think is the best fish name? ")
Fish_name_list.insert(5, newfishname)
print(Fish_name_list[5], "is a dumb fish name.")

#dictionary of fish and their owners

fishdata = {'Ned' : 'Digby',
            'Buffy Blubbers' : 'Willow',
            'Harley Finn' : 'Bruce',
            'Sushi' : 'Chef',
            'Swim Shady' : "Marshall",
            newfishname : 'you'}

randomfish = random.choice(list(fishdata.keys()))
print("The best fish is", randomfish, "owned by", fishdata.get(randomfish))

