# Создаём пустой словарь для манипулирования контактами
contacts = {}

# Создаем логику для добавления контакта с использованием функции
def add_contact(name, phone):
    if name in contacts:
        print(f"Контакт с именем {name} уже существует!")
    else:
        contacts[name] = phone
        print(f"Контакт {name} добавлен(а).")

# Создаем логику для обновления контакта с использованием функции
def update_contact(name, new_phone_num):
    if name in contacts:
        contacts[name] = new_phone_num
        print(f"Контакт {name} обновлен(а).")
    else:
        print(f"Контакт {name} не найден.")

# Создаем логику для удаления контакта с использованием функции
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Контакт {name} удален(а).")
    else:
        print(f"Контакт {name} не найден.")

# Создаем логику для отображения контакта(ов) с использованием функции
def display_contacts():
    print("\n Список контактов: " if contacts else "Список контактов пуст.")
    for name, phone in contacts.items():
        print(f"📞 {name}: {phone}")

add_contact("Иван", "123456")
add_contact("Мария", "789101")
update_contact("Иван", "555555")
delete_contact("Мария")
display_contacts()  

Краткий конспект по лекции:

list.append() – добавляет элемент в конец списка.
list.remove(x) – удаляет первый найденный элемент x.
list.pop(i) – удаляет элемент с индексом i (по умолчанию – последний).
list.sort() – сортирует список.
list.reverse() – переворачивает список.