import random

#定义fight函数实现打架游戏逻辑
def fight(my_ph,my_power,enemy_ph,enemy_power):
    my_ph = my_ph - enemy_power
    enemy_ph = enemy_ph - my_power
    if (my_ph <= 0):
        if(enemy_ph <= 0):
            print("平局！")
            print(f"我方的血量为：{my_ph},敌方的血量为：{enemy_ph}")
        else:
            print("我输了！")
            print(f"我方的血量为：{my_ph},敌方的血量为：{enemy_ph}")
        return 0;
    elif (enemy_ph <= 0):
        print("我赢了！")
        print(f"我方的血量为：{my_ph},敌方的血量为：{enemy_ph}")
        return 0;
    else:
        return (my_ph,enemy_ph)


#自定义双方的初始ph值
my_ph = int(input("请输入我方目前的ph值："))
enemy_ph = int(input("请输入敌方目前的ph值："))

while True:
    #双方每次打架的power攻击力为一个随机值
    my_power = random.randint(100,200)
    enemy_power = random.randint(100,200)

    fight_result = fight(my_ph,my_power,enemy_ph,enemy_power)

    #通过判断函数的返回值来确定游戏是否已分出胜负
    if isinstance(fight_result,tuple):
        my_ph = fight_result[0]
        enemy_ph = fight_result[1]
    else:
        break