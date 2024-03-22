from characters import Ork, Elf
from relics import HealthPotion, StoneSkinPotion
import time


def fight(*, character_1: 'Character', character_2: 'Character') -> None:
    while character_1.health > 0 and character_2.health > 0:
        character_1.attack_target(character_2)
        character_2.attack_target(character_1)
        print(f'The {character_1.name} has {character_1.health} hp left')
        print(f'The {character_2.name} has {character_2.health} hp left')
        if character_1.health <= 30:
            character_1.use_health_potion()
        if character_2.health <= 30:
            character_2.use_health_potion()
        if character_1.health <= 40:
            character_1.use_stone_skin_potion()
        if character_2.health <= 40:
            character_2.use_stone_skin_potion()
        time.sleep(2)


ork = Ork(name='Orche', level=1)
elf = Elf(name='Legolas', level=1)
print(ork.defence_percentage)
potion = HealthPotion(name='Potion', count=2)
potion_2 = StoneSkinPotion(name='Stone Skin Potion', count=1)
ork.add_to_inventory(item=potion)
elf.add_to_inventory(item=potion)
ork.add_to_inventory(item=potion_2)
elf.add_to_inventory(item=potion_2)
fight(character_1=ork, character_2=elf)
