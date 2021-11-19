import random

def rand_num():
    guess = random.randrange(1,100)
    return (guess)

def decide(number, player,life):
    if number < player:
        print("결과 : DOWN")
        print("목숨이 %d개 남았습니다.\n"%(life))

    if number > player:
        print("결과 : UP\n")
        print("목숨이 %d개 남았습니다.\n"%(life))

    if number == player:
        print("맞았습니다.\n\n")
num = rand_num()
life = 4

print("숫자맞추기 게임\n\n")
for i in range(6,0,-1):
    player_guess = int(input("맞출 숫자를 입력하세요\n"))
    decide(num, player_guess,life)
    print("\n-------------------------\n")
    life-=1
    if life == -1:
        print("게임오버")
        print("결과는 %d 였습니다."%(num))
        break
