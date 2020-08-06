# 반복되는 수행, 논리적 개념 독립화

# 특별한 의미를 갖는 식 을 별도로 추출하는 것으르 Factoring 
'''
import math
x1 = ( -b + math.sqrt(b*b - 4*a*c)) / (2.0 * a)
21 = ( -b - math.sqrt(b*b - 4*a*c)) / (2.0 * a)
D = math.sqrt(b*b-4*a*c)
a1 = 2.0 * a
x1 = -b + D / a1
x2 = -b - D / a2'''
'''
'''
def add (a,b):
    return a+b
'''
def addabs(a, b):
    c = add(a,b)
    return c'''
'''
    def 함수명 ( parameters ....):
        statements
        쭉
        쭉
        쭉
        return value
    함수이름은 함수 객체의 REference 를 가지고 있다  -> 함수포인터 개념


'''
'''
print(add)  # print add함수가 메모리의 어떤 주소에 있는지
def nothing ():
    pass
nothing()
print(nothing())    # print None
'''
'''
def add_member(member_list, new_member):
    if type(new_member) not in ( type([]), type(())):
        new_member = [new_member]
    if new_member not in member_list:
        member_list.append(new_member)

member_list = ['박병호', '김하성', '김혜성', '킹갓이정후', '브리검', '요키시']
add_member(member_list, '조상우')
add_member(member_list, '안우진')
print(member_list)
member_list.remove('박병호')        # delete element in list, listname.remove('value which wnat to del')
print(member_list)
member_list.pop()
print(member_list)  # del at the top of stack / last index of list
add_member(member_list, ['박동원', '허정협', '전병우'])
print(member_list)
''''''
def f(t):
    t = 10
a = 20
f(a)
print(a)'''
'''
    파이썬은 함수를 호출할때 래퍼런스를 넘겨준다.

'''
'''
def noreturn():
    return
print(noreturn())   # print None        None 도 객체임 아무것도 없음을 나타내는 객체
a = noreturn()
print(a)    # print None
'''
# return 은 어떠한 객체도 넘길 수 있다.  안넘길거면 return 안써도 된다
'''
def print_menu():
    print('1. a')
    print('2. b')
    print('3. c')
print(print_menu())
'''
# 리턴값이 존재하지 않을때  None을 return 한다. 리턴값이 존재하지 않을때 언제나 None 객체를 return 한다
# 1개의 값을 return 할때
'''
def abs(x):
     if x < 0 :
         return -x
     return x   # 1개의 return 값       return 그값
x = int(input("정수 입력 : "))
print(abs(x))
'''
'''
def swap(x,y):
    return y, x         # 이렇게 하면 튜플로 리턴된다.
a = int(input("정수 1 입력 : "))
b = int(input("정수 1 입력 : "))
a,b = swap(b,a)
x = swap(a,b)
print(x)
'''
#print(divmod(10,3))
'''
def len_list(l1):               # 리스트를 받아서 , 리스트의 원소의 길이를 리스트로 반환
    res = []
    res1 =[]
    for e in l1:
        res.append(len(e))
    for e in l1:
        res1.append(e)
    return res, res1
li = ['1', '12', '123', '123123', '123123123']
print(len_list(li))
'''
'''
li = ['1', '12', '123', '123123', '123123123']
print([s for s in li])  # li 리스트 안의 원소들을 순서대로 출력
print()
print([li for s in li]) # li리스트 전체를 리스트의 길이만큼 출력
'''
'''c = add(1, 3.4)
d = add('dynamic', 'typing')
e = add(['list'], ['and', 'list'])
print(c, d, e)
'''
# 스코핑 룰
'''
        Local       Global      Built-in(Scope)
        함수        모듈(파일)  파이썬에서 정의한 내용
        
        LGB Rule
        Local, Global, Built-in 우선순위가 L > G > B 이다.
'''

g = 10
h = 5
def f(a):
    h = a + 10
    b = a + g
    return b
# g, h는 전역에 속하고 a,b는 지역   h의 경우에는 함수 안에서는 지역변수 h, 밖에서는 전역변수 h로 사용
#예시
# 안좋은 예시
g = 10
'''
def qw (a) :
    a = g
    g = 20
    return a'''
#print(qw(g))
#좋은 예시
'''
def we (a) :
    global g
    a = g
    g = 20
    return a
print(we(g))
global k = 20
def er (a) :
    a = k
    return a
print(er(k))
#print(dir(__builtins__))
'''
'''
def f(x):
    def g(i):
        print(i)
        if i:
            g(i-1)
    g(x)
print(f(3))         # print 3   2   1   0   None

''''''
def varg(a, *arg):
    print(a, arg)
print(varg(1))              # 공튜플
print(varg(1,2))
print(varg(1,2,3))
print(varg(1,2,3,4))
print(varg(1,2,3,4,5))

def printf(format, *args):
    print(format % args)
printf(" I've spent d days and %d night to do this", 6, 5)
'''

'''def f(w, h, **kw):
    print(w, h)
    print(kw)
print(f(w = 10, h = 5 , depth = 10, dim = 3))   # depth와 dim 이 사전형ㅌ로 입력받아짐
'''
'''
def g(a, b, *args):
    print(a,b)
    print(args)
    print(kw)
print(g(1, 2, e=3, f=4, c=5, d=6))          # args 가 tuple형으로 받는다
print('------------------------------------------')
print(g(1, 2, (3, 4), c=5, d=6))
'''
''' #튜플인수, 사전인수, 함수호출
def func(name, last_name, **qw):
    print(name)
    print(last_name)
    for key, value in qw.items():
        print("%s -> %s" % (key, value))

dic_a = {'name':'kim', 'last_name':'las', 'age':'10'}
'''
name = 'kim'
last_name = 'las'
age = '10'
'''
func(**dic_a)'''
#func(name=name, last_name=last_name, age=age)
# tuple -> 1개 매개변수, dict -> mapping된 식형태의 매개변수

'''
    fkaekgkatn gkswnfWKfl
    dlfmadl djqtsms gkswnfWKfl gkatn
    lambda 콤마로 구분된 인수들: 식
    받는 인수가 없고, 언제나 1을 리턴->     lambda:1
    
'''
#g = lambda x, y: x+y    # 이 자체가 함수
#print( g(1,2))

inc = lambda x, inc=1 : x+inc
print(inc(10))
print(inc(10, 5))

vargs = lambda x, *args: args

print(vargs(1,2,3,4,5))
'''
            input               output
            1,2                 2
            2,3                 3
            3,4                 4
            4,5                 5
'''
lk = lambda x, *args, **kw: kw
print(lk(1, 2, 3, a=4, b=5, c=6))
'''
            1               ->  x              
            (2,3)           ->  *args
            a=4, b=5, c=6   ->  **kw
''' 
# 함수를 인수로 Func( func)

def f1(x):
    return x*x + 3*x - 10
def f2(x):
    return x*x*x
#def g(func):
    #return [func(x) for x in range(-10, 10)]
#print(g(f1))       # x = -10 ~ 9  정의역에 대해 f1(x)
# 합성함수
# 위와 같은 내용구현해보면      lambda parameter : result , 함수래퍼런스를 리턴
def g(func):
    return [func(x) for x in range(-10,10)]
g(lambda x: x*x + 3*x - 10)
g(lambda x: x*x*x)
print(g(f1))
'''
    람다 함수는 식이다. 함수 선언과 함께 함수 인수로 전달하는것이 가능하다.
'''
