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

