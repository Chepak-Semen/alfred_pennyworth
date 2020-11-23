import random
import time

"""
_______________________________________________1____________________________________________
1. Під мостом завівся Троль, який систематично і бездушно забирає плату за прохід мостом
Оскільки ми проти расизму, то допоможемо Тролю правильно забирати кошти в людей.
Створіть декоратор Troll, та застосуйте його до функції bridge, по якій ходять люди Person. 
За прохід по мосту в них віднімаються кошти, якщо їх достатньо. 
Якщо ні, то TrollIsAngry exception не дасть людині перейти міст!
"""


class TrollIsAngry(Exception):
    pass


class Person():
    def __init__(self):
        self.money = random.randint(20, 50)
        print(f"Person has {self.money}")

    def lost_money(self, tax):
        print(f" Person lost {tax} money ")
        self.money -= tax
        return self.money

    def can_pay(self, tax):
        if self.money >= tax:
            print(f"Person can pay")
            return True


def troll(func):
    Troll_tax = 25

    def wraper(*args, **kwargs):
        person = args[0]
        if person.can_pay(Troll_tax):
            person.lost_money(Troll_tax)
        else:
            raise TrollIsAngry
        return func(*args, **kwargs)

    return wraper


@troll
def bridge(person: Person):
    print(f"Person passed the bridge with {person.money} money")
    return


"""
_______________________________________________2____________________________________________
Створіть декоратор (Timer), який засікає час роботу функції. Для створення декоратора використайте 
 adding a decorator to the function 
```
@Timer
def some_function(delay): 
    from time import sleep 

    # Introducing some time delay to  
    # simulate a time taking function. 
    sleep(delay) 
"""


class Timer:
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            t1 = time.time()
            result = func(*args, **kwargs)
            t2 = time.time() - t1
            print(f'{func.__name__} ran in: {t2} sec')
            print(f"{self.name} finished work")
            return result

        return wrapper


@Timer('timer_class')
def my_func(n):
    time.sleep(n)


'''
___________________________________________________3____________________________________________________________
3. recursion + factorial
Нашіть функцію, яка рекурсивно рахує факторіал, а заодно декоратор, який перевіряє чи вхідне значення ціле та позитивне число:
'''


def factorial(given_num):
    return factorial(given_num - 1) * given_num if given_num != 1 else given_num


'''
___________________________________________________4____________________________________________________________
Напишіть программу, яка виводить частину послідовності 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 .... 
 На вхід приймається значення n - кількість елементів послідовності, які мають бути виведенні 

Наприклад, якщо n = 7, то программа має вивести 1 2 2 3 3 3 4.
Sample Input:
7
Sample Output:
1 2 2 3 3 3 4
'''


def calc(numb: int):
    lst = []
    for i in range(1, numb + 1):
        a = 0
        while i != a:
            if len(lst) == numb:
                break
            a += 1
            lst.append(i)
    return lst


'''
___________________________________________________5____________________________________________________________
Напишіть програму, яка зчитує з консолі числа (по одному в строці) до тих пір,
пока сума сум введених чисел не буде рівною 0 і, відповідно, після цього виводить сумму квадратів усіх введених чисел.
У прикладі ми зчитуємо числа 1, -3, 5, -6, -10, 13; в цей момент помічаємо, що сума цих чисел рівна 0.
і виводим сумму їх квадратів зупиняючи зчитування з консолі.
Sample Input:
1
-3
5
-6
-10
13
4
-8
Sample Output:
340
'''


def s():
    l.append(int(input('input your numbers: ')))
    if sum(l) != 0:
        s()
    else:
        m = [i * i for i in l]
        print(f"Your sqr(sum) is {sum(m)}")


'''
___________________________________________________6____________________________________________________________
Одне із застосувань множинного успадкування - розширення функціональності класу якимось заздалегідь визначеним способом.
Наприклад, якщо нам знадобиться залогувати якусь інформацію при зверненні до методів класу.
Розглянемо класс Loggable:
```
import time
class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
```

У нього є рівно один метод log, який дозволяє виводити в лог (в даному випадку в stdout) якесь повідомлення,
додаючи при цьому поточний час.
Реалізуйте клас LoggableList, унаслідував його від класів list і Loggable таким чином,
щоб при додаванні елемента в список за допомогою методу append в лог відправлялося повідомлення, що складається з тількищо доданого елемента.
'''


class Loggable:
    def log(self, msg):
        print(f"{str(time.ctime())} : given element {str(msg)}")


class LoggableList(Loggable, list):

    def append(self, item):
        super().log(item)
        super().append(item)


'''
___________________________________________________7____________________________________________________________
Реалізуйте клас PositiveList, унаслідував його від класу list, для зберігання позитивних цілих чисел.
Також реалізуйте нове виключення NonPositiveError.
У класі PositiveList перевизначите метод append (self, x) таким чином, щоб при спробі додати
 непозитивним ціле число викликалося виключення  NonPositiveError і число не додавалося,
 а при спробі додати позитивне ціле число, число додавалося б як в стандартний list.
'''


class NonPositiveError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PositiveList(list):

    def append(self, x):
        if x > 0 and type(x) == int:
            super().append(x)
        else:
            raise NonPositiveError("Really?! Again?!")


if __name__ == "__main__":
    print('_____________________________1______________________________')
    vasia = Person()
    bridge(vasia)
    print('_____________________________2______________________________')
    my_func(0)
    print('_____________________________3______________________________')
    print(f"factorial = {factorial(5)}")
    print('_____________________________4______________________________')
    print(calc(20))
    print('_____________________________5______________________________')
    l = []
    s()
    print('_____________________________6______________________________')
    log_list = LoggableList([1, 2, 3])
    log_list.append(4)
    print('_____________________________7______________________________')
    num = PositiveList([])
    num.append(-5)
