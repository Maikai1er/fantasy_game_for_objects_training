from characters import Ork, Elf


def create_character(race, name):
    match race:
        case 'Ork':
            character = Ork(name=name, level=1, kind='Character')
        case 'Elf':
            character = Elf(name=name, level=1, kind='Character')
        case _:
            pass
    return character
