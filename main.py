from random import randint, choice, sample

from colorama import Fore, init, Back

import person
import thing

init(autoreset=True)

MAX_PERSONS = 10
MIN_HP_AVAILABLE = 100
MAX_HP_AVAILABLE = 200
MIN_ATTACK_AVAILABLE = 10
MAX_ATTACK_AVAILABLE = 20
MIN_PROTECTION_PERCENT_AVAILABLE = 0
MAX_PROTECTION_PERCENT_AVAILABLE = 10

MAX_ITEMS = 40
MIN_ITEMS_PER_PERSON = 0
MAX_ITEMS_PER_PERSON = 4

def generate_persons(things_list):
  
  persons_list = []
  
  for _ in range(MAX_PERSONS):
    persons_class = choice([person.Paladin, person.Warrior, person.Rogue])
    name = sample(person.NAMES, k=MAX_PERSONS)
    
    new_person = persons_class(name=name.pop(), 
      health=randint(MIN_HP_AVAILABLE, 
                     MAX_HP_AVAILABLE), 
      attack=randint(MIN_ATTACK_AVAILABLE, 
                     MAX_ATTACK_AVAILABLE), 
      protection_percent=randint(MIN_PROTECTION_PERCENT_AVAILABLE,
                                MAX_PROTECTION_PERCENT_AVAILABLE))

    new_person_items = [choice(things_list) for _ 
                        in range(randint(MIN_ITEMS_PER_PERSON, MAX_ITEMS_PER_PERSON))]
    
    new_person.set_things(new_person_items)
    print(Fore.MAGENTA + f'{new_person}')
    print()
    persons_list.append(new_person)

  return persons_list
    

def generate_items():
  
  things_list = []
  
  for _ in range(MAX_ITEMS):
    thing_person = thing.Thing(name=choice(thing.ITEMS_NAMES),
                               health=randint(MIN_HP_AVAILABLE, 
                                             MAX_HP_AVAILABLE),
                               attack=randint(MIN_ATTACK_AVAILABLE,
                                              MAX_ATTACK_AVAILABLE),
                               protection_percent=randint(MIN_PROTECTION_PERCENT_AVAILABLE,
                                                          MAX_PROTECTION_PERCENT_AVAILABLE))
    print(Fore.CYAN + f'{thing_person}')
    print()
    things_list.append(thing_person)
    
  things_list.sort(key=lambda x: x.protection_percent)
  return things_list


def main():
  things_list = generate_items()
  persons_list = generate_persons(things_list)
  while len(persons_list) > 1:
    print(f'Список участников: {", ".join([person.name for person in persons_list])}')
    attack_person, protect_person = sample(persons_list, k=2)
    protect_person.health_loss(attack_person.attack)
    print(Fore.RED + f'{attack_person.name} атакует {protect_person.name} '
          f'и наносит ему {attack_person.attack} урона')
    print(Fore.YELLOW + f'У {protect_person.name} осталось {protect_person.health}')
    if protect_person.health <= 0:
      print(Fore.BLACK + Back.WHITE + f'{protect_person.name} умер')
      print()
      persons_list.remove(protect_person)
  print()
  print(Fore.GREEN + f'Победил {persons_list[0].name}')
  with open("results.txt", "w") as file:
    file.write(f'Победил {persons_list[0].name}')
    file.close()
  print()

if __name__ == '__main__':
  main()