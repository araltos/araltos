import random
count=0
play_again = "YES"

while play_again.upper() == 'YES':
    number = random.randint(1, 100)
    guess = None
    magic_num = None
    magic_num = number      
    while guess != magic_num:
        count += 1 
        guess = int(input("What is your guess? "))
        if guess < magic_num:
            print('Higher')
        elif guess > magic_num:
            print('Lower')
        else:
            print('You guess it!')
    print('Congratulations! You guessed the secret number in', count, 'guesses.')
    play_again = input("Do you want to play again? (YES/NO): ")
print('\nThank you for playing!')

