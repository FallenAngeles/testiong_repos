import time # подключаем либу с временем
from datetime import datetime # из либы datetime подключаем класс datetime
import random # подключаем библиотеку рандом

odds = [] # создаем пустой список под названием odds
for vadim in range(60): # объявляем цикл for с конечным числом 60
    if vadim % 2 != 0: # проверяем число с именем Вадим на нечетность
        odds.append(vadim) # добавляем значение Вадима в список odds

for akbar in range(5): # объявляем цикл for c переменной Акбар
    right_this_second = datetime.today().second # Получаем переменную second из метода класса datetime и кладем в переменную right_this_second
    if right_this_second in odds: # проверили текущую секунду на нечетность
        print(datetime.today().strftime('%H:%M:%S'), ' Это нечетная секунда!')
    else: # в ином случае пишем, что секунда четная
        print(datetime.today().strftime('%H:%M:%S'), ' Это четная секунда.')
    wait_time = random.randint(0, 5) # кладем случайное число в переменную wait_time
    time.sleep(wait_time) 