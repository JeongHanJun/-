'''class C1:
    a = 1
print(C1.a)
C1.b = 2
print(C1.b)
#print(dir(C1))
# class instance x
x = C1()
x.a = 10
print(x.a)
print(C1.a)
y = C1()
y.a = 'y.a = Class instance y 의 이름공간에 a라는 이름 생성'
print(y.a)
print(x.a)
print(C1.a)
'''
# 상속 Inheritance
# class-class간에 공통적인 특징 공유
'''
class KBO:
    team = ['NC', 'KiWoom', 'DooSan', 'LG', 'KT', 'else']
    player= []
    judge = 'No Answer'
    def f():
        print('KBO')
class Heroes:
    pass
d = Heroes()
KBO.f()

class MyClass:
    def prord(x,y):
        print(x+y)
MyClass.prord(4,6)'''
'''class Cname:    # header
    pass        # body
s1 = Cname()
s2 = Cname()        # s1, s2 는 Cname 이라는 클래스를 호출하는 클래스 인스턴스 객체
s1.stack = []
s1.stack.append(1)
s1.stack.append(2)
s1.stack.append(3)  # [1, 2, 3]
print(s1.stack)
print('In s1 stack,', s1.stack.pop(), 'is poped')
print('In s1 stack,', s1.stack.pop(), 'is poped')
print(s1.stack)
s2.stack = None
print(s2.stack)         # 같은 클래스를 참조하는 다른 클래스 인스턴스에 대해, 각각의 인스턴스도 독립적인 공간을 가진다.
'''
'''
class tClass:
    def set(self, v):
        self.value = v
    def put(self):
        print(self.value)   # self는 this 와 같은 느낌
c= tClass()
c.set('abc')
c.put()
#tClass.set(c, 'abc')   위에꺼랑 같은 내용
#tclass.put()'''
'''
class Operate:
    def Add(x, y):
        return x+y
    def Mul(x,y):
        return x*y
    def pb():
        print("I Like BaseBall")
    def kh():
        print("My team is Kiwoom Heroes")
    kh = staticmethod(kh)
o = Operate()
o.Add(5,4)
o.Mul(4,5)
o.pb()
o.kh()
'''
'''
# 절챠 지향적 코드
phone1 = 'I phone'
detail_phone1 = {'color' : 'white'} , {'price' : 10000}
phone2 = 'Galaxy'
detail_phone2 = {'color' : 'Blue'}, {'price' : 8000}
phone3 = 'BB'
detaul_phone3 = {'color' : 'Red'}, {'price' : 6000}

#List 코드
phone_list = ['I phone', 'Galaxy', 'BB']
phone_detail_list = [ {'color' : 'white', 'price' : 10000}
                      {'color' : 'Blue', 'price' : 8000}
                      {'color' : 'Red', 'price' : 6000} ]
#Dictionary 코드
phone_dict = [
        { 'color' : 'White', 'price' : 10000}
        { 'color' : 'Blue', 'price' : 8000}
        { 'color' : 'Red', 'price' : 6000}
]'''
'''
class sphone:
    def __init__(self, company, detail):
        self.company = company
        self.detail = detail
    def __str__(self):
        return f'str : {self._company} - {self._detail}'
    def __repr__(self):
        return f'repr : {self._company} - {self._detail}'
        @staticmethod
        def mod(x,y):
            print('static method', x, y)
            return x%y
sp1 = sphone('Iphone', {'color': 'white', 'price' : 10000})
sp2 = sphone('Galaxy', {'color': 'Blue', 'price' : 8000})
sp3 = sphone('BB', {'color':'Silver', 'price': 6000})
#print(sp1)
print(sp1.__dict__)
print(sp2.__dict__)
print(sp3.__dict__)
'''
'''
from time import time, ctime, sleep
class life:
    def __init__(self):
        self.start = ctime()
        print('The time which Execution started :', self.start)
    def __del__(self):
        print('The time which Execution finished :', ctime())
def test():
    mylife = life()
    print('sleep for 3 sec')
    sleep(3)
test()
# when test func called, life class's instance is constructed called ' my life '
  Automatically, __init__func start and the time which statement executed is saved in self.start
  And wait for 3 second
  and when test func is finished, __del__ func start and print finished time
    생성자 __init__ / 소멸자 __del__
'''
class Smartphone:
    def __init__(self, brand, details):
        self._brand = brand
        self._details = details

    def __str__(self):
        return f'str : {self._brand} - {self._details}'

    def __repr__(self):
        return f'repr : {self._brand} - {self._details}'
    

Smartphone1 = Smartphone('Iphone'    , {'color' : 'White' , 'price': 10000})
Smartphone2 = Smartphone('Galaxy'    , {'color' : 'Black' , 'price': 8000})
Smartphone3 = Smartphone('Blackberry', {'color' : 'Silver', 'price': 6000})
Smartphone_list = ['Iphone', 'Galaxy', 'Blackberry']
print(Smartphone1)
print(Smartphone1.__dict__)
print(Smartphone2.__dict__)
print(Smartphone3.__dict__)


print(id(Smartphone1))
print(id(Smartphone2))

print(Smartphone1._brand == Smartphone2._brand)
print(Smartphone1 is Smartphone2)
for x in Smartphone_list:
    print(repr(x))
    print(x)
    
print(Smartphone.__doc__) 
print()
print()
print()
print(Smartphone1.__dict__)
print(dir(Smartphone1))
