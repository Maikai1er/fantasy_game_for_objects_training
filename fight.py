from characters import Creature, Ork, Elf, Werewolf
from relics import HealthPotion, StoneSkinPotion, Diadem, Sword, Bow, Armour
import time


def fight(*, character_1: 'Creature', character_2: 'Creature') -> None:
    while character_1.health > 0 and character_2.health > 0:
        print(f'The {character_1.name} has {character_1.health} hp left')
        print(f'The {character_2.name} has {character_2.health} hp left')
        print('Possible actions: attack, heal, stone')
        action = input('Which action would you like to perform? ')
        match action:
            case 'attack':
                character_1.attack_target(character_2)
            case 'heal':
                character_1.use_potion(potion_name='Health Potion')
                # print(f'The {character_1.name} has used Health Potion and has '
                #       f'{character_1.inventory['Health Potion']['count']} left.')
            case 'stone':
                character_1.use_potion(potion_name='Stone Skin Potion')
                # print(f'The {character_1.name} has used Stone Skin Potion and has '
                # f'{character_1.inventory['Stone Skin Potion']['count']} left.')

        if character_2.kind == 'Character':
            potion_used = False
            if character_2.health <= 40:
                if character_2.use_potion(potion_name='Health Potion'):
                    time.sleep(1)
                    continue
                # print(f'The {character_2.name} has used Health Potion and has '
                #       f'{character_2.inventory['Health Potion']['count']} left.')

            if character_2.health <= 60:
                if character_2.use_potion(potion_name='Stone Skin Potion'):
                    time.sleep(1)
                    continue
                # print(f'The {character_2.name} has used Stone Skin Potion and has '
                #       f'{character_2.inventory['Stone Skin Potion']['count']} left.')

            character_2.attack_target(character_1)
            time.sleep(1)

    if character_1.health <= 0 and character_2.health <= 0:
        print(f'The {character_1.name} and the {character_2.name} both dead. RIP!')
        return
    if character_1.health <= 0:
        print(f'The {character_1.name} is dead, {character_2.name} wins!')
    if character_2.health <= 0:
        print(f'The {character_2.name} is dead, {character_1.name} wins!')
