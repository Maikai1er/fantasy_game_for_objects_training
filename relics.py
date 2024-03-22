class Relics:
    def __init__(self, *, name: str = 'Potion', count: int) -> None:
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
    # Increases your defence by three times


# class Diadem(Relics):
#     name = 'Diadem'

