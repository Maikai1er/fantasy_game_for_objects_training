import time
from relics_for_fight import Relics, HealthPotion


class Character:
    def __init__(self, *, name: str, level: int) -> None:
        self.level = level
        self.health = self.base_health * level
        self.attack_power = self.base_attack * level
        self.name = name

    def __str__(self) -> str:
        return f'The {self.name} character is level {self.level} with health {self.health} and attack {self.attack_power}'

    def attack_target(self, target: 'Character') -> None:
        target.got_damage(damage=self.attack_power)

    def got_damage(self, *, damage: int) -> None:
        self.health -= damage


class Elf(Character):
    base_attack = 15
    base_health = 60


class Ork(Character):
    base_attack = 10
    base_health = 100


ork = Ork(name='Orche', level=1)
elf = Elf(name='Legolas', level=1)
potion = HealthPotion
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


fight(character_1=ork, character_2=elf)