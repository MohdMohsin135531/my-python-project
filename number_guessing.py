from random import randint

random_number = randint(1, 10)
guess_count = 0
while True:  
    try:
            guess = int(input("Guess the number between 1 and 10: "))
            if 1 <= guess <= 10:
                guess_count += 1
            break
    except ValueError:
            print("Please enter a valid number")
while guess != random_number:
    if guess > 10 or guess < 1:
        print("Please make a guess between 1 and 10")
    elif guess < random_number:
        print("Too low")  
    else:
        print("Too high")

    while True:
        try:
                guess = int(input("Guess the number between 1 and 10: "))
                if 1 <= guess <= 10:
                    guess_count += 1
                break
        except ValueError:
                print("Please enter a valid number")
            
if guess_count == 1:
    print(f"You won in {guess_count} guess!")
else:
    print(f"You won in {guess_count} guesses!")
