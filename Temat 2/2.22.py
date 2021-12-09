
import random

throw = random.randrange(1, 7)

user_guess = int(input('Enter your guess: '))

print(throw == user_guess)