# 1
for messages_count in range(6):
    if messages_count > 0:
        print(f'Новых сообщений: {messages_count}')
    else:
        print('У вас нет сообщений')
        
# 2 
for current_hour in range(24):
    if current_hour < 12:
        print('Сейчас', current_hour, 'часов! Доброе утро!')
        
# 3
for current_hour in range(24):
    if current_hour < 12:
        print('Сейчас', current_hour, 'часов! Доброе утро!')
    else:
        print('Сейчас', current_hour, 'часов! Добрый день!')

# 4 
for beaufort in range(8):
    if beaufort == 0:
        print('Штиль')
    elif beaufort == 1:
        print('Тихий ветер')
    elif beaufort == 2:
        print('Лёгкий ветер')
    elif beaufort == 3:
        print('Слабый ветер')
    elif beaufort == 4:
        print('Умеренный ветер')
    elif beaufort == 5:
        print('Свежий ветер')
    elif beaufort == 6:
        print('Сильный ветер')
    elif beaufort == 7:
        print('Шторм')
        
# 5
for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас 1 новое сообщение')
    elif 2 <= messages_count <= 4:
        print('У вас', messages_count, 'новых сообщения')
    else:  
        print('У вас', messages_count, 'новых сообщений')
        
# 6
for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")
    if current_hour < 6:
        print("Доброй ночи!")
    elif current_hour < 12:
        print("Доброе утро!")
    elif current_hour < 18:
        print("Добрый день!")
    elif current_hour <= 23:
        print("Добрый вечер!")
    else:
        print("Доброй ночи!") 
        
# 7
for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")
    if current_hour >= 6 and current_hour <= 11:
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour <= 17:
        print('Добрый день!')
    elif current_hour >= 18 and current_hour <= 22:
        print('Добрый вечер!')
    elif current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')
        
# 8
good_boy = True  # мальчик-то неплохой
if not good_boy:
    print('Этот в грязь полез')
    print('и рад,')
    print('что грязна рубаха.')
    print('Про такого говорят:')
    print('он плохой, неряха.')
else:
    print('Этот чистит валенки,')
    print('моет сам галоши.')
    print('Он хотя и маленький,')
    print('но вполне хороший.')
    
# 9
# 1)
milk = True
cereals = False
eggs = True
if milk or cereals or eggs:
    if eggs:
        if milk:
            breakfast = '- омлет'
        else:
            breakfast = '- яичница'
    else:
        breakfast = '- хлопья с молоком'
else:
    if milk:
        breakfast = '- стакан молока'
    elif cereals:
        breakfast = 'можно погрызть сухих хлопьев'
    else:
        breakfast = 'ничего не будет: разгрузочный день'
print('Сегодня на завтрак', breakfast)

# 2)
milk = False
cereals = False
eggs = True
if milk or cereals or eggs:
    if eggs:
        if milk:
            breakfast = '- омлет'
        else:
            breakfast = '- яичница'
    else:
        breakfast = '- хлопья с молоком'
else:
    if milk:
        breakfast = '- стакан молока'
    elif cereals:
        breakfast = 'можно погрызть сухих хлопьев'
    else:
        breakfast = 'ничего не будет: разгрузочный день'
print('Сегодня на завтрак', breakfast)

# 3)
milk = False
cereals = False
eggs = False
if milk or cereals or eggs:
    if eggs:
        if milk:
            breakfast = '- омлет'
        else:
            breakfast = '- яичница'
    else:
        breakfast = '- хлопья с молоком'
else:
    if milk:
        breakfast = '- стакан молока'
    elif cereals:
        breakfast = 'можно погрызть сухих хлопьев'
    else:
        breakfast = 'ничего не будет: разгрузочный день'
print('Сегодня на завтрак', breakfast)