a = range(1, 101)
for num in a:
    if num % 15 == 0:
        print('FuzzBuzz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3 == 0:
        print('Fuzz')
    else:
        print(num)
