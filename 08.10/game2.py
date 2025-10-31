import random

tools = ['камень', 'ножницы', 'бумага']
moves = {'камень': 'ножницы', 'ножницы': 'бумага', 'бумага': 'камень'}

def game() -> str:
    score = [0, 0]
    for _ in range(1, 4):
        user_move = input('ваш ход: [камень\ножницы\бумага]: \n')
        comp_move = random.choice(tools)

        if moves[user_move] == comp_move:
            score[0] += 1
        else:
            score[1] += 1

        if score[0] == 2:
            return 'ты победил'
        elif score[1] == 2:
            return 'компьтер победил'
        
        print(score)

print(game())