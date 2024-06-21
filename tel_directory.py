# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, 
# номер телефона - данные, которые должны находитьсяв файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну изхарактеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программане должна быть линейной


# ph_book = ['Ivanov', 'Sidorov', 'Petrov', ' ',]

def work_with_phonebook():
	
    choice = show_menu() # 1-ая функция

    phone_book = read_txt('phon.txt')

    while (choice!=7):

        if choice==1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice == 3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
        elif choice == 4:
            lastname = input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice == 5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phon.txt',phone_book)


        choice = show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          '1. Отобразить весь правочник\n'
          '2. Найти абонента по фамилии\n'
          '3. Найти аобнента по номеру телефона\n'
          '4. Добавить абонента в справочник (изменить данные)\n'
          '5. Сохранить справочник в текстовом формате\n'
          '6. Закончить работу')
    choice = int(input())
    return choice





ph_book = [ ]
data = open('phon.txt', 'a')
data.writelines(ph_book)
data.close()

with open('phon.txt', 'w') as data:
    data.write('Ivanov, Ivan, 	111, description of Ivanov\n\n')
    data.write('Petrov, Petr, 	222 , description of Petrov\n\n')
    data.write('Rembo , John, 333 , description of Rembo\n\n')
    data.write('Smirnov, Vasya, 777, master of Python\n\n')

print()


way = 'file.txt'
data = open('file.txt', 'r', encoding='utf-8')
for line in data:
    print(line)
data.close


