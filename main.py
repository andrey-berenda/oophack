from random import randint, sample

BASE_HPS = 20
BASE_ATACK = 10
BASE_DEFENCE = 100  # PERCENTS %


class Thing:
    def __init__(self, name, defence_percent, attack, health):
        self.name = name
        self.defence_percent = defence_percent
        assert defence_percent < BASE_DEFENCE
        self.attack = attack
        self.health = health


class Person:
    def __init__(self, name):
        self.name = name
        self.count_hp_life = BASE_HPS
        self.base_attack = BASE_ATACK
        self.base_defence = BASE_DEFENCE
        self.things_of_person = []

    def set_things(self, things):
        count_of_things = randint(1, 4)
        # i = 0
        # while i < count_of_things:
        #  self.things_of_person.append(choice(things))
        # i += 1
        return sample(things, count_of_things)
        # return self.things_of_person

    def life_damage(self, damage):
        self.count_hp_life -= damage

    def attack_damage(self):
        damage = self.base_attack
        for thing in self.things_of_person:
            damage += thing.attack
        return damage


class Paladin(Person):
    def __init__(self, name):
        super().__init__(name)
        self.count_hp_life = self.count_hp_life * 2
        self.base_defence_percent = self.base_defence * 2


class Warrior(Person):
    def __init__(self, name):
        super().__init__(name)
        self.base_atack = self.base_attack * 2


def main():
    # Количество игроков
    NUMBER_OF_PLAYERS = 10

    # ШАГ 0. СОЗДАНИЕ СПИСКА 20 РАНДОМНЫХ ИМЕН
    NAMES = [
        'Kylie',
        'Bob',
        'Dave',
        'Lala',
        'Jordan',
        'Ohio',
        'Kyle',
        'Sherly',
        'Tom',
        'Sam',
        'Ron',
        'Soup',
        'Kaka',
        'Sale',
        'Ivan',
        'Bogdan',
        'Kolya',
        'Dima',
        'Genius',
        'Papa'
    ]

    # ШАГ 1. СОЗДАНИЕ ПРОИЗВОЛЬНОГО КОЛ-ВА ВЕЩЕЙ С ЗАЩИТА < 10%
    THINGS = [
        Thing('Sword', 5, 20, 100),
        Thing('Hamlet', 8, 0, 50),
        Thing('Armor', 10, 0, 80),
        Thing('Shield', 7, 0, 70),
        Thing('Belt', 3, 0, 30)
    ]
    THINGS = sorted(THINGS, key=lambda x: x.defence_percent)
    # ШАГ 2. СОЗДАНИЕ СПИСКА 10 ОБЪЕКТОВ ПЕРСОНАЖЕЙ
    #        (5 ВОИНОВ, 2 ПАЛАДИНА, 3 ОБЫЧНЫХ ЖИТЕЛЯ)
    names = sample(NAMES, NUMBER_OF_PLAYERS)
    # count_of_palladins = randint(1, NUMBER_OF_PLAYERS // 2))
    paladins = [
        Paladin(names[0]),
        Paladin(names[1]),
    ]
    warriors = [
        Warrior(names[2]),
        Warrior(names[3]),
        Warrior(names[4]),
        Warrior(names[5]),
        Warrior(names[6]),
        Warrior(names[7]),
        Warrior(names[8]),
        Warrior(names[9]),
    ]
    players = paladins + warriors

    # ШАГ 4. ОДЕВАЕМ ПЕРСОНАЖЕЙ ВЕЩАМИ (от 1 до 4 вещи)
    # ИГРA
    p = Paladin('Kylie')
    k = Warrior('Sam')
    p.set_things(THINGS)
    k.set_things(THINGS)
    players = [p, k]

    while len(players) > 1:
        attacker = players[0]
        defender = players[1]
        # {атакующий персонаж} наносит удар по {защищающийся персонаж} на {кол-во урона} урона
        defender.life_damage(attacker.attack_damage())

        print(f'{attacker.name} атакует {defender.name} на {attacker.attack_damage()}')

        if defender.count_hp_life <= 0:
            players.remove(defender)

        attacker, defender = defender, attacker


if __name__ == "__main__":
    main()



