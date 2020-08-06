'''
Python 의 자료형에는
Numbers ( 수치형) - int, long, float, complex   -   Direct Datatype
Strings - cannot changed
Lists - Object's group which have sequence []
Dictionaries = Object's group which have sequence and pickup by Key value
Tuples = Object's group which have sequence and cannot changed ()
File - for i/o

'''

#문자열 ' ' or " " 안에 묶인 문자들의 모임
a = "I am studying Python lang"

#by indexing
'''for k in range(len(a)):
    print(a[k])'''     # a[index] = 문자열 인덱싱 -> split
#by Slicing
'''print(a[1:3])       # print a[1], a[2]                    ' a'
print(a[0:5])       # I am  04                           'I am'
print(a[2:-1])      # 2번~ -1번  2번이 a니까 a부터 끝까지 ' a' ~ -1번쨰전(-2번쨰)까지 니까 'n'까지
print(a[1:])    # 1번부터 끝까지 출력
print(a[:3])    # 0 1 2 번쨰까지 출력
print(a[:]) # 전체 출력
'''
'''
Slicing  start : stop : step
start ~ stop   , step 은 몇단계를 건너뛸까   
이들은 문자열, 리시트, 튜플에 모두 적용된다. ( dic 에는 안된다? -> div은 key로 추출하므로 ?)
기본적으로 생략되었을시 start = 0  , stop = len(자료형), step = 1
'''
'''s = 'abcdefg'
print(s[::2])   # 2칸 단위 출력 'a, c, e, g'
print(s[::-1])      #거꾸로 출력 'gfedcba'
print('hello' + 'World')
print('hello', 'World')
#문자열은 값이 변경되지 않는다.
#  s[0] = z 이건 오류난다
#변경하려면 슬라이싱해서 연결해야한다.
print(s)
s = 'z'+s[1:]
print(s)
print(len(s))
s = 'Hello World'
print('World' in s) 
print('World' not in s) 

'''
'''s = "Hello World"
s = "World " + s[0:5]
print(s)
'''
'''x = 'abcde'
x = x[1:]+'a'
print(x)

# about List
L = [1, 2, 3, 4]
print(len(L))
print(L[1],"\t", L[-1])
print(L[1:-1])
del L[0]
print(L)
L.reverse()
print(L)
L.sort()
print(L)
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(len(t))
print(t[0], "\t", t[1], "\t", t[-1])
print(t[0:2])
print(t[0::2])      # 홀수만 출력
t = t+t
print(t)
t *= 2
print(t)
print ( 3 in t)
'''
'''
< 튜플과 리스트의 차이 > 
튜플은 값이 변경 안된다, 리스트는 변경할 수 있다.
리스트는 다양항 메소드를 갖는다, 튜플은 그렇지 않다.
'''

#<dictionary>   -   Mapping Type
d = {'One':'hana', 'Two' : 'dul', 'three' : 'set'}
print(d['One']) # print hana
d['four'] = 'net'
print(d)
print('one' in d)
print('One' in d)
# dictionary not mentioned about sequence, since we pop element with key value
# so not need to sort or sequence
# also  we can type change to tupe or list
print(d.keys())
print(d.values())
print(d.items())    # (key, value)

# List, Dictionary  Mutable
# Numbers, String , Tuple ImMutable
# 문자열, Numbers 는 1가지의 type 만 넣을수있따 문자열은 문자열, 넘버는 넘버
# 그러나 list, 튜플 dic 은 그렇지 않다 .
di = {'one':'1', '2':'Two', '3': '3!4!', 'singer':"Lula"}
print(di)
List = [1, 2, 3]
List[0] = 0
print(List) # 리ㅅ트는 값을 변경할 수 있다.
'''import types     35가지의 자료형이 있다고 한다
print(dir(types))'''    
print(type({}))     # class dict
print(type(3))      # class int
print(type(''))     # class str
print(type(None))   # class NoneType
print(type([]))     # class List
print(type(()))     # class Tuple
print(type(type(())))   # class type
'''

모든 객체들은 Reference Count 값을 갖고있다.
 얼마나 많이 객체가 참조되고있는가
 특정 객체가 Reference count 가 0이 되면 즉 참조되지 않은 객체이면
 자동으로 Garbage Collection
 reference count 알아내는 방법은 import sys 하고 sys.getrefcount(객체) 하면 된다.
'''
print(id(List))     #id(객체) = 해당 객체의 주소값 return , if 객체의 id가 동일하다면, 같은 객체를 참조하는것
print(id(tuple))
a = 500
b = 500
c = a
print(id(a))    #같은 객체를 참조하므로
print(id(b))    # 참조하는 객체의 주소값이같다.
# 같은 객체를 참조하는지 확인하는 방법
print( a is b)
print( c is a)
x = [1, 2, 3]
y = [1, 2, 3]
print(id(x))        # 리스트의 원소의갯수, 원소들의 값이 같아도
print(id(y))        # 그들이 참조하는 리스트는 다른 리스트 [1, 2, 3] 이라는 리스트가 2개가 생성되고 각각 참조하는것
s = t = [1,2,3]
print(id(s))        # 이렇게 참조해서 받으면 같은 객체를 참조한다.
print(id(t))
