from random import randrange

# Предметы
items = ['ножницы', 'бумага', 'камень', 'ящерица', 'спок']

# Предметы в родительном падеже
right_ending_items = ['ножницы', 'бумагу', 'камень', 'ящерицу', 'Спока']


# Приветствие
def welcome():
    name = input('Введите ваше имя: ')
    print(f'Привет, {name}! Давайте сыграем с вами в камень-ножницы-бумага-ящерица-спок!')
    command = input('Чтобы начать игру, нажмите Enter. Если вы не знаете правила игры, напишите "правила": ')
    # Правила
    rules = '''
ПРАВИЛА:
Ножницы режут бумагу. Бумага заворачивает камень. Камень давит ящерицу, а ящерица травит Спока,
в то время как Спок ломает ножницы, которые, в свою очередь, отрезают голову ящерице, которая ест бумагу, 
на которой улики против Спока. Спок испаряет камень, а камень, разумеется, затупляет ножницы. '''
    # Проверка нажатия Enter'а
    while command:
        if command.lower() == 'правила':
            print(rules)
            print()
            command = input('Чтобы начать игру, нажмите Enter.')
        else:
            print('Не понял вас.')
            command = input('Чтобы начать игру, нажмите Enter. Если вы не знаете правила игры, напишите "правила": ')


# Основная часть игры
def game(comp_choice, player_choice):
    # Индексы выбранных предметов в списке
    player_index = items.index(player_choice)
    comp_index = items.index(comp_choice)
    # Выбор компьютера в правильном падеже
    comp_choice_right_ending = right_ending_items[comp_index]
    # Определение победителя
    if comp_index == player_index:
        print(f'Ничья! Я тоже выбрыл {comp_choice_right_ending}.')
        return 'tie'
    elif (player_index + 1) % 5 == comp_index or \
         (player_index + 3) % 5 == comp_index:
        print(f'Победа за вами, я выбрал {comp_choice_right_ending}.')
        return 'player'
    else:
        print(f'Ха-ха-ха, а я выбрал {comp_choice_right_ending} и победил!')
        return 'comp'


# Игра
def rock_paper_scissors_lizard_spock():
    welcome()
    results = {'tie': 0, 'player': 0, 'comp': 0}
    one_more_time = 'да'
    # Пока хочет играть
    while one_more_time.lower() == 'да':
        # Выбор компьютера
        comp_choice = items[randrange(5)]
        # Выбор игрока
        player_choice = input('Выберите ваш предмет: ').lower()
        # Проверка предмета
        while player_choice not in items:
            player_choice = input('Такой предмет нельзя выбрать. Попробуйте ещё раз: ')
        # Запуск игры и обновление результатов
        results[game(comp_choice, player_choice)] += 1
        # Ещё раз?
        one_more_time = input('Хотите сыграть ещё раз? ')
    # Итоги
    print(f'Итого:\nВаши победы: {results["player"]} \nМои победы: {results["comp"]} \nНичьи: {results["tie"]}')
    print('Спасибо за игру! До новых встреч!')


rock_paper_scissors_lizard_spock()
