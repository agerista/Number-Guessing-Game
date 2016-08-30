#Guess the number game written on May 11, 2016


import random
from sys import exit

def again():
	print "Play again?"
	answer = raw_input("> Enter Y or N")
	
	if "Y" in answer or "y" in answer:
		Play()
		
	else:
		exit(1)	
		
def Play():
	number = random.randrange(1,100)
	#print number
	tries = 0
	win = False
	
	while True and tries < 10:
		
		guess = raw_input("Enter a number  ")
		guess = int(guess) #This is very important!!!
		tries += 1
		
		if guess == number:
			print "You win!"
			win = True
			break
			
		elif guess < number:
			print "too low"
			win = False
			
		elif guess > number:
			print "too high"
			win = False
			
		else:
			print "I don't understand."
			
	if guess == number:
		print "It took you %s tries." % tries
		again()
		
	else:
		print "Better luck next time!"
		again()
		
print "Hello! Welcome to the number guessing game!"		
print "You have 10 tries to guess a randomly generated number between 1 and 100."
print "After each guess, you will receive a hint."
print "Let's begin!\n"
Play()						