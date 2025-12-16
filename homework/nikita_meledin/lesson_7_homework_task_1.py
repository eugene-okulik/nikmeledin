import random

random_number = random.randint(1, 100)

while True:
    your_number = int(input("Guess a number from 1 to 100: "))
    if your_number == random_number:
        print("You guessed right!")
        break
    else:
        while True:
            question = input('Try again... Yes/No: ').strip().lower()
            if question == 'no':
                print("Okay, goodbye!")
                exit()
            elif question == 'yes':
                break
            else:
                print('Input error. Please enter "Yes" or "No".')
