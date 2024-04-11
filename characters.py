class Creature:
    def __init__(self, *, name: str, level: int, kind: str) -> None:
        self.name = name
        self.level = level
        self.max_health = self.base_health * level
        self.health = self.max_health
        self.attack_power = self.base_attack * level
        self.defence = self.base_defence * level
        self.inventory = {}
        self.kind = kind

    def __str__(self) -> str:
        return (f'Name: {self.name}, Level: {self.level}, Health: {self.max_health}, '
                f'Defence: {self.defence}, Attack: {self.attack_power}')

    def attack_target(self, target: 'Creature') -> None:
        target.got_damage(damage=self.attack_power)

    def got_damage(self, *, damage: int) -> None:
        damage_received = damage * (1 - self.defence / 100)
        self.health -= round(damage_received)

    def increase_attack(self, *, damage_modifier=0) -> None:
        self.attack_power += damage_modifier

    def increase_defence(self, *, defence_modifier=0) -> None:
        self.defence += defence_modifier

    def increase_max_health(self, *, health_modifier=0) -> None:
        self.max_health += health_modifier

    def heal(self, *, heal_amount: int) -> None:
        self.health += heal_amount

    def use_potion(self, *, potion_name) -> None:
        # print(self.inventory[potion_name])
        if self.inventory[potion_name]['count'] > 0:
            self.inventory[potion_name]['count'] -= 1
            # print(self.inventory[potion_name]['attributes'])
            # print(potion_name.get_attributes)
            attributes = self.inventory[potion_name]['attributes']
            match potion_name:
                case 'Health Potion':
                    self.heal(heal_amount=attributes['heal_amount'])
                    print(f'The {self.name} has used Health Potion and has '
                          f'{self.inventory['Health Potion']['count']} left.')
                case 'Stone Skin Potion':
                    self.increase_defence(defence_modifier=attributes['defence_multiplier'])
                    print(f'The {self.name} has used Stone Skin Potion and has '
                          f'{self.inventory['Stone Skin Potion']['count']} left.')
                case _:
                    return


class Character(Creature):
    kind = 'Character'

    def add_to_inventory(self, *, item) -> None:
        if item.name in self.inventory:
            self.inventory[item.name]['count'] += item.count
        else:
            self.inventory[item.name] = {
                'data': item,
                'count': item.count,
                'attributes': item.attributes,
            }

    def equip(self, *, item) -> None:
        if hasattr(item, 'health_modifier'):
            self.increase_max_health(health_modifier=item.health_modifier or 0)
        if hasattr(item, 'defence_modifier'):
            self.increase_defence(defence_modifier=item.defence_modifier or 0)
        if hasattr(item, 'damage_modifier'):
            self.increase_attack(damage_modifier=item.damage_modifier or 0)
        # print(self.inventory[item.name]['count'])

        self.inventory[item.name]['count'] -= 1


class Monster(Creature):
    kind = 'Monster'


class Werewolf(Monster):
    name = 'Werewolf'
    base_attack = 20
    base_health = 100
    base_defence = 10


class Elf(Character):
    base_attack = 15
    base_health = 60
    base_defence = 7


class Ork(Character):
    base_attack = 10
    base_health = 100
    base_defence = 10
