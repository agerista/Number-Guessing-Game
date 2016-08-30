# Computer guesses number game written on June 17, 2016
		
def Play():

	step = .5
	numGuesses = 0
	low = 0
	high = 100
	guess = 50
	#number = raw_input("Enter a number between 1 and 100   ")
	
	while guess!= "c":
		
		print "Is your secret number %s?" % guess
		print "Enter 'h' to indicate the guess is too high.",
		print "Enter 'l' to indicate the guess is too low." 
		print "Enter 'c' to indicate I guessed correctly.",
		response = raw_input(" ")
		
		if response == "h":
			high = guess
			guess = (high + low) * step
			guess = int(guess)
			#print guess 
			#print ("low = " + str(low) + " high = " + str (high))
			#numGuesses += 1
			
		elif response == "l":
			low = guess
			guess = (high + low) * step
			guess = int(guess)
			#print guess 
			#print ("low = " + str(low) + " high = " + str (high))
			#numGuesses += 1
			
		elif response == "c":
			break
				
						
		else:
			print "Sorry, I did not understand your input."
			print "Enter 'h' to indicate the guess is too high.",
			print "Enter 'l' to indicate the guess is too low." 
			print "Enter 'c' to indicate I guessed correctly.",
			response = raw_input(" ")	
			
	print "Game over. Your secret number was: %s" % guess		
			
		#print ("numGuesses = " + str(numGuesses))
					
	
		
			

print "Please think of a number between 0 and 100!"
Play()						