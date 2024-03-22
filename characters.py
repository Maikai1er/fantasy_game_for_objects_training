from relics import Relics, HealthPotion


class Character:
    def __init__(self, *, name: str, level: int) -> None:
        self.level = level
        self.health = self.base_health * level
        self.attack_power = self.base_attack * level
        self.name = name
        self.inventory = {}

    def __str__(self) -> str:
        return f'The {self.name} character is level {self.level} with health {self.health} and attack {self.attack_power}'

    def attack_target(self, target: 'Character') -> None:
        target.got_damage(damage=self.attack_power)

    def got_damage(self, *, damage: int) -> None:
        self.health -= damage

    def add_to_inventory(self, *, item) -> None:
        item_to_add = Relics.create_item_and_count(item)
        self.inventory.update(item_to_add)

    def use_health_potion(self) -> None:
        if self.inventory['Potion'] >= 0:
            self.health += 30
            print(f'Potion is used! The health is {self.health}! Potions left: {self.inventory["Potion"]}')
            self.inventory['Potion'] -= 1


class Elf(Character):
    base_attack = 15
    base_health = 60


class Ork(Character):
    base_attack = 10
    base_health = 100
