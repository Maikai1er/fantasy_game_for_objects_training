import time

from fight import prepare_to_fight, fight


def run_game():
    print("Welcome to the Neverland, stranger")
    time.sleep(1)
    print("Let the battle begin!")
    time.sleep(1)
    characters = input("What characters would you like to fight?")
    print(characters.split(', '))
    elf1, ork1, werewolf = prepare_to_fight()
    print(elf1, ork1)
    fight(character_1=ork1, character_2=werewolf)
