# Este é um jogo de adivinhar o número.
# guessTheNumber = adivinhe o número

import random
secretNumber = random.randint(1, 20)
print('\n\tI am thinking of a number between 1 and 20.')

# Peça para o jogador adivinhar 6 vezes.

for guessesTaken in range(1, 7):
    # print('\n\tTake a guess.')
    guess = int(input('\n\tTake a guess 》》》   '))

    if guess < secretNumber:
        print('\n\tYour guess is too low.')
    elif guess > secretNumber:
        print('\n\tYour guess is too high.')
    else:
        break  # Esta condição corresponde ao palpite correto!
if guess == secretNumber:
    print('\n\tGood job! You guessed my number in ' +
          str(guessesTaken) + ' guesses!')
else:
    print('\n\tNope. The number I was thinking of was ' + str(secretNumber))
