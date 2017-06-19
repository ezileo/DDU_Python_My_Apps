import random

print ('-------------------------------------------')
print ('           GUESS THE NUMBER GAME           ')
print ('-------------------------------------------')
print ()

player_name = input('Please Input your Name: ')
print ('Welcome to the Game ' + player_name)

the_number = random.randint(0, 100)

print(the_number, type(the_number))

guess = -1

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < the_number:
        #print("Your guess is too low, " + player_name + ",think of a bigger number")
        print('Your guess of {} is too low {}, think of a BIGGER number'.format(guess, player_name))

    elif guess > the_number:
        #print("Your guess is too high, " + player_name + ",think of a lower number")
        print('Your guess of {} is too high {}, think of a LOWER number'.format(guess, player_name))
    else:
        #print("You guessed the correct number, You win " + player_name)
        print('Congratulations {1}!!! You Win by guessing {0}'.format(guess, player_name))
