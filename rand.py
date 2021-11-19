import random

left_life = 0

def rand_num():
    guess = random.randrange(1,100)
    return (guess)

def decide(number, player):
    if number < player:
        print("DOWN\n")
        print("목숨이 %d개 남았습니다."%(left_life))

    if number > player:
        print("UP\n")
        print("목숨이 %d개 남았습니다."%(left_life))

    if number == player:
        print("맞았습니다.")