'''import copy
a = ['a1', 'a2', 'a3']
b = ['b1', 'b2', a]
x = [a, b, 'x1']
y = copy.copy(x)
z = copy.deepcopy(x)
print(a)
print(b)
print()
print('x = ', end="")
print(x)
print("y = ", end="")
print(y)
print("z = ", end="")
print(z)
print()
a[1] = 'changed'
print('x = ', end="")
print(x)
print("y = ", end="")
print(y)
print("z = ", end="")
print(z)'''

'''
    얕은 복사   POINTER 까지 복사해서 기존껏을 완전히 가져옴 , 즉 기존의 원소가 바뀌어도 얕은복사하면 바뀐거 적용됨
    깊은 복사   POINTER 복사가 아니라 내용을 복사해서 기존의 원소가 바뀌어도 깊은복사하면 바뀐거 적용안됨
    import copy
    copy.deepcopy(복사할 객체)
'''

'''
import copy
data_a_list = [1,2,3,4,5,6,7,8,9,10]
data_b_list = data_a_list

data_b_list[3] = 55

def func_a(data_list):
    data_list[3] = 55

data_a_list = [1,2,3,4,5,6,7,8,9,10]
func_a(data_a_list)

'''
'''
    < 형변환 >
    int(k)          k 를 int형으로
    round(k)        k 를 반올림해서 int형으로
    math.floor(k)   k를 내림 k가 float형이고, return float
    math.ceil(k)    k를 올림    k가 float형이고, return float
    long type 없음
    complex(k)      k를 복소수형으로 이떄 k는 string or number , not tuple
'''
# sequence DataType Change
#리스트 형변환, 튜플 형변환
t = (1, 3, 5, 7, 9)
l = [2, 4, 6, 8, 10]
s = 'abcd'
'''
print(list(t), list(s))
print(tuple(l), tuple(s))
'''
# 리스트형변환 -> list(변환할 객체) -> return list type(객체)
# 튜플형변화 -> tuple(변환할 객체) -> return tuple type(객체)

'''
        list(객체)  tuple(객체)    str(객체)    repr(객체)  
        str vs repr
        str은 비형식적인 문자열 변환, repr은 형식적인 문자열 변환
'''
'''
print(str(t)+"\n"+ str(l) + "\n" + s + "\n"+ str(s))
print(repr(t)+"\n"+ repr(l) + "\n" + s + "\n"+ repr(s))
# eval(객체) 객체를 리스트로 생성
print()
x = 1
print(eval('x+1'))
# 객체를 문자열로 변환한 후 나중에 그 문자열을 원래의 객체로 변환하기 위해 repr , eval을 사용한다. str은 완벽한변환을 하지 못할때가 있다.(  str(StringType )인 경우)
a = {1:'one', 2:'two'}
b = repr(a)
c = eval(b)
print(type(a))
print(a)
print(type(b))
print(b)
print(type(c))
print(c)
''''''
l = ['파란하늘', 'blue sky', 1, (1,2), 1/3.0]
for s in l:
    print('s', s)
    print('str(s)', str(s))
    print('repr(s)', repr(s))
    print('\'s\'', s)
    print()'''
'''
import string
s = 'python is the first lang'
l = s. split()
print(l)
print('.'.join(l))
''''''
d = {1:'one', 2:'two', 3:'three'}
print(d.keys())
print(d.values())
print(d.items())'''
# 사전에서 리스트로 변환하는 것은 keys, values, items 메소드 활용
'''
#change list to dict
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
l = zip(keys, values)
print(l)
print(dict(l))
'''
# zip으로 mapping을 하고, dict로 사전형으로 형변환 하면 오키
'''
print(chr(65))
print(ord('A'))
print(int(0o64))  # 16진수 0x , 8진수 0o
print(0o64)
print(int(0x64))
print(0x64)''''''
print(hex(100))
print(oct(100))'''
# 10진수에서 2진수로 변환하는 내장함수는 없다.
# 그래서 이건 함수 구현해야함
def decTobin (n):
    if n == 1:
        return '1'
    ans = ''
    while n >= 1 :
        if n == 1:
            ans += '1'
            break
        if n % 2 == 0:
            ans += '0'
        else:
            ans += '1'
        n //= 2
    return ans[::-1]
'''
n = int(input("10진수에서 2진수로 변환할 숫자 입력 : "))
print(decTobin(n))
'''
def decToelse (n, base):
    ans = ''
    while n > 0:
        n,r = divmod(n,base)
        if r > 9:
            r = chr(ord('a') + r -10)   # 나머지가 10을 넘어갈때 
        ans += str(r)
    if not ans:
        ans = '0'
    return ans[::-1]
'''
print(decToelse(70,5))
print(decToelse(70,12))
print(decToelse(70,15))
print(decToelse(70,16))

'''
import locale
locale.setlocale(locale.LC_ALL,"")
print(locale.format("%d", 10030405, 1)) # 무슨 소린지 모르겠다!