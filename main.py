import random

attempt = 0
dNum = random.randint(0,20)
not_in_range = range(0,21)

while attempt <= 4:

    # check for int
    try:
        user_guess = int(input('guess from 1-20: '))
    except ValueError:
        print("not a number")
        attempt +=1
        continue

    if user_guess not in not_in_range:
        print('not in range')
        attempt +=1
    elif user_guess > dNum:
        print('LOWER!')
        attempt +=1
    elif user_guess < dNum:
        print('HIGHER!')
        attempt +=1
    elif user_guess == dNum:
        print(f'Correct! The number was {dNum}')
        break

if user_guess != dNum:
    print(f'BYE! The number was {dNum}')
else:
    pass
