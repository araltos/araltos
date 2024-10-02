import random

word_list = ["mosiah", "alma", "helaman", "nephi", "moroni"]
secret = random.choice(word_list)

hint = ['_'] * len(secret)
guesses = 0

print('Welcome to the word-guessing game!')
print(f'Your hint is: {" ".join(hint)}')

while hint != list(secret):
    guess = input('What is your guess? ')
    guesses += 1

    if len(guess) != len(secret):
        print('Sorry, the guess must have the same number of letters as the secret word.')
    else:
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                hint[i] = guess[i]
            elif guess[i] in secret:
                hint[i] = guess[i].lower()

        print(f'Your updated hint is: {" ".join(hint)}')

print(f'Congratulations! You guessed the whole word: {secret}')
print(f'It took you {guesses} guesses.')
