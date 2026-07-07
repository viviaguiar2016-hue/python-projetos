#este é um jogo adivinhar o número
import random
secretNumber= random.randint(1,20)
print('I am thinking of a number between 1 and 20')

#peça para o jogador adivinhar 6 vezes. 
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess= int(input())

    if guess < secretNumber:
        print('your guess is too low')
        
    elif guess > secretNumber:
        print('your guess is to high')
    else:
        break  #Essa condição corresponde o  palpite correto!


if guess== secretNumber:
    print('Good job! you guessed myb number in'+str(guessesTaken)+ 'guesses')
else:
    print('Nope the number i was thinking of was'+str(secretNumber))
