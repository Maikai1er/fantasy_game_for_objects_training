from relics import Relics, HealthPotion


class Character:
    def __init__(self, *, name: str, level: int) -> None:
        self.level = level
        self.health = self.base_health * level
        self.attack_power = self.base_attack * level
        self.name = name
        self.inventory = {}
        self.defence = self.base_defence * level

    def __str__(self) -> str:
        return f'The {self.name} character is level {self.level} with health {self.health} and attack {self.attack_power}'

    def attack_target(self, target: 'Character') -> None:
        target.got_damage(damage=self.attack_power)

    def defence_percentage(self) -> int:
        return self.defence / 100

    def got_damage(self, *, damage: int) -> None:
        damage_received = damage * (1 - self.defence_percentage())
        self.health -= round(damage_received)

    def add_to_inventory(self, *, item) -> None:
        item_to_add = Relics.create_item_and_count(item)
        self.inventory.update(item_to_add)

    def use_health_potion(self) -> None:
        if self.inventory['Potion'] > 0:
            self.health += 20
            self.inventory['Potion'] -= 1
            print(
                f'Health Potion is used! The {self.name} health is {self.health}! Potions left: {self.inventory["Potion"]}'
            )

    def use_stone_skin_potion(self) -> None:
        if self.inventory['Stone Skin Potion'] > 0:
            self.defence *= 3
            self.inventory['Stone Skin Potion'] -= 1
            print(f'{self.name} used Stone Skin Potion! Base defence is increased by 3 times!')


class Elf(Character):
    base_attack = 15
    base_health = 60
    base_defence = 7


class Ork(Character):
    base_attack = 10
    base_health = 100
    base_defence = 10
