HELP = """""
help - напечаать справку по
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""""


today = []
tomorrow = []
other = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(today, tomorrow, other)
    elif command == "add":
        date = input("Введите дату: ")
        task = input("Введите название задачи: ")
        if command == "Сегодня":
            today.append(date)
        elif command == "Завтра":
            tomorrow.append(date)
        else:
            other.append(date)
        print("Задаче добавлена")
    elif command == "exit":
        print("Спасибо за использование!")
        break
    else:
        print("Неизвестная команда")
        break
print("Пока!")
