import time

from create_character import create_character
from fight import fight
from relics import HealthPotion, StoneSkinPotion, Diadem, Sword, Bow, Armour


def run_game():
    print("Welcome to the Neverland, stranger")
    time.sleep(1)
    print("Firstly, you have to create a character")
    time.sleep(1)
    race = input("Races available: Ork, Elf. Please, select your race: ")
    time.sleep(1)
    name = input("Please enter your nickname: ")
    player_character = create_character(race, name)
    npc_character = create_character('Ork', 'Orche')
    time.sleep(1)
    print("Let the battle begin!")

    potion = HealthPotion(name='Health Potion', count=2)
    potion_2 = StoneSkinPotion(name='Stone Skin Potion', count=1)
    diadem = Diadem(name='Diadem', count=1)
    sword = Sword(name='Sword', count=1)
    bow = Bow(name='Bow', count=1)
    armour = Armour(name='Armour', count=1)
    npc_character.add_to_inventory(item=potion)
    npc_character.add_to_inventory(item=sword)
    player_character.add_to_inventory(item=potion)
    npc_character.add_to_inventory(item=potion_2)
    player_character.add_to_inventory(item=potion_2)
    npc_character.add_to_inventory(item=diadem)
    player_character.add_to_inventory(item=diadem)
    player_character.add_to_inventory(item=bow)
    npc_character.add_to_inventory(item=armour)
    player_character.add_to_inventory(item=armour)
    npc_character.equip(item=diadem)
    npc_character.equip(item=sword)
    player_character.equip(item=diadem)
    player_character.equip(item=bow)
    npc_character.equip(item=armour)
    player_character.equip(item=armour)

    time.sleep(1)
    fight(character_1=player_character, character_2=npc_character)
