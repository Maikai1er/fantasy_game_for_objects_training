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

    def got_damage(self, *, damage: int) -> None:
        damage_received = damage * (1 - self.defence / 100)
        self.health -= round(damage_received)

    def add_to_inventory(self, *, item) -> None:
        item_to_add = Relics.create_item_and_count(item)
        self.inventory.update(item_to_add)

    def increase_attack(self, *, damage_modifier=0) -> None:
        self.attack_power += damage_modifier

    def increase_defence(self, *, defence_modifier=0) -> None:
        self.defence += defence_modifier

    def increase_health(self, *, health_modifier=0) -> None:
        self.health -= health_modifier

    def equip(self, *, item) -> None:
        if hasattr(item, 'health_modifier'):
            self.increase_health(health_modifier=item.health_modifier or 0)
        if hasattr(item, 'defence_modifier'):
            self.increase_defence(defence_modifier=item.defence_modifier or 0)
        if hasattr(item, 'damage_modifier'):
            self.increase_attack(damage_modifier=item.damage_modifier or 0)

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
            print(f'{self.name} used Stone Skin Potion! Defence is increased by 3 times!')


class Elf(Character):
    base_attack = 15
    base_health = 60
    base_defence = 7


class Ork(Character):
    base_attack = 10
    base_health = 100
    base_defence = 10
