class Relics:
    def __init__(self, *, name: str) -> None:
        self.name = name
    def __str__(self) -> str:
        return f'The item is {self.name}'


class HealthPotion(Relics):
    name = 'Health Potion'

    def use(self, *, target: 'Character') -> None:
        target.health += 30
        print(f'{target.name} health increased by 30 and is {target.health} now')


# class Diadem(Relics):
#     name = 'Diadem'
#
#     def equip(self, *, target: 'Character') -> None:
