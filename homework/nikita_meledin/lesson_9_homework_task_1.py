temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32,
                34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
                29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

while True:
    temperatures_hot = list(filter(lambda x: x >= 28, temperatures))

    average = sum(temperatures_hot) / len(temperatures_hot)
    print(f'Минимальная температура: {min(temperatures_hot)}')
    print(f'Максимальная температура: {max(temperatures_hot)}')
    print(f'Средняя температура: {round(average, 2)}')
    break
    