import time

from create_character import create_character
from fight import prepare_to_fight, fight


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
    time.sleep(1)
    fight(character_1=player_character, character_2=npc_character)
