from random import randint


print('ИГРА НАЧАЛАСЬ епта')

class Heroes:

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power


class Attack(Heroes):
        
        def __init__(self, name, health, power, weapon):
            self.weapon = weapon
            super().__init__(name, health, power)

        def attack(self, weapon, other_hero):
            damage = randint(0, self.power)
            critical_chance = randint(1, 10)

            if weapon == "меч":
                damage += 2
                if critical_chance > 7:
                    damage *= 2
            
            if weapon == "лук":
                damage += 1
                if critical_chance > 6:
                    damage *= 2
            
            if weapon == "топор":
                damage += 3
                if critical_chance > 8:
                    damage *= 2
            
            if weapon == "магия":
                damage += 4
                if critical_chance > 9:
                    damage *= 2

            other_hero.health -= damage

            return f"{self.name} атакует {other_hero.name} с помощью {weapon}, нанося {damage} урона. У {other_hero.name} осталось {other_hero.health} здоровья"
    

class Casino:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def play(self):
        
        game_type = input("Вы попали в казино епта! Выберите игру: 1 - бархатный шелест, 2 - русская рулетка с 7 патронами, 3 - русская рулетка с 6 патронами: ")
        try:
            if game_type == "1": 
                print("Перед вами 8 задание ЕГЭ по русскому языку. Ваша задача - ответить правильно, иначе вы уммрете.")
                answer = input("""Укажите варианты ответов, в которых во всех словах одного ряда пропущена одна и та же буква. Запишите номера ответов.

                                1) тр..нироваться, зан..мательный (рассказ), перекл..каться
                                2) д..рижёр, с..рень, заж..гательный
                                3) р..мантизм, ск..сить (траву), разг..дать
                                4) лег..ндарный, изм..рение (скорости), забл..стеть
                                5) ди..пазон, изд..вать (звук), п..стух)
                               Ваш ответ: """) == '245'
                if answer:
                    print("Вы выйграли в бархатный шелест! Ваш баланс увеличен на 1000 тенге епта и вам дается зачарование на меч!")
                    self.__balance += 1000
                else:
                    print("Неправильно!!!!!! Вы проиграли епта и вас жестоко казнили!!! Конец игры")
                    exit()

            elif game_type == "2":
                print("Вы играете в русскую рулетку с 7 патронами. Мои соболезнования")
                chamber = randint(1, 8)
                if chamber == 1:
                    print("Вы выжили! Ваш баланс увеличен на 1000 тенге")
                    self.__balance += 1000
                else:
                    print("ХААХХАХАХАХ А на че ты расчитывал? Ты умер! Конец игры")
                    exit()
            
            elif game_type == "3":
                print("Вы играете в русскую рулетку с 7 патронами. Мои соболезнования")
                chamber = randint(1, 8)
                if chamber == 1 or chamber == 2:
                    print("Вы выжили! Ваш баланс увеличен на 500 тенге")
                    self.__balance += 500
                else:
                    print("ХААХХАХАХАХ А на че ты расчитывал? Ты умер! Конец игры")
                    exit()
        except:
            print("Ошибка ввода! поробуйте еще раз")

class Figth(Attack):

    def __init__(self, name):
        self.name = name

    def duel(self, hero1, hero2, weapon1, weapon2):
        while hero1.health > 0 and hero2.health > 0:
            print(hero1.attack(weapon1, hero2))
            if hero2.health <= 0:
                print(f"{hero2.name} пал в бою! {hero1.name} победил")
                break
            print(hero2.attack(weapon2, hero1))
            if hero1.health <= 0:
                print(f"{hero1.name} пал в бою! {hero2.name} победил")
                break
                

