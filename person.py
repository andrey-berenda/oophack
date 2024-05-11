
NAMES = (
  'Сева',
  'Серафим',
  'Аркадий',
  'Юрий',
  'Игорь',
  'Варфоломей',
  'Леонид',
  'Давид',
  'Августин',
  'Аполлон',
  'Владилен',
  'Моисей',
  'Иннокентий',
  'Дементий',
  'Артём',
  'Эдуард',
  'Арсений',
  'Арнольд',
  'Елисей',
  'Ярослав'
)

class Person:

  class_name = 'Person'
  
  def __init__(self, name, health, attack, protection_percent):
    self.name = name
    self.health = health
    self.attack = attack
    self.protection_percent = protection_percent
    self.items = []
  
  def set_things(self, things):
    self.items.extend(things)
    for thing in self.items:
      self.health += thing.health
      self.attack += thing.attack
      self.protection_percent += thing.protection_percent
    

  def health_loss(self, damage):
    additional_protection = 0
    for item in self.items:
      additional_protection += item.protection_percent
    self.health -= int(damage * (1 - self.protection_percent / 100))

  def __str__(self) -> str:
    return (f'{self.class_name} {self.name} имеет {self.health} здоровья, '
            f'{self.attack} атаки и {self.protection_percent} процентов защиты, '
            f'а так же следующие предметы: '
            f'{", ".join([item.name for item in self.items])}')

class Paladin(Person):

  class_name = 'Паладин'

  def __init__(self, name, health, attack, protection_percent):
    super().__init__(name, health*2, attack, protection_percent*2)


class Warrior(Person):

  class_name = 'Воин'

  def __init__(self, name, health, attack, protection_percent):
    super().__init__(name, health, attack*2, protection_percent)

class Rogue(Person):

  class_name = 'Разбойник'
  
  def __init__(self, name, health, attack, protection_percent):
    super().__init__(name, int(health*0.5), attack*4, protection_percent)
  