'''
Decorators:

1. Під мостом завівся Троль, який систематично і бездушно забирає плату за прохід мостом
Оскільки ми проти расизму, то допоможемо Тролю правильно забирати кошти в людей.
Створіть декоратор Troll, та застосуйте його до функції bridge, по якій ходять люди Person.
За прохід по мосту в них віднімаються кошти, якщо їх достатньо.
Якщо ні, то TrollIsAngry exception не дасть людині перейти міст!
'''

class Troll_is_angry(Exception):
    pass

class Person:
    def __init__(self, money):
        self.money = money

def trol(func):
    Trol_tax = 50
    def inner(*args, **kwargs):
        person = args[0]
        if person.money > Trol_tax:
            person.money -= Trol_tax
        else:
            raise Troll_is_angry
        return person.money
    return inner
@trol
def bridge(person: Person):
    print(f"Person passed the bridge with money {person.money}")
    return

if __name__ == "__maine__":
    v = Person(300)
    bridge(v)