ITEMS_NAMES = (
  'Меч',
  'Кирка',
  'Лук',
  'Посох',
  'Копьё',
  'Катана',
  'Кинжал',
  'Секира',
  'Копьё',
)

class Thing:
  
  def __init__(self, name, health, attack, protection_percent) -> None:
    self.name = name
    self.health = health
    self.attack = attack
    self.protection_percent = protection_percent

  def __str__(self) -> str:
    return (f'{self.name} добавляет владельцу {self.health} здоровья,'
            f'{self.attack} атаки и {self.protection_percent} процентов защиты')