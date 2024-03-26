class Relics:
    def __init__(self, name: str, count: int, attributes: dict = {}, description: str = '') -> None:
        self.name = name
        self.count = count
        self.attributes = attributes
        self.health_modifier = self.attributes.get('health_modifier')
        self.damage_modifier = self.attributes.get('damage_modifier')
        self.defence_modifier = self.attributes.get('defence_modifier')
        self.description = description

    def __str__(self) -> str:
        return f'The item is {self.name}, count is {self.count}'

    def create_item_and_count(self) -> object:
        return {self.name: self.count}


class HealthPotion(Relics):
    name = 'Health Potion'
    attributes = []
    description = 'Heals the owner for 30 HP'


class StoneSkinPotion(Relics):
    name = 'Stone Skin Potion'
    attributes = []
    description = 'Increases defence by 3 times'


class Diadem(Relics):
    name = 'Diadem'
    attributes = {
        'health_modifier': 2,
        'damage_modifier': 3,
        'defence_modifier': 2,
    }
    description = 'Increases damage, hp and defence by 2'


class Sword(Relics):
    name = 'Sword'
    perks = {
        'damage_modifier': 5,
    }
    description = 'Increases damage by 5'
