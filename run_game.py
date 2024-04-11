from fight import prepare_to_fight, fight


def run_game():
    elf1, ork1 = prepare_to_fight()
    print(elf1, ork1)
    fight(character_1=ork1, character_2=elf1)
