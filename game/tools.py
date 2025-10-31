from random import randint


class Inventory:

    def __init__(self):
        self.items = []

    def add_item(self, item: any):
        self.items.append(item)

    def show_weapons(self):
        weapons = [i for i in self.items if isinstance(i, Weapon)]
        if not weapons:
            return
        print("Доступное оружие:")
        for idx, w in enumerate(weapons, start=1):
            print(f"{idx}) {w.name} (урон {w.base_damage}, крит. шанс {w.crit_chance}/10)")
        return weapons
    

class Weapon:

    def __init__(self, name: str, base_damage: int, crit_chance: int):
        self.name = name
        self.base_damage = base_damage
        self.crit_chance = crit_chance

    def damage(self):
        dmg = self.base_damage
        if randint(1, 10) <= self.crit_chance:
            crit_dmg = dmg * 2
            return [1, crit_dmg]
        return [0, dmg]
    
    def __str__(self):
        return f"Оружие: {self.name} Базовый урон: {self.base_damage}, Крит. шанс: {self.crit_chance * 10}% "
