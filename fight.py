from characters import Creature, Ork, Elf
from relics import HealthPotion, StoneSkinPotion, Diadem, Sword, Bow, Armour
import time


def fight(*, character_1: 'Creature', character_2: 'Creature') -> None:
    while character_1.health > 0 and character_2.health > 0:
        character_1.attack_target(character_2)
        character_2.attack_target(character_1)
        print(f'The {character_1.name} has {character_1.health} hp left')
        print(f'The {character_2.name} has {character_2.health} hp left')
        if character_1.health <= 30:
            character_1.use_potion(potion_name='Health Potion')
        if character_2.health <= 30:
            character_2.use_potion(potion_name='Health Potion')
        if character_1.health <= 40:
            character_1.use_potion(potion_name='Stone Skin Potion')
        if character_2.health <= 40:
            character_2.use_potion(potion_name='Stone Skin Potion')
        time.sleep(0)
    if character_1.health <= 0 and character_2.health <= 0:
        print(f'The {character_1.name} and the {character_2.name} both dead. RIP!')
        return
    if character_1.health <= 0:
        print(f'The {character_1.name} is dead, {character_2.name} wins!')
    if character_2.health <= 0:
        print(f'The {character_2.name} is dead, {character_1.name} wins!')


def prepare_to_fight():
    ork = Ork(name='Orche', level=1, kind='Character')
    elf = Elf(name='Legolas', level=1, kind='Character')
    potion = HealthPotion(name='Health Potion', count=2)
    potion_2 = StoneSkinPotion(name='Stone Skin Potion', count=1)
    diadem = Diadem(name='Diadem', count=1)
    sword = Sword(name='Sword', count=1)
    bow = Bow(name='Bow', count=1)
    armour = Armour(name='Armour', count=1)
    ork.add_to_inventory(item=potion)
    ork.add_to_inventory(item=sword)
    elf.add_to_inventory(item=potion)
    ork.add_to_inventory(item=potion_2)
    elf.add_to_inventory(item=potion_2)
    ork.add_to_inventory(item=diadem)
    elf.add_to_inventory(item=diadem)
    elf.add_to_inventory(item=bow)
    ork.add_to_inventory(item=armour)
    elf.add_to_inventory(item=armour)
    ork.equip(item=diadem)
    ork.equip(item=sword)
    elf.equip(item=diadem)
    elf.equip(item=bow)
    ork.equip(item=armour)
    elf.equip(item=armour)
    return elf, ork


elf1, ork1 = prepare_to_fight()

fight(character_1=ork1, character_2=elf1)
