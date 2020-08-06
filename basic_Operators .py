'''list = ["-3", "3", "-20", "10"].
for k in range(len(list)):
    if int(list[k]) < 0:
        print(list[k])
''''''
list = ["-3", "3", "-20", "10"]
for k in list:
    if int(k) < 0:      # 위와 같은 코드
        print(k)
''''''
list = ["-3", "3", "-20", "10"]
for k in list:
    if int(k)%3 == 0:   # 3의 배수 출력
        print(k)'''
'''list = [13, 6, 2, 21, 1, 12, 14, 30, 18, 333]
for k in list:
    if int(k) < 20 and int(k) % 3 == 0:
        print(k)        # 20보다 작은 3의 배수들 출력, for k in list - list[k], k=0~len(list)       // for k in range(len(list)) k = 0~len(list)
'''
'''list = ["I", "study", "python", "language", "!"]
for k in list:
    if len(k) < 3:  # 길이가 3보다 작은 리스트의원소들을 출력 k = list[i], i = 0 ~ len(list)
        print(k)'''

# is 와 == 의 차이  is는 포인터(reference) 를 비교, == 는 값(value)을 비교
'''a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = [1,2,3]
print(a == b)   # b = a 로 a의 모든 것을 복사했으므로 b는 a와 같은 값
print(a is b)   # b = a 로 a의 모든 것을 복사했으므로 b는 a와 같은 객체
print(a == c)   # c는 a과 같은 크기, 같은 원소들을 가졌으므로 같은 값
print(a is c)   # 하지만 b처럼 a와 같은 리스트객체가 아니다. 따라서 이 부분은 false
print(a == d)   # spacebar 가 없어도 list의 크기, 원소의갯수, 원소의 값들 은 같다. T
print(a is d)   # c와 같은 이유로 False'''    
'''
list = ["A", "b", "C", "d"]
for k in list:
    if k.isupper():     # 변수.isupper() 변수가 대문자이면 return True
        print(k) '''
'''list = ["A", "b", "C", "d"]
for k in list:
    if k.islower(): # 변수.islower() 변수가 소문자이면 return True
        print(k)'''
'''list = ["A", "b", "C", "d"]
for k in list:
    if k.isupper() == False: # 위와 같은 코드  대문자 가 참이 아니면 거짓이라는 뜻 != True 로 해도 같은뜻
        print(k)'''
'''list = ["A", "b", "C", "d"]
for k in list:
    if not k.isupper(): # 같은 뜻   not 변수.isupper 변수가 대문자가 아니면 true이므로
        print(k)'''
'''
import sys      # 파이썬 버전 출력 3.8.5 2020,7 20
print(sys.version)'''
'''import calendar
calendar.prmonth(2020,8)    # 2020-8월 달력 출력 calendar.prmonth(연도, 월)
''''''
a = 1;b= 3
    if (a == 1) and \'\' 는 앞뒤라인 연결
    print("ok")'''
'''a=1;b=2
a,b = 3,4   # 복수개로 치환 가능
print(a,b)
a,b = b,a
print(a,b)  # 교홛 가능
a <<= 2     # a *= 4
print(a,b)
a **= 2     # a의 제곱
print(a,b)
'''
'''a = [1, 2, 3]
b = [10, a, 20]
c = [a, b, 30]
print(a)
print(b)
print(c)    
a[0] = 11       #call by reference
print(a, '\n', b, '\n', c)
b = [10, a, 20]
c = [a, b, 30]
print(a, '\n', b, '\n', c)'''
'''
a = 1
a = eval('a+4') # 문자열로 된 식 을 실행 ( = 가없는 한쪽)
print(a)'''
'''a = 5
print(a)
exec( 'a +=4 ') #문자열로 된 문을수행    ( = 가 있는 양쪽)
print(a)'''
'''code = compile('a+1', '<string>', 'eval')
a = 1
for k in range(10):
    a = eval(code)
    print(a)'''
'''name = input('name =')   # 콘솔 입력 (br)
print(name)'''
'''k = input('input : ')
print(k)
print(int(k))'''
#print( 12 + 'a')    # 문자와 숫자 간에 + 는 없다
print('12' + 'a')   # 문자 간에는 가능
import pprint
complicated = ['spam', (1, 2, 3), ('ham', 'egg', ('ab', 'cd', 'ef'), '1')]
complicated *= 3
pprint.pprint(complicated)
# pprint 문이 복잡한 자료를 출력할때 사용
print("위는 pprint , 아래는 print")
print(complicated)
# pprint 는 형식이 유지된채로 반복출력 , print는 이어서 출력
