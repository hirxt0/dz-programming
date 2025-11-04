import tools as tl


from random import randint


class Hero:

    def __init__(self, name: str, health: int, power: int, weapon: tl.Weapon = ('кулак', 10, 3), balance: int = 0):
        self.name = name
        self.health = health
        self.power = power
        self.weapon = weapon
        self._balance = balance

    def add_balance(self, amount: int):
        self._balance += amount

    @property
    def info(self) -> str:
        return (f"{self.name}: \n Здоровье = {self.health}\n Сила = {self.power}\n "
                f"Оружие = {self.weapon.name}\n Баланс = {self._balance}")

    def attack(self, other: Hero) -> str:
        base_damage = self.power
        weapon_damage = self.weapon.damage()
        total = base_damage + weapon_damage[1]
        other.health -= total
        if weapon_damage[0]:
            return f"{self.name} атакует {other.name} с помощью {self.weapon.name}, нанося {total} критического урона. У {other.name} осталось {max(0, other.health)} HP.\n"

        return f"{self.name} атакует {other.name} с помощью {self.weapon.name}, нанося {total} урона. У {other.name} осталось {max(0, other.health)} HP.\n"
        

class Cucumber(Hero):

    def __init__(self, name: str, health: int, power: int, weapon: tl.Weapon = ('кулак', 10, 3), balance: int = 0):
        self.inventory = tl.Inventory()
        super().__init__(name, health, power, weapon, balance)

    def spike_attack(self, other: Hero):
        spike_damage = randint(30, 60)
        other.health -= spike_damage
        return f"{self.name} выстрелили своим шипом в {other.name}, нанося {spike_damage} урона. У {other.name} осталось {max(0, other.health)} HP.\n"
    
    def heal(self):
        heal_amount = randint(10, 30)
        self.health += heal_amount
        self.weapon.crit_chance -= 1
        return f"{self.name} восполняет себе {heal_amount} HP. Герой также увеличил свой крит. шанс на 10%. \n"

        
    def show_abilities(self):
        return f"{self.name}, вы можете использовать слудующие:\n \
              1 - атака\n \
              2 - атака шипом\n \
              3 - созидать\n"


class Warrior(Hero):

    def __init__(self, name: str, health: int, power: int, weapon: tl.Weapon = ('кулак', 10, 3), balance: int = 0):
        self.inventory = tl.Inventory()
        super().__init__(name, health, power, weapon, balance)

    def change_weapon(self):
        weapons = self.inventory.show_weapons()
        if not weapons:
            return"В рюкзаке нет другого оружия."

        choice = input("Выберите номер оружия для смены: ")
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(weapons):
                old_weapon = self.weapon
                new_weapon = weapons[idx]
                self.weapon = new_weapon
                self.inventory.items.remove(new_weapon)
                self.inventory.items.append(old_weapon)
                return f"{self.name} теперь вооружён: {self.weapon.name}!"
            else:
                return "Нет такого оружия."
        except ValueError:
            return "Некорректный ввод."

    def heal(self):
        heal_amount = randint(10, 30)
        self.health += heal_amount
        self.weapon.crit_chance -= 1
        return f"{self.name} восполняет себе {heal_amount} HP. Герой также увеличил свой крит. шанс на 10%. \n"

    def show_abilities(self):
        return f"""{self.name}, вы можете использовать следующие навыки: 
              1 - атака
              2 - сменить оружие и атаковать
              3 - созидать"""
              
 

class Ment(Hero):

    def __init__(self, name: str, health: int, power: int, weapon: str = 'кулак', balance: int = 0):
        self.cartridges = 10
        self.inventory = tl.Inventory()
        super().__init__(name, health, power, weapon, balance)

    def attack(self, other):
        if self.cartridges > 0:
            base_damage = self.power
            weapon_damage = self.weapon.damage()
            total = base_damage + weapon_damage[1]
            other.health -= total
            self.cartridges -= 1
            if weapon_damage[0]:
                return f"{self.name} выстрелили в {other.name} с помощью {self.weapon.name}, нанося {total} критического урона. У {other.name} осталось {max(0, other.health)} HP.\n"
            else:
                return f"{self.name} выстрелили в {other.name} с помощью {self.weapon.name}, нанося {total} урона. У {other.name} осталось {max(0, other.health)} HP.\n"
        else:
            return f"У {self.name} закончились патроны"

    def pepper_spray(self, other: Hero):
        pepper_spray_damage = randint(10, 30)
        other.health -= pepper_spray_damage
        return f"{self.name} использовал перцовый баллончик против {other.name}, нанося {pepper_spray_damage} урона. У {other.name} осталось {max(0, other.health)} HP.\n"

    def sneez(self):
        return "Полицейский чихнул"


class Dragon(Hero):

    def __init__(self, name, health, power, weapon, balance=0):
        super().__init__(name, health, power, weapon, balance)

    def breathe_fire(self, other: Hero):
        fire_damage = randint(20, 40)
        other.health -= fire_damage
        return f"{self.name} дышит огнем на {other.name}, нанося {fire_damage} урона. У {other.name} осталось {max(0, other.health)} HP.\n"

    def dragon_heal(self):
        heal_amount = randint(10, 30)
        self.health += heal_amount
        return f"{self.name} исцелился на {heal_amount} HP. Текущее здоровье: {self.health} HP"
