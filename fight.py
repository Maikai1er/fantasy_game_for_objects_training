from ork_vs_elf import Ork, Elf
from relics_for_fight import HealthPotion
import time

def fight(*, character_1: 'Character', character_2: 'Character') -> None:
    while character_1.health > 0 and character_2.health > 0:
        character_1.attack_target(character_2)
        character_2.attack_target(character_1)
        print(f'The {character_1.name} has {character_1.health} hp left')
        if character_1.health <= 20:
            potion.use(self=potion, target=character_1)
        if character_2.health <= 20:
            potion.use(self=potion, target=character_2)
        print(f'The {character_2.name} has {character_2.health} hp left')
        time.sleep(1)


ork = Ork(name='Orche', level=1)
elf = Elf(name='Legolas', level=1)
potion = HealthPotion



fight(character_1=ork, character_2=elf)