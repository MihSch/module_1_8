#Условный оператор. Как работает оператор if  elif else
#name = input('введи имя: ')
#if name == 'urban' :            # = - присвоение ==-проверка на равенство
#    print('ку, админ')
#if name == 'Мих':
#    print('шалом')         #:-заканчиваем условие, отступом обозначаем то что команды
#else:                                # относятся к определенным частям кода
#    print('привет', name)           #if-условие   если
                            #else сработает если не сработает комманда if
                            #ЗАДАЧА ФИЗ
#number = int(input('Введи число: ')) # если число дел на 3 то вывод fizz,
# если на 5 вывод buzz,если и то и то то fizzbuzz
#if number % 3 == 0 and number % 5 == 0:
#    print('FizzBuzz')
#elif number % 5 == 0:
 #   print('Buzz') # or не строгий либо - and строгий и то и то
    #самое маловероятное помещаем в начало где if
#elif number % 3 == 0:
#    print('Fizz')
#else:
#    print('число не подходит')


#ЗАДАЧА
first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))
if first == second == third:
    print(3)
elif first == second or third == second or first == third:
    print(2)
elif first != second != third:
    print(0)
else:
    print('Число не подходит!')

