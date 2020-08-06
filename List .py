'''
    List는 순서를 가지는 객체들의 집합 sequence, mutalbe, 변경가능한 자료형이 리스트, 사전 뿐이고  스트링,number는 변경이 안됨
    그런데 사전은 key값을 가진 mapping이 된 자료들이 들어가므로, 배열과 같은 1차원 혹은 매핑되지 않은 자료를 변경하려면 리스트를 사용할수밖에없다.
''''''
L = range(10)
print(L)
print(L[::2])
print(len(L))
l = ['a', 'b', '1', '2']
l[0] = l[0] + '1'
print(l)
l[0:2] = {'aa', 'bb'}   #복수 치환하려면 리스트 슬라이싱, 중괄호 안에 자료형 맞게 자료 투입
print(l)
a = [1, 2, 3, 4]
print(a[::2])
del a[0]
print(a)
del l[::2]
print(l)
''''''
# ** 중첩 리스트** 리스트 안에 또다른 리스트가 포함되있는 경우
s = [1, 2, 3, 4]
t = ['a', 'bravo', 'c', s]    # t 는 중첩리스트 s가 t안에 들어가있으므로
# 리스트는 다른 객체를 직접 저장하지 않고 객체들의 레퍼런스를 저장한다. 포인터 형식으로 저장
s[0] = 0;s[2] = 4;s[3] = 6
print(t)'''

'''
        ** List 의 메소드들 **
        1. append       객체를 리스트 끝에 추가
        2. insert       객체를 지정된 위치에 삽입
        3. index        search element
        4. count        # of elements
        5. sort         list sort
        6. reverse      reverse sequence
        7. remove       지정한 객체 한개 삭제
        8. pop          지정한 객체 읽으면서 삭제
        9. extend       list 추가

'''
'''
s = [1, 2, 3]
s.append(5)
print(s)
s.insert(3, 4)  # 3위치에 4 삽입
print(s)
print(s.index(3))   # java 의 indexOf or charAt
print(s.count(2))
#print(s.reverse())  #reverse 는 return 값 없음
s.reverse()
print(s)
s.sort()
print(s)
s = [10, 10, 10, 20, 30, 40, 50]
print(s)
s.remove(10)        # 10이 여러개 있으면 제일 앞에꺼 하나만 삭제됨
print(s)
s.remove(10)
print(s)
s.remove(10)
print(s)
s.extend([100, 200, 300, 400])  # 주의) extend는 1개의 argument 를 갖기 때문에 [] 안에 리스트형태로 넣어서 다수를 입력하면 된다.
print(s)
'''
'''# List를 Staack처럼 사용
s = [10, 20, 30, 40, 50]
s.append(60)
print(s)
print("List append method is similar with stack push method")
s.pop()
print(s)
print(s.pop())  # pop 하면서 the element which pop is memorized 
# 현재 시점의 s = 10, 20, 30, 40, 50 
# 만약 여기서 s.pop 을 한다면 50이 뺴내지겠지만 좀더 응용해서
print(s.pop(1))    # 하면 앞에서 부터 두번째 자료를 빼냄 뒤에서가 아니네
print(s)
#   pop() 연산시 괄호 안에 매개변수 없으면 맨뒤에꺼를 추출, 매개변수를 넣는다면 list의 인덱스처럼 앞에서 부터 indexing
def mycmp(a1, a2):
    return cmp(a2, a1)
l = [1, 6, 2, 5, 3, 8, 9]
print(l)
l.sort()
print(l)
#l.sort(mycmp) 이거 안되네
def cmp1 (a1, a2):
    return cmp(a1[1]), a2[1]

def cmp2 (a1, a2):
    return cmp(a1[2], a2[2])
L = [ ('lee', 5, 38), ('kim', 3, 28), ('jung', 10,  36) ]
l.sort()
print("sorted by name : ")
print(L)
for e in l:
    print(e)
l.reverse()
print(l)
l.reverse()
print(l)
for e in reversed(l):
    print(e)
l = [k*k for k in range(10)]
print(l)
a = []
a = ' '.join( str(e) for e in range(10))
print(a)
L = [k*k for k in range(10) if k%2] #  짝수인 것에대해 k*k를 출력하는 loop
print(L)
t = ()
L = [(i, j, i*j) for i in range (2, 20, 2) for j in range(3, 30, 3) if(i+j) % 7 == 0 ]
#  for i in range (2, 20, 2) 2의 배수 i , for j in rnaage(3, 30, 3) 3의배수 ,  둘을 더했을때 7의 배수가 되는 i,j,i*j 리스트
print(L)
s1 = 'abc'
s2 = (1,2,3)
L = [ (x,y) for x in s1 for y in s2 ]
print(L)
L = [ 'x,y' for x in s1 for y in s2 ]
print(sum( [x*x for x in range(10)]))
q = 0
for x in range(10):
    q += x*x
    print(x, x*x, q)
g = ['is not unix']
g.insert(0,g)
print(g)
print(dir())        # 지금 지역변수로 사용가능한 것들 리스트안에 문자열들 원소로 출력
''''''
a = [1,2,3,4,5]
b = range(10)
print(a, b)
n = [20, 15, 39, 2, 7, 5, 223, 75, 46, 87]
m = [3, 5, 9, 2, 7]
l = [None] * 10
for k in m:
    l[k] = k * n[k] # m의 첫번쨰원소 3에 대해  3*2 = 6 -> n[3] , m의 2번쨰원소 5에 대해  5*n[5] = 25 -> l[5]
print(l)
mat = [ [1,2,3]],
        [4, 5, ]
''''''
from functools import cmp_to_key
def mycmp(a1, a2):
    return -1
l = [1, 2, 4, 8, 16, 15, 10, 5]
b = sorted(l, key=cmp_to_key(mycmp))            # 1     2     4    8      16     15   10      5
print(b)
print(l)
l.sort(key=cmp_to_key(mycmp))                   #      1    2   4       8       -1  -5      -5
print(b)
print(l)
# 원하는 기준으로 정렬을 하고싶은데
# 일단 이렇게 하는 틀은 알겠는데
# mycmp 함수에서 a1<a2 든 abs(a2-a2) 든 기준을 뭘로 해도 return값이 1 또는 -1이 되는거 같아서
# 출력 하면 
     '''   '''
L = [k*k for k in range(10) if k % 2 != 0]
print(L)
L = [None] * 10
print(L)
mat = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
MAT = [ 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(mat)
print(mat[1][2])
print(MAT)
print(MAT[1][2])    #같다

# 0으로 초기화하는 올바른 예제
Mat = []
for x in range(3):
    Mat.append([0] * 4)
Mat[0][0] = 1
print(Mat)'''
'''
# 잘못된 예제       이렇게 초기화하면 레퍼런스의 복사를 통해 참조값에 따라 객체의 값이 다르다
WrongMat = []
WrongMat = [ [0] * 4] * 3
WrongMat[0][0] = 1
print(WrongMat)'''
'''
# 0으로 초기화하는 올바른 예제
mat = [ [0] * 4 for x in range(3)]
mat[0][0] = 100
print(mat)
from array import *
a = array('i', range(10))
print(a)    # print -> array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a = array('i', [0] * 10)
print(a)
a = array('i')
a.append(1)     # 1  
a.append(4)     # 1 4
a.insert(1,2)   # 1 2 4
a.extend(array('i', [1, 2, 3, 4, 5]))   # 1 2 4 [1,2,3,4,5]
print(a)'''
# i is typecode
'''
import glob
import os
print(os.path.getsize('List .py'))  # 파일의 크기
import time
t = os.path.getatime('List .py')    #파일의 최근 접근 시간 1970년 1월 1일 자정 ~ 현재까지 경과한 초이다.
print(t)
print(time.ctime(t))
print(time.ctime(os.path.getmtime('List .py')))
L = [1, 2, 3, 4, 5]
L[1:3] = [100]
print(L)    # print -> [1, 100, 4, 5]
L = [1, 2, 3, 4, 5]
#L[1:3] = 100   오류 뜸
print(L)
a = [1, 2, 3]
a[:] = [4,5,6]
print(a)
#단어의 순서가 바뀌도록 출력 -> split해서 list로 받고, 그 list print reverse
s = "somethimes i feel like a motherless child"
list = s.split(" ")
print(list[::-1])   # child motherless a .......

# want to print dlihc ssel .....
List = []
for e in list:
    List.append(e[::-1])
#print(List)
print(List[::-1])   # dlihc, ssel.....
# split 과 join을 이용해 문자열에서 공백을 모두없앤 문자열
list = s.split(" ")
str = ''.join(list)
print(str)
a = [1, 2, 3, 4]
c = [a] * 3
ca = [a[:]] * 3
b = a*3
print(c)
print(ca)
print(b)
print("\n")
a = [1,2,1,2]
print(c)
print(ca)
print(b)
print("\n")
s = 'first : second : third  '
# 식 for element in 객체 if 조건
e = [ d.strip() for d in s.split(":")  ]        # 리스트 내장 한번에 출력
# 출력할 객체 = [ for문안에서의 실행문 for 요소 in 객체 if (조건)]
print(e)

## Tuple ##
t = ()
t = 1, 2, 3 # 괄호를 하지 않아도 콤마로 시퀀스형 자료를 입력하몀 자동으로 튜플로 처리된다.
print(t)
r1 = 1          # numbers
r2 = (1)        # numbers
r3 = 1,         # tuple
r4 = (1,)       # tuple         결론 : 튜플형 자료는 괄호가 없어도 쉼표는 있어야한다
print(r1);print(r2);print(r3);print(r4)
t += ('a',)
print(t)
#튜플은 변경할수없다. 리스트랑 사전만 가능
x = 1
y = 2
print(x,y)
x,y = y,x
print(x,y)
t = 1, 2, x, y, 'abc', '123'
print(t)
a = ['foo', 'bar', 4, 5]
[x,y,z,w] = a
print(a, x, y, z, w)
T = (1, 2, 3, 4, 5)
L = [T]
#L[0] = 1003
print(L)
T = tuple(L)
print(T)'''
#           ** 튜플을 사용하는 경우**
# 1 함수에서 복수의 값을 return 하는 경우
def cal(a, b):
    return a+b, a-b
x,y = cal(5, 4)
print(x,y)

# 2 문자열 포맷팅
print("id : %s, name : %s" % ('Kiwoom', 'Heroes'))

# 3 ,튜플의 값을 함수의 매개변수로
args = (4,5)
print(cal(*args))   # 포인터니까

d = {'one': 1 , 'two' : 2}
print(d.items())

import os
p = os.path.abspath('List .py')
print(p)    #  경로 출력 해당 파일의 위치 및 경로
print(os.path.exists(p))    # 존재시 T
print(os.path.getsize(p))
print(os.path.split(p)) # directory , fila name

# URL parse  url 분리해서 리턴
from urllib.parse import urlparse
a = 'https://dojang.io/mod/page/view.php?id=2285'
print(urlparse(a))

t = (1,2,3,4)
s = t[:2] + t[3:]
print(s, t)

Sun, Mon, Tue, Wed, Thu, Fri, Sat = range(7)
print(Sun, Mon)
weekday = input("요일 입력 Sun/Mon/Tue/Wed/Thu/Fri/Sat")
print(weekday)

