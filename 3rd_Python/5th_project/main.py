import school_management # Подключаем файл с функциями управления учениками

while True: # Запускаем бесконечный цикл, чтобы программа работала непрерывно
    # Выводим меню
    choice = input("Выберите действие:\n"
               "1 - Добавить ученика\n"
               "2 - Удалить ученика\n"
               "3 - Редактировать ученика\n"
               "4 - Показать всех учеников\n"
               "5 - Выйти\n")
    if choice == "1":
        name = input("Введите имя ученика: ")
        class_name = input("Введите класс (например, 1А): ")
        result = school_management.add_student(name, class_name)
        print(result)
    elif choice == "2":
        name = input("Введите имя ученика, которого нужно удалить: ")
        result = school_management.remove_student(name)
        print(result)
    elif choice == "3":
        old_name = input("Введите текущее имя ученика: ")
        new_name = input("Введите новое имя (нажмите Enter, если не менять): ")
        new_class = input("Введите новый класс (нажмите Enter, если не менять): ")

        # Передаём None, если пользователь ничего не ввёл
        new_name = new_name if new_name.strip() != "" else None
        new_class = new_class if new_class.strip() != "" else None

        result = school_management.edit_student(old_name, new_name, new_class)
        print(result)

    elif choice == "4":
        school_management.show_students()

    elif choice == "5":
        print("Выход из программы. До свидания!")
        break

    else:
        print("Ошибка: выберите пункт от 1 до 5.")