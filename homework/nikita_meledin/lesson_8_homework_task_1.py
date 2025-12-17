import random

salary = int(input("Enter the salary: "))
bonus = random.choice([True, False])

if bonus:
    bonus_random = random.randint(1, 10000)
    salary_new = salary + bonus_random
    print(f"{salary}, {bonus} - ${salary_new}")
else:
    print(f"{salary}, {bonus} - ${salary}")
