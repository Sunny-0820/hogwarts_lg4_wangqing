### 作业一：封装五个类

#定义类：书
class Book:
    #定义书的页码数和封面颜色
    page_number = 100
    cover_colour = 'Silver'

    #定义书的出版地
    def publisher_place(self):
        print("出版的地方：中国！")

    #定义书的种类
    def species(self):
        print("上架建议：文学种类！")

#定义类：动物
class Animal:
    #定义动物身体颜色
    colour = "black"

    #定义动物的食性
    def eating(self):
        print("是肉食动物！")

    #定义动物的生存环境
    def living_environment(self):
        print("是水生动物！")

# 定义类：桌子
class table:
    shape = "square"
    colour = "white"

    def func1(self):
        print("可以进行旋转！")

    def func2(self):
        print("高度可以进行升降！")

#定义类：椅子
class chair:
    colour = "black"
    hight = 10
    def function1(self):
        print("可以加热进行按摩！")
    def function2(self):
        print("可以进行折叠！")

#定义类：灯
class Lamp:
    #定义灯的形状和颜色：
    shape = "round"
    colour = "yellow"

    #定义灯的寿命长度
    def lifetime(self):
        print("灯的寿命为5年！")

    #定义灯的挡位和对应的光照强度
    def brightness(self,gear):
        if gear==0 :
            print("灯已关闭")
        elif gear==1 :
            print("灯调为一档，光照强度为弱！")
        elif gear==2 :
            print("灯调为二档，光照强度为中！")
        elif gear==3 :
            print("灯调为三档，光照强度为强！")
        else:
            print("灯的挡位超出范围，请重新设置挡位！")



#实例化书类
my_book = Book()
print(f"书的页码数为：{my_book.page_number},书的封面颜色为:{my_book.cover_colour}")
my_book.species()
my_book.publisher_place()

#实例化动物类
my_animal = Animal()
print(f"动物身体的颜色为{my_animal.colour}")
my_animal.eating()
my_animal.living_environment()

#实例化桌子类
my_table = table()
print(f"桌子形状为{my_table.shape},桌子颜色为{my_table.colour}")
my_table.func1()
my_table.func2()

#实例化椅子类
my_chair = chair()
print(f"椅子高度为{my_chair.hight},椅子颜色为{my_chair.colour}")
my_chair.function1()
my_chair.function2()

#实例化灯类
my_lamp = Lamp()
print(f"灯的形状为：{my_lamp.shape},灯的颜色为：{my_lamp.colour}")
my_lamp.lifetime()
my_lamp.brightness(2)



