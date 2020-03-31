import random

attempt = 0
dNum = random.randint(0,21)
not_in_range = range(0,21)

while attempt <= 5:

    try:
        user_guess = int(input('guess from 1-20: '))
    except ValueError:
        print("not a number")
        continue

    if user_guess == dNum:
        print('Correct!')
        break
    elif user_guess > dNum:
        print('LOWER!')
        attempt +=1
    elif user_guess < dNum:
        print('HIGHER!')
        attempt +=1
    elif attempt not in not_in_range:
        print("not in range")
        attempt +=1
    else:
        pass

print(f'You lost! the number was {dNum}')