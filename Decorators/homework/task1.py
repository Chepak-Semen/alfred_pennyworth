
class Trollisangry(Exception):
    pass

class Person:
    def __init__(self, money):
        self.money = money

    def lost_money(self, n):
        self.money -= n
        return self.money


def troll(giwen_func):
    trol_tax = 20
    def wraper(*args, **kwargs):
        person = args[0]
        if person.money >= trol_tax:
            person.lost_money(trol_tax)
        else:
            raise Trollisangry
        return giwen_func(*args, **kwargs)
    return wraper


@troll
def bridge(person: Person):
    print(f"Person passed the bridge with {person.money} money")
    return

if __name__ == '__main__':
    a = Person(30)
    bridge(a)

