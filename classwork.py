"""
We are going on a camping trip and we need to bring Ten items.  
To help with this we will create a random selector and assign it to a person(you). 
Your task is to create a program that ask the user the name. 
This name can only be a type string. We also want to know the age of the person. 
Only allow integer type to be accepted. 
If they are over 18 they can bring the knife 
otherwise a different item must be selected. 
At the end the program should end with " 
Thanks for Volunteering to bring item1 and item2 user_name." 
If the person is younger than 18 a print " 
I understand that you couldn't bring the knife but glad you could still contribute" 
Lastly create a random variable that ranges from 1-100 call it temperature . 
This will be used to let the campers know what to bring. 
if temperature is greater or equal to 80degrees say 
"its going to be hot so pack a swimsuit"  if temperature is between 68-79 say " 
The weather will be delightful " if temperature is 50-67 say 
"Might want to bring some warm clothes it will be cold"  
lastly if temperature is below 49 say " 
Its going to be freezing so pack warm clothes"

"""
#The camping list
camping_list = ['Chairs', 'Lantern', 'Bug Spray', 'Fire wood', 'Water']
camping_list2 = ['knife', 'Beans', 'Tent', 'Sleeping bag', 'Lighter']
camping_list3 = ['Chairs', 'Lantern', 'Bug Spray', 'Fire wood', 'Water', 'Beans', 'Tent', 'Sleeping bag', 'Lighter']

#random number genorator
import random
random_camping_gear = random.choice(camping_list)
random_camping_gear2 = random.choice(camping_list2)
random_camping_gear3 = random.choice(camping_list3)
random_temp = random.randint(1, 100)

#These are random items that you could get
item1 = random_camping_gear
item2 = random_camping_gear2
no_knife = random_camping_gear3

#name and age user inputs
name = input("What is your name?\n:")
age = int(input("What is your age?\n:"))

#What people will bring
if random_camping_gear == "knife" and age < 18 or random_camping_gear2 == "knife" and age < 18:
    print("You can't bring the knife, but you can bring " + no_knife)
    print("I understand that you couldn't bring the knife " + name + " but were glad you could still contribute")
else:
    print("Thanks for Volunteering to bring " + item1 + " and " + item2 + " " + name)

#Temp outside
print("Its going to be " + str(random_temp) + " degrees outside")
#The weather print for outside
if random_temp >= 80:
    print("So pack a swimsuit")
elif random_temp >= 68 and 79:
    print("The weather will be delightful so you won't need anything else")
elif random_temp >= 50 and 67:
    print("You might want to bring some warm clothes as well it will be cold")
elif random_temp <= 49:
    print("So pack warm clothes too")