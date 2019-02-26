# Guessing Game Challenge
# Let's use while loops to create a guessing game.

# The Challenge:

# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

# If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# On a player's first turn, if their guess is
# within 10 of the number, return "WARM!"
# further than 10 away from the number, return "COLD!"
# On all subsequent turns, if a guess is
# closer to the number than the previous guess return "WARMER!"
# farther from the number than the previous guess, return "COLDER!"
# When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
# You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!

# First, pick a random integer from 1 to 100 using the random module and assign it to a variable
# Note: random.randint(a,b) returns a random integer in range [a, b], including both end points.
from random import randint

random_int = randint(1, 100)
print('secret:', random_int)
print('Pick a number between 1 and 100 and I\'ll tell you if you\'re close!')

guesses = [0]

while guesses[-1] != random_int:
  guess = int(input('=> '))

  if guess == random_int: 
    print('You guessed it!')
  elif len(guesses) == 1:
    if guess <= random_int + 10 and guess >= random_int - 10: 
      print('WARM')
    else:
      print('COLD')
  else:
    currDistance = abs(random_int - guess)
    prevDistance = abs(random_int - guesses[-1])
    if currDistance < prevDistance:
      print('WARMER')
    else: 
      print('COLDER')
  guesses.append(guess)
