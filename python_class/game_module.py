"""
作业二：
1、定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
    (1)see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，
    如果传入“丁春秋”，打印“叛徒！我杀了你”
    (2)fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，
    打完之后，比较双方血量。血多的一方获胜。
2、定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
3、加入模块化改造
"""

## 定义TongLao类
class TongLao:
    #定义构造函数，传入hp、power参数
    def __init__(self,hp,power):
        self.my_hp = hp
        self.my_power = power

    #定义see_people方法，传入name参数
    def see_people(self,name):
        #判断传入的name是否为特定的字符，否则直接pass
        if(name == "WYZ"):
            print("师弟！！！！")
        elif(name == "李秋水"):
            print("师弟是我的！")
        elif(name == "丁春秋"):
            print("叛徒！我杀了你!")
        else:
            pass

    #定义fight_zms方法，传入emeny_hp、emeny_power参数
    def fight_zms(self,emeny_hp,emeny_power):

        self.my_hp = self.my_hp / 2
        self.my_power = self.my_power * 10

        self.my_hp = self.my_hp - emeny_power
        emeny_hp = emeny_hp - self.my_power

        #判断一回合制后的输赢情况
        if(self.my_hp > emeny_hp):
            print("我赢了！")
            return 1;
        elif(self.my_hp < emeny_hp):
            print("我输了！")
            return 2;
        else:
            print("平局！")
            return 0;

## 定义XuZhu类，并继承TongLao类
class XuZhu(TongLao):
    def read(self):
        print("罪过罪过！")

## 定义DingChunQiu类
class DingChunQiu:
    def __init__(self,hp):
        self.my_hp = hp

    #定义armor方法，提升hp值
    def armor(self):
        self.my_hp = self.my_hp * 2
        return self.my_hp

    def fight_result(self,result):
        if (result == 0):
            print("来呀，再战！")
        elif(result == 1):
            print("放过我吧！")
        elif(result == 2):
            print("哈哈哈，受死吧！")