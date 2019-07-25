import random as rd

rand = rd.randint(0,100)
count = 1

while count <= 3:
    guess = int(input('Guess what it is'))
    if guess > rand:
        print('Too big..')
    elif guess < rand:
        print('Too small...')
    else:
        print('Bingo! random number is', rand)
        break
    count += 1
else:
    print('You lose! random number is', rand)
