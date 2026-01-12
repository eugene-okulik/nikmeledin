def deco_calc(func):
    def wrapper(first, second, operation):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif second > first:
            return func(second, first, '/')
        elif first < 0 or second < 0:
            return func(first, second, '*')
    return wrapper


@deco_calc
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        if second != 0:
            return first / second
        else:
            return "Ошибка: деление на ноль"


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

result = calc(num1, num2, None)
print("Результат:", result)
