def process_line(line):
    position = line.index(':') + 2
    number_str = line[position:]
    number = int(number_str)
    print(number + 10)


lines = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]


for line in lines:
    process_line(line)
