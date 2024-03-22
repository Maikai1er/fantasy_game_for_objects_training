class Relics:
    def __init__(self, *, name: str, count: int, **kwargs) -> None:
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
    health_modifier = 2
    damage_modifier = 2
    defence_modifier = 2

    # Increases damage, hp and defence by 2
