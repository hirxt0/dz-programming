import tools as tl
import heroes as hr
import mechanics as mc

import sys
import time

def main():
    print("Приветствую тебе в игре \"Рыцарь за МКАДОМ\"")

    main_character = input("Выберите своего персонажа:\n" \
        "1 - благородный и сильный рыцарь Антон\n" \
        "2 - огурец\n ")

    time.sleep(1)
    if main_character == "1":
        main_hero = hr.Warrior("Антон", 100, 10, tl.Weapon('Деревянная палка', 15, 4), 0)
        print(f"Вы сделали прекрасный выбор, ваш персонаж  - незнающий побед рыцарь {main_hero.info}")
    elif main_character == '2':
        main_hero = hr.Cucumber("Огурец", 90, 5, tl.Weapon('Нож', 18, 4), 1000)
        print(f"Вы сделали ошеломительный выбор, ваш персонаж - {main_hero.info}")
    else:
        print("Ошибка ввода")
        sys.exit()  

    time.sleep(1.5)
    move1 = input("Вы очутились на опушке леса" \
    ", перед вами мухомор.\nСъесть его: Да\Нет ").lower() == 'да'
    
    if move1:
        main_hero.health -= 20
        main_hero.power += 10
        time.sleep(1)
        print("Вас конкретно так накрыло, но вы еще в строю\n")
    
    time.sleep(2)
    print("Вы идете дальше, пока не выходите на пустую трассу\n")
    time.sleep(2)
    print("Вы оглядываетесь по сторонам и тут словно ниоткуда появляется полицейский\n")
    
    police = hr.Ment("Юрий Борисович", 100, 12, tl.Weapon('Пистолет', 18, 5), 5000)
    [police.inventory.add_item(x) for x in ['cocain', 'удостоверение', tl.Weapon('Пистолет', 20, 4)]]

    if move1:
        time.sleep(1)
        print("- Гражданин, что вы делаете здесь посреди ночи?", \
               " И почему вы находитесь в таком состоянии?")
        time.sleep(1)
        print("- Отвали\n")
        mc.duel(main_hero, police)
        if main_hero.health <= 0:
            print("Вы проиграли. Конец игры")
            sys.exit()
        else:
            time.sleep(1.5)
            move2 = input("Вы убили полицейского, вы можете подобрать его вещи - Да\Нет: ").lower() == 'да'
            if move2:
                time.sleep(0.8)
                [main_hero.inventory.add_item(item) for item in police.inventory.items]
                main_hero.balance += police.balance
                print(f"Вы подобрали {police.balance} тенге, а также {[str(item) for item in police.inventory.items]}")
    else:
        print("- Гражданин, что вы делаете здесь посреди ночи?\n")
        move3 = input("") == "Пошел нахуй" or "Отвали"
        time.sleep(1)
        if move3:
            mc.duel(main_hero, police)
            if main_hero.health <= 0:
                print("Вы проиграли. Конец игры\n")
                sys.exit()
            else:
                time.sleep(0.5)
                move2 = input("Вы убили полицейского, вы можете подобрать его вещи - Да\Нет: ").lower() == 'да'
                [main_hero.inventory.add_item(item) for item in police.inventory.items]
                main_hero.balance += police.balance
                print(f"Вы подобрали {police.balance} тенге, а также {[str(item) for item in police.inventory.items]}")
        else:
            time.sleep(1)
            print("- Ладно, не задерживайтесь здесь\n")

    main_hero.health = 100
    print("Ваше здоровье восстановилось")
    time.sleep(1)

    move4 = input("Вы движетесь вперед по трассе пока не видите казино. Зайти в него Да\Нет: \n").lower() == 'да'

    if move4:
          time.sleep(0.5)
          mc.Casino.play(main_hero)
          print("Вы вышли из казино\n")

    time.sleep(1)
    move5 = input("Вдалеке вы услышали громкий рёв! Двигаетесь к источнику звука? Да/Нет: \n").lower() == 'да'

    if move5:
        dragon = hr.Dragon("Владислав Борисович", 200, 25, tl.Weapon("Удар крылом", 20, 8), 0)
        time.sleep(0.5)
        print("Вы встретили громадного огнедышащего дракона Владислава Борисовича!\n")
        mc.duel(main_hero, dragon)
        if main_hero.health <= 0:
            print("Вы сгорели в огне дракона. Конец игры.")
            sys.exit()
        else:
            print("Герой победил дракона! Вам удалось выжить в тяжелых условиях заМкадья, вы молодец!\n")
    else:
        print("Вы решили не подходить к дракону и ушли домой. Конец игры")
    

if __name__ == "__main__":
    main()