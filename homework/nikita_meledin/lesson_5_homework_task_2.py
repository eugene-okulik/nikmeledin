result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'

number = 10
index_1 = result_1.index(':')
index_2 = result_2.index(':')
index_3 = result_3.index(':')

sum_1 = int(result_1[index_1 + 1:].strip())
sum_2 = int(result_2[index_2 + 1:].strip())
sum_3 = int(result_3[index_3 + 1:].strip())

print(sum_1 + number)
print(sum_2 + number)
print(sum_3 + number)
