class Relics:
    def __init__(self, *, name: str, count: int) -> None:
        self.name = name
        self.count = count

    def __str__(self) -> str:
        return f'The item is {self.name}, count is {self.count}'

    def create_item_and_count(self) -> object:
        return {self.name: self.count}


class HealthPotion(Relics):
    name = 'Potion'
    # Heals 30 HP


class StoneSkinPotion(Relics):
    name = 'Stone Skin'
    # Increases your current defence by three times


class Diadem(Relics):
    name = 'Diadem'

    def __init__(self, name: str, count: int) -> None:
        super().__init__(name=name, count=count)
        self.perks = {
            'health_modifier': 2,
            'damage_modifier': 3,
            'defence_modifier': 2,
        }

        self.health_modifier = self.perks.get('health_modifier')
        self.damage_modifier = self.perks.get('damage_modifier')
        self.defence_modifier = self.perks.get('defence_modifier')

    # Increases damage, hp and defence by 2


class Sword(Relics):
    name = 'Sword'

    def __init__(self, name: str, count: int) -> None:
        super().__init__(name=name, count=count)
        self.perks = {
            'damage_modifier': 5,
        }

        self.damage_modifier = self.perks.get('damage_modifier')
