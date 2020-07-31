divmod(2, 3)
print(divmod(2, 3))
print(5.)
print(5.0)
print(5)
print(5e10)
print(2**3)
print(2**3**2)  # 2^(3^2) = 2^9
a = 1+4j    # 복소수  여기는 허수부에 i가 아닌 j를 사용 
b = 5-3j
print(a+b)  # 6 + j
print(a*b)  # 5 - 3j + 20j +12 = 17 +17j
# 복소수 출력시 () 괄호 안에 실수부+허수부 형태로 출력됨
print(b.real)   #실수부  float
print(b.imag)   #허수부  float
# python idle 종료 하고싶으면 ctrl d
'''import calendar
calendar.prmonth(2020,7)
import os
obj = input("inputgo : ")
print(obj)
inputgo : os.system("time")'''
# 파이썬은 입력값을 형변환하는 과정중에 파이썬 코드가 실행됨
from turtle import *
'''reset()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
''''''
for k in range(20):
    forward(50) # 앞으로 50만큼
    backward(30)    # 뒤로 30만큼
    left(20)    #각도를  20도 만큼 회전 반시계방향으로
    right(10)   #각도는 10도만큼 회전 시계방향으로
   # goto(100,100)  # 100,100으로 커서(펜) 이동
   circle(50, [180, -180])'''
'''for k in range(3):
    forward(100)
    left(120)       
    # 정삼각형'''
str(12345)      # string형으로 형변환
str1 = 'abc'
print(str1)
print(str)  # string class 를 출력 <class 'str'>
a = 1
b = 3
#if( a == 1) and \    
    #(b == 3):       # '\' 는 라인을 이어주는 역할
 #   print('connected line')

a = a + 1
print(a)
a += 1
print(a)
#a++    # 얘는 안됨
print(a)