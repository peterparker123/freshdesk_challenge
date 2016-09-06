#Python program for challenge

import random

def Name():	
	return (input("Enter you name:"))
	
def NameNumberGenerator(x):	
	return "Name GeneratedNumber %s" %(Name() + str(x))

num = random.randrange(6,15)
print(NameNumberGenerator(num))