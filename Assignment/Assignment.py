import numpy as np
def game_core_v3(number: int = 1) -> int:
    """
    Args:В данном подходе будет использовать не метод "тыка наугад",
    а начнем с середины заданного диапазона и будем двигать ее в нужную сторону

        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Установим наш счетчик с 0
    count = 0
    # установим верхнюю и нижнюю границы (заданы по заданию)
    low = 1
    high = 100
    # Воспользуемся итерацией, которая будет работать до нахождения нашего
    # рандомного числа
    while True:
        # Прибавлям в переменную попытку
        count += 1
        # Берем среднее от наших границ (экстремумов)
        predict = (low + high) // 2
        # Если нашли - выводим номер попытки
        if predict == number:
            return count
        # Если ответ ниже выше нашей границы - двигаем ее верх на 1
        elif predict < number:
            low = predict + 1  # Сдвигаем нижнюю границу
        # Если ниже - двигаем вниз на 1
        else:
            high = predict - 1  # Сдвигаем верхнюю границу

           
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)