# Задание: Известны год, номер месяца и день рождения каждого из двух человек. Определить, кто из них старше.

UserYear1 = int(input("Введите ваш год рождения человек 1: "))
UserMonth1 = int(input("Введите ваш месяц рождения человек 1 (числом): "))
UserDay1 = int(input("Введите ваш день рождения человек 1: "))

UserYear2 = int(input("Введите ваш год рождения человек 2: "))
UserMonth2 = int(input("Введите ваш месяц рождения человек 2 (числом): "))
UserDay2 = int(input("Введите ваш день рождения человек 2: "))


from datetime import date

today = date.today()

if today.month == UserMonth1 and today.month == UserDay1 or today.month > UserMonth1 and today.day > UserDay1 or today.month > UserMonth1 and UserDay1 < today.day or today.month == UserMonth2 and today.month == UserDay2 or today.month > UserMonth2 and today.day > UserDay2 or today.month > UserMonth2 and UserDay2 < today.day:
    Age1 = today.year - UserYear1
    Age2 = today.year - UserYear2
    if Age1 > Age2:
        if UserDay1 < today.day:
            print("Человек 1.1 старше, ему:", Age1-1, "лет. Человеку 2 -", Age2, "лет")
        else:
            print("Человек 2.1 старше, ему:", Age2, "лет. Человеку 2 -", Age1-1, "лет")
    elif Age2 > Age1:
        if UserDay2 < today.day:
            print("Человек 1.2 старше, ему:", Age2-1, "лет. Человеку 1 -", Age1, "лет")
        else:
            print("Человек 2.2 старше, ему:", Age1, "лет. Человеку 1 -", Age2-1, "лет")
    elif UserYear1 == UserYear2 and UserMonth1 == UserMonth2 and UserDay1 > UserDay2:
        print("Человек 2 старше Человека 1, но у них одинаково количество лет", Age2 or Age1)
    elif UserYear2 == UserYear1 and UserMonth2 == UserMonth1 and UserDay2 > UserDay1:
        print("Человек 1 старше Человека 2, но у них одинаково количество лет", Age1 or Age2)

elif UserMonth1 > today.month and UserDay1 > today.day or UserMonth1 > today.month and UserDay1 < today.day or UserMonth2 > today.month and UserDay2 > today.day or UserMonth2 > today.month and UserDay2 < today.day:
    Age1 = today.year - UserYear1
    Age2 = today.year - UserYear2
    if Age1 > Age2:
        print("Человек 1.1.1 старше, ему на данный момент:", Age1-1, "лет. Человеку 2 -", Age2, "лет")
    elif Age2 > Age1:
        print("Человек 2.2.1 старше, ему на данный момент:", Age2-1, "лет. Человеку 1 -", Age1, "лет")
    elif UserYear1 == UserYear2 and UserMonth1 == UserMonth2 and UserDay1 > UserDay2:
        print("Человек 2 старше Человека 11, но у них одинаково количество лет", Age2-1 or Age1)
    elif UserYear2 == UserYear1 and UserMonth2 == UserMonth1 and UserDay2 > UserDay1:
        print("Человек 1 старше Человека 22, но у них одинаково количество лет", Age1-1 or Age2)