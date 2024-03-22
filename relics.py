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


# class Diadem(Relics):
#     name = 'Diadem'
#
#     def equip(self, *, target: 'Character') -> None:
