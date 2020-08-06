'''
        Dictionary --> Non - sequence -> Mapping Type  by using Key, approach to Value
'''
'''
member = {'basketball' : 1, 'baseball' : 2 , 'soccer' : 3}
print(member)
member['volleball'] = 7
print(member)
print(len(member))
del member['basketball']
print(member)
# key 의 자료형은 변형 불가능이어야 한다.-> 문자열, 숫자, 튜플
d = { }
d['str'] = 'abc'                # ok
d[1] = 4                        # ok
d[(1, 2, 3)] = 'tuple'          # ok
#d[[1, 2, 3]] = 'list'           #list는 가변형으로 키로 사용될 수 없다/
print(d)
def add(a,b):
    return a+b
def sub(a, b):
    return a-b

# dictionary 사전을 함수의 키나 값으로 활용하는 경우
action = {0:add , 1:sub}
print(action[0](4,5))       # = add(4,5)
print(action[1](4,5))       # = sub(4,5)

dict()
dict(one=1, two=2)
dict( [('one', 1), ('two', 2) ] )
dict( {'one' : 1, 'two': 2})
keys = [ 'one', 'two', 'three']
values = (1, 2, 3)
zip(keys, values)
dict(zip( keys, values))
d = {}
d[10] = (1, 2, 3)
print(d[10])
d[10] = [1, 2, 3]
print(d[10])
d[10] = {1:2, 3:4}
print(d[10])
phone = {'jake' : 123123, 'jim' : 123456, 'Joseph' : 112233 }
print(phone.keys())             # return list
print(phone.values())              # return list
print(phone.items())        # return tuple형태의 로 묶어서 List로 다 출력
#phone.clear()
ph = phone.copy()
phh = phone
print(ph)
print(phh)
phone['jake'] = 1234
print(phone)
print(ph)
print(phh)
print(ph.get('jack'))
print(ph.get('jake'))
print(phone.get('jake'))
print(ph.setdefault('jake', 78))
print(ph.setdefault('jack', 78))
print(ph)
print(ph.popitem())
print(ph.popitem())
print(ph)
ph['jim'] = None
print(ph)
del ph['jim']
print(ph)
''''''
d.clear()   전체 아이템 삭제 , 틀은 남아있다        d.copy()        사전 복사
d.get(key [, x])   값이 존재하면 D[key] , 아니면 return x
''''''
#print(globals())
#print(locals())
class C:
    x = 10
    y = 20
C.a = 100
C.b = 200
#print(C.__dict__)
def f():
    pass
f.a = 1
f.b = 2
#print(f.__dict__)
D = {'a' : 1, 'b' : 2, 'c': 3, 'd' : 4}
print(D.keys())
print(D.values())
print(D.items())
print(D.get('a'))
print(D.get(1)) # Key 로는 Value 에 접근 가능, Value로 키에는 접근 불가능
# 기본적으로 출력시 리시트로 출력, items 는 리스트 안에 튜플들의 집합형태로 출력
for key in D:
    print(key, D[key])          # 3개 다
for key in D.keys():        
    print(key, D[key])          # 같은 코드
for key,value in D.items():
    print(key, value)           # key value  형태로 출력


''' #전화번호 관리 시스템
'''
def print_menu():
    print('1. 전화번호 출력')
    print('2. 전화번호 추가')
    print('3. 전화번호 삭제')
    print('4. 전화번호 찾기')
    print('5. 종료')

def print_dic(nums):
    print("전화 번호")
    for name in nums:
        print("이름 : ", name, "\t번호: ", nums[name])
        print

def add_number(nums):
    print(" add name and number")
    name = input("이름 : ")
    phone_number = input("전화번호 : ")
    nums[name] = phone_number

def remove_member(nums):
    print("Remove name and number")
    name = input("이름 : ")
    if name in nums:
        del nums[name]
    else:
        print("There is not exist Entered number")
def search_number(nums):
    print("search number")
    name = input("이름: ")
    if name in nums:
        print("전화번호 : ", nums[name])
    else:
        print(' There is not exist Entered number')
nums = {}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("원하는 명령의 번호 입력: "))
    if menu_choice == 1:
        print_dic(nums)
    elif menu_choice == 2:
        add_number(nums)
    elif menu_choice == 3:
        remove_number(nums)
    elif menu_choice == 4:
        search_number(nums)
    else:
        print_menu'''

''' # 사칙연산
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
def mod(a,b):
    return a%b

def select_menu():
    print("Select add or sub or mul or div or mod or quit")
    return input('choice : ')
menu = {'add':add, 'sub':sub, 'mul':mul, 'div':div, 'mod':mod}
choice = select_menu()
while choice != 'quit':
    if choice in menu:
        x =  int(input('first value : '))
        y =  int(input('second value : '))
        print(menu[choice](x,y))
    choice = select_menu()'''
'''
set()
print(set)
a = set ( [1, 2, 3, 4, 5, 6])
b = set ( [ 2, 4, 6, 8, 10])
c = set ( [10, 20, 30])
print(len(a))
print( 5 in a)
print(c.issubset(b))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
# union = symmertric_difference + intersection
'''
'''
d = {'odeng':300, 'sundae':400, 'mandu':500}
ob = input("menu")  
if ob in d:
    print(d.get[ob])''''''
def f(x):
    return x*x
x = [1, 2, 3, 4, 5]
for e in map(f, x):
    print(e)  # map은 return list
print()

for e in map(lambda a: a*a , x):
    print(e)
print()
print()'''
print()
x1 = [1, 2, 3, 4, 5]
x2 = [6, 7, 8, 9, 10, 0]
a = map(lambda a,b : a+b, x1,x2)

for e in map(lambda a,b : a+b, x1,x2):
    print(e)
# map 및 zip 합수에서의 파라미터의 갯수가 다를 경우, x1, x2 집합중 원소의 갯수가 작은것에 맞춰서 연산한다.
# 위 연산하면 5번 실행되고, 오류가 출력되지는 않는다.
'''
    f : x->y 도 되는데
    (x1,x2)-> y
    (x1,x2,.....xn)-> y 도 가능
    map : 치역 = map(함수, 정의역)
    map으로 순서쌍 만들기 ->  첫 parameter를 None으로
    map(None, a, b)
    -> a,b가 리스트일때, (a1,b1), (a2,b2)....... 이 됨  -> zip과 무엇이 다른가?
    굳이 1대1대응이 아니어도 됨

'''
t = ()
t = zip( [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12] )    # 굳이 두개의 시퀀스가아니어도 된다
for e in t:                                            # map함수는 return tuple
    print(e)                                           # zip함수는 return tuple
#filter 함수        filter(lambda x:x>2, [1, 2, 3, 4])  filter 함수는 return list
L1 = []
L = filter(lambda x : x>2, [1, 3, 5, 7, 9])
for e in L:
    print(e)
for e in filter(lambda  x: x < 'a', 'asdfgSDFGH12345t'):    # 아스키코드값이 97보다 작으면 출력
    print(e)

for e in filter( lambda x : x%5 == 0 or x%5 == 7 , range(100)):
    print(e)                # 5의 배수와 7의 배수를 걸러서 출력

# reduce 함수       첫인수를 함수로 받고, 2개의 인수를 받아야 하는 함수
#   2번째 인수는 sequence 형이어야한다. 첫 인수에 누적적으로 결과가 적용된다.
#for e in reduce(lambda x, y : x+y , [1, 2, 3, 4, 5]):
#    print(e)
# 없어진 함수?
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
for e in map(lambda x,y : (x,y), a, b):
    print(e)
#a= ''
print('.'.join(str(e**e) for e in range(10)))
#print(a)
