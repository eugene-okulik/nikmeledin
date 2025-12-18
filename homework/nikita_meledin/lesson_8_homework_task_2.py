import sys

sys.set_int_max_str_digits(1000000)


def fibonacci_generator():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


fib_gen = fibonacci_generator()

for _ in range(4):
    five_number = next(fib_gen)

for _ in range(200):
    two_hundred_number = next(fib_gen)

for _ in range(1000):
    thousand_number = next(fib_gen)

for _ in range(100000):
    hundred_thousand_number = next(fib_gen)

print(five_number)
print(two_hundred_number)
print(thousand_number)
print(hundred_thousand_number)
