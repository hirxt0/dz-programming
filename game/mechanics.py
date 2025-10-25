import heroes as hr
import tools as tl

from random import randint
import sys
import time
        

class Casino:

    def __init__(self, hero: hr.Hero, hero_weapon : tl.Weapon):
        self.hero = hero
        self.hero.weapon = hero_weapon

    def play(self):
        
        game_type = input("""
                          Вы попали в казино! Выберите игру: 
                          1 - бархатный шелест 
                          2 - русская рулетка с 7 патронами
                          3 - русская рулетка с 6 патронами: """
                          )

        if game_type == "1": 
            print("Перед вами 8 задание ЕГЭ по русскому языку. Ваша задача - ответить правильно, иначе вы уммрете.")
            answer = input("""Укажите варианты ответов, в которых во всех словах одного ряда пропущена одна и та же буква. Запишите номера ответов.

                                1) тр..нироваться, зан..мательный (рассказ), перекл..каться
                                2) д..рижёр, с..рень, заж..гательный
                                3) р..мантизм, ск..сить (траву), разг..дать
                                4) лег..ндарный, изм..рение (скорости), забл..стеть
                                5) ди..пазон, изд..вать (звук), п..стух)
                                Ваш ответ:  """) == '245'
            
            if answer:
                print("Вы выйграли в бархатный шелест! Ваш баланс увеличен на 1000 тенге епта и вам дается зачарование на меч!")
                self.hero.balance += 1000
                self.hero.weapon.damage += 5
                self.hero.weapon.crit_chance += 1

            else:
                print("Неправильно! Вы проиграли, охранник казино подходит к вам сзади и убивает вас! Конец игры")
                sys.exit()

        elif game_type == "2":
            print("Вы играете в русскую рулетку с 7 патронами. Мои соболезнования")
            chamber = randint(1, 8)
            if chamber == 1:
                print("Вы выжили! Ваш баланс увеличен на 1000 тенге")
                self.hero.balance += 1000
            else:
                print("ХААХХАХАХАХ А на че ты расчитывал? Ты умер! Конец игры")
                sys.exit()
            
        elif game_type == "3":
            print("Вы играете в русскую рулетку с 7 патронами. Мои соболезнования")
            chamber = randint(1, 8)
            if chamber == 1 or chamber == 2:
                print("Вы выжили! Ваш баланс увеличен на 500 тенге")
                self.hero.balance += 500
            else:
                print("ХААХХАХАХАХ А на че ты расчитывал? Ты умер! Конец игры")
                sys.exit()
        else:
            return "Ошибка ввода! Поробуйте еще раз"


def duel(hero1: hr.Hero, hero2: hr.Hero):
        print(f"\nБой между {hero1.name} и {hero2.name} начинается!\n")

        while hero1.health > 0 and hero2.health > 0:
            time.sleep(0.7)
            if hasattr(hero1, "show_abilities"):
                print(hero1.show_abilities())
            move = input("Выберите действие: ")
            try:
                if move == "1":
                    print(hero1.attack(hero2))
                elif move == "2" and hasattr(hero1, "spike_attack"):
                    print(hero1.spike_attack(hero2))
                elif move == "2" and hasattr(hero1, "change_weapon"):
                    print(hero1.change_weapon())
                    print(hero1.attack(hero2))
                elif move == "3" and hasattr(hero1, "heal"):
                    print(hero1.heal())
                else:
                    print("Неверный ввод, вы пропускаете ход.")

            except:
                print(f"Неправильный ввод. Ход пропущен.")

            if hero2.health <= 0:
                print(f"{hero2.name} пал! Победил {hero1.name}.")
                break

            move2 = randint(1, 3)
            print(f"\nХод {hero2.name}: {move2}")
            if move2 == 1:
                if hasattr(hero2, "attack"):
                    print(hero2.attack(hero1))
            elif move2 == 2:
                if hasattr(hero2, "pepper_spray"):
                    print(hero2.pepper_spray(hero1))
                elif hasattr(hero2, "breathe_fire") and randint(0, 1):
                    print(hero2.breathe_fire(hero1))
                elif hasattr(hero2, "change_weapon"):
                    print(hero2.change_weapon())
            elif move2 == 3:
                if hasattr(hero2, "sneez"):
                    print(hero2.sneez())
                elif hasattr(hero2, "dragon_heal"):
                    print(hero2.dragon_heal())
            if hero1.health <= 0:
                print(f"{hero1.name} пал! Победил {hero2.name}.")
                break
