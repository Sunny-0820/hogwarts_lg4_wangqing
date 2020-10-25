from hogwarts_lg4_wangqing.python_class.game_module import XuZhu, TongLao, DingChunQiu
import random

#定义define_hp_power函数得到升级后人物的hp、power值
def define_hp_power(lev_num):
    #定义初始hp、power值
    hp = random.randint(1000,1100)
    power = random.randint(190, 200)

    #按照升级的级数hp/power发生对应变化
    hp = hp * (lev_num/10 + 1)
    power = power * (lev_num / 10 + 1)

    #返回升级后人物的hp、power值
    return (hp,power)


#自定义童姥、虚竹、丁春秋的等级数
tonglao_lev_num = int(input("请输入目前童姥的等级数："))
xuzhu_lev_num = int(input("请输入目前虚竹的等技数："))
dingchunqiu_lev_num = int(input("请输入目前丁春秋的等技数:"))


#用define_hp_power函数得到升级后的童姥、虚竹、丁春秋的hp、power值
(tonglao_hp,tonglao_power) = define_hp_power(tonglao_lev_num)
(xuzhu_hp,xuzhu_power) = define_hp_power(xuzhu_lev_num)
(dingchunqiu_hp,dingchunqiu_power) = define_hp_power(dingchunqiu_lev_num)


#实例化TongLao类、XuZhu类、DingChunQiu类
new_tonglao = TongLao(tonglao_hp,tonglao_power)
new_xuzhu = XuZhu(xuzhu_hp,xuzhu_power)
new_dingchunqiu = DingChunQiu(dingchunqiu_hp)


#调用TongLao类中的see_people方法
new_tonglao.see_people("丁春秋")


#调用DingChunQiu类中的armor方法
dingchunqiu_hp = new_dingchunqiu.armor()


#调用TongLao类中的fight_zms方法
result = new_tonglao.fight_zms(dingchunqiu_hp,dingchunqiu_power)


#调用DingChunQiu类中的fight_result方法
new_dingchunqiu.fight_result(result)


#根据打架结果result，虚竹做出不同的反应
if (result == 2):
    print("虚竹：休要猖狂！")
    #调用XuZhu类继承的TongLao类中的fight_zms方法
    new_xuzhu.fight_zms(xuzhu_hp,xuzhu_power)

else:
    #调用XuZhu类中的read方法
    new_xuzhu.read()



