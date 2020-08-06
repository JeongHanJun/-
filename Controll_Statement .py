# if    for     while
'''if 조건:
    실행할 문
elif:
    실행할 문
else:
    실행할문'''
'''
a = int(input("숫자 입력:"))
if a > 0:
    print(" a is possitive")
elif a < 0:
    print(" a is negative")
else:
    print("a is zero")
'''
'''list = ['a', 'ab', 'abc']
for x in list:
    print(len(x), x)
for x in [1, 2, 3]:     # 얘는 index를 출력하는거고
    print(x)
for x in list:          # 얘는 list의 값들을 출력하는거고
    print(x)
sum = 0;con =1
for x in range(1,11):
    sum = sum + x
    con = con * x
print(sum , con)'''
'''l1 = ['cat', 'dog', 'bird', 'pig']
for k, animal in enumerate(l1):
    print(k, animal)
    # enumerate(index, value) index 와 value를 둘다 출력
'''
'''for x in range(10):
    if x > 3:
        break
    print(x)        break는 블록 탈출, continue는 나머지 내용수행안하고 반복문 초기부분으로 이동
print('done')
''''''
sum = 0
x = 0
while(x < 10):
    x += 1
    sum += x    # 반복문 제어는 break, continue, else
print(sum)      #             반복문탈출, 아래무시하고 다시 위로, 반복문내용이 참이아닌경우

def funcname( parameter):
    statement'''
'''def add(a, b):
    return a+b
print(add(4,4))''''''
s = 'python'
print(s[0][0][0])
print(s[1:-1])  # 1 ~ -1-1 이니까 1 ~ -2까지
print(s[3:-3])  # [3] = 
s = 
''' 
'''we propose to start by making it posiible to teach programming in python.
as existing scripting language, and to focus on creaging a new development environment and teaching materials for it'''
'''
li2 = s.split()
print(li2)
li2.sort()
print(li2)      
'''
'''
list 의 sort는 우선 list원소의 길이가 작은 순서, 그리고 알파벳순
'''
'''
a = 0;b = 0
exec('a = b+1') # exec 는 문자열로 된 파이썬 문장을 실행
print(a, b)

import sys
print(sys.maxsize)  # maxsize 는 있고
print(sys.maxunicode)# maxunicode도 있는데, maxint는 없다
#print(sys.maxint) 이거 없음

#long type은 정수의 끝에 l을 붙여서 표현한다.
a = 123456789123456789123456789123456789
print(type(a))
a = 123456789123456789123456789123456789L
print(type(a))'''
'''c = 4 + 5j
d = 7 -2j
print(c*d)
e = 0.0
for k in range(100000):
    e += 0.00001
print(e)
import decimal
r = decimal.Decimal('0.0')
de = decimal.Decimal('0.00001')
for k in range(100000):
    r += de
print(r)
print(divmod(5, 3)) #몫 1, 나머지 2 (1,2)가 출력됨
print(-7/4)
print(-(7/4))   #둘다 -1.75나온다
''''''
print('abcd' > 'abc')
print( (1, 2, 4) < (2, 1, 0))
print( (1, 2, 3) == (1, 2, 3))
print( (1, 2, 3) != (1, 2, 4))  # 사전순서, 앞에서 부터 하나씩 비교

연산자 우선순위 : 식 >> 함수호출/슬라이싱/첨자 >>  not > 단항연산자 > 곱,나누기,나머지 > 다항연산자 > shift > 비교연산자
''''''
# Math
print(abs(-3))
for x in range(97, 123):
    print(chr(x), end = " ")    # 아스키코드 97 ~ 122 소문자 출력
print("\n")
for x in range(65, 91):
    print(chr(x), end = " ")    # 아스키 코드 65 ~ 91 대문자 출력
print("\n")
print(ord('a'), ord('A'))       # 아스키 코드값 출력
print("\n")
x = 3
print(float(x))
print(complex(3.4, 5)) # 3.4 + 5j
print(pow(2, 3) == 2**3)
'''

'''     #비트연산자를 이용해 입력받은 숫자의 홀/짝 구분, 비트연산한 횟수 출력
cnt = 0
a = int(input("정수 입력"))
k = a & 0x01
while True:
    a >>= 1
    cnt += 1
    if a < 2:
        break
if k == 0:
    print("a는 짝수", a, cnt)
else:
    print("a는 홀수", a, cnt)'''
'''a = int(input("intput: "))
high = a>>4 & 0x0f
low = a & 0x0f
a = ~a + 1
print(a)
if a > 0:
    print("a 는 음수입니다")
else:
    print("a 는 양수입니다")
print(high, low)'''



'''
a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))                   # 1 2 1 ->  -2 + ( ( 2*2 - 4*1*1) ** 0.5) / (2*1) = -2 + 0/ 2
x1 = -b + ((b*b) - (4*a*c)) ** 0.5 / (2*a)
x2 = -b - ((b*b) - (4*a*c)) ** 0.5 / (2*a)
t= (x1, x2)
print(t)'''
'''
L1 = [1, 2, 3, 4, 5]
L2 = [2, 4, 6, 8, 10]
print(L1)
print(L2)
for k in L1:
    if k in L2:
        continue
    else:
        L2.append(k)        # List 2개 비교하면서, 없으면 append하기
print(L2)''''''
s = 'abcde'
print( c in s)
'''
'''
a = []
a = ", ".join((str(cnt) for cnt in range(1, 10)))   # 반복문 없이 한번에 객체에 특정 객체들의 sequence 집합을 추가하는 법 
print(a)

str = 'don\'t worry'    # 이스케이프 문자
print(str)
'''
'''
for c in 'abcd':    # 이거 오류 안남 for문의 타겟 c는 문자열안의 abcd의 c와 관계가 없다. 
    print(c)        # 타겟 c에 대해서 출력하는 것  , 즉 같은 c라는 값의 객체여도 주소값이 다르고, 역할이 다르다(하나는 타겟, 하나는 문자열안의 c)
    ''''''
s = "tomato Spaghetti"
s = s[:6] + ' cheese ' + s[7:]
print(s)
s = 'spam and egg'
s = s[:4] +" "+ s[9:]
print(s)'''
#format = 'name = %s , age = %d'
'''
#letter = '''
#안녕하세요 %s님,
#오늘 밤 파티에 참석해 주실 수 있나요?
#그럼 이만 ...
#Kiwoom Heroes '''
#names = ['브리검', '요키시', '러셀']
#for name in names:
#    print(letter % name)
#    print('_' * 40)'''
print("%s -- %s -- %d -- %f -- %e" % ( (1, 2), [3, 4, 5], 5, 5.3, 101.3))
# 위 식 출력시 (1,2) -- [3, 4, 5] -- 5 -- 5.3000000 -- 1.0130000e+02
# 양식에 해당하는 부분을 문자열 사이에 끼워놓고, 그 값은 %기준으로 오른쪽에 입력하면 그 값이 양식에 맞쳐서 출력됨
# 이것이 문자열 포맷
print('name = %s, age = %s' % ('gslee', '24'))
print('name = %s, age = %d' % ('gslee', 24))

a = 1234
print("%d -- %o -- %x -- %X" % (a, a, a, a))
'''
<참고> 
%s = String (use str() func to TypeChange)    %r = String (use repr() func to TypeChange)
%c = len = 1 인 chr                           %d = decimal
%u = unsigned integer                         %o = 8진수
%x = 16진수                                   %e = 부동소수점을 지수형태로 표현 , 유효숫자 자리는 7자리
%f = 부동소수점을 실수형태로  
'''
'''
# Formatting using Dictionary
print("%(name)s -- %(phone_number)s" % {'name':'Jake', 'phone_number' : '010-1234-5678'}) 

#모든 변수는 사전 형식으로 저장된다?
# vars() or locals()
name = 'HanJun'
phone = 3672
print("%(name)s -- %(phone)s" % vars()) # HanJun -- 3672 이라고 출력됨'''
'''
import string
t = string.Template('$page : $title')
t.substitute({'page': 2, 'title': 'The Best'})
print(t)
'''
'''s = 'python Programming'
print(s)
print(s.upper())
s = 'Python Programming'
print(s.lower())
s = 'Python Programming'
print(s.swapcase())
s = 'Python Programming'
print(s.capitalize())   # 첫문자만 대문자로
s = 'Python Programming'
print(s.title())
'''
'''s = "Programming lang python, java, c++ are popular"
print(s.count('p')) # p 라는 substring의 발생 횟수 리턴 대소문자 구별
print(s.find('python')) # index 검색 
print(s.find('Pro', 3)) # 없음 return -1
print(s.find('are', 3)) # 3번쨰부터 검색
print(s.rfind('lang'))  # find 와 같지만 문자열의 뒤부터 검색해서 return index
print(s.startswith('P'))    # 무엇으로 시작하는가? return t/f
print(s.endswith('r'))      # 무엇으로 끝나는가?   return t/f? 
print(s.startswith('lang', 12)) # 12번째 문자열이 lang 으로 시작하는가 - T
'''
s = "  spam   and  ham  "
print(s.strip())                # 좌우 공백 없애기
s = "  spam   and  ham  "
print(s.rstrip())               # 오른쪽 공백 없애기
s = "  spam   and  ham  "
print(s.lstrip())               # 왼쪽 공백 없애기
s = "  spam   and  ham  "
print(s.replace('spam', 'egg')) # spam 을 egg 로 치환하기
s = "  spam   and  ham  "
print(s.split())                # 공백으로 분리
s = "  spam   and  ham  "
print(s.split('and'))           #and를 기준으로 분리
s = "  spam   and  ham  "
t = s.split()                   # 분리한것들을 t에 저장해서 이들을 : 기준으로 join 해서 출력
print(':'.join(t))
print(' : '.join(t))            # 이렇게 하면 보기 더 편하다
                                #join은 '기준문자'.join(리스트)  기준문자란, 리스트의 문자열들을 연결하는 문자열
line = ''' first line
second
third
fourth end of line'''
print(line.splitlines())

s = "  spam   and  ham  "
print(s.center(60))     # 60문자 기준 가운데에 정렬
print(s.ljust(60))      
print(s.rjust(60))

print('1234'.isdigit())     #   t
print('1234'.isalpha())     #   f
print('1234'.isalnum())     #   t
print('abcd'.isdigit())     #   f
print('abcd'.isalpha())     #   t
print('abcd'.isalnum())     #   t
print('1234abcd'.isalnum()) #   t
#alnum 은 숫자 혹은 영문자
s = '''
first line
second line
third line
'''
t = s.splitlines()
st = ':'.join(t)
print(st[1:])           ## 그냥 출력하면 :first~~ 로 되서 안이뻐서 이렇게

str = st.split(':')             # 분리해서 중간라인 첫번쨰 단어를 빼올거임
print(str[1].split(" ")[0])    # 분리하고, " "로 분리해서 첫번째 단어뺴옴
print(str)
'''
str.split -> return list

'''
# 156pg 3번  i want to print like 'first:line:second:line:third:line'
print(s)
s1 = s.replace("\n", "", 1)
s2 = s1.replace(" ", ":")
s3 = s2.replace("\n",":", 2)
s4 = s1.replace("\n"," ").split(" ")    # s4는 리스트임 split한 결과는 list를 return 하므로
print("--------------------")
print(s1)
print(s2)
print(s3.strip())   # s3 is ok
print(s.replace("\n", "", 1).replace(" ",":").replace("\n",":",2).strip())  # 순수 문자열로만 연산하면 위랑 똑같음 , 좌우공백 없애는 strip  , java에서 trim과 같은
print(s4)   # ['first', 'line', 'second', 'line', 'third', 'line', '']
s5 = ':'.join(s4)
print(s5[:-1])                                                              # 문자열 메소드를 통해 리스트로 분할하고 이들을 join 하면 편함
''' ** 문자열 붙이는 방법 2가지 **
# string += "붙일 문자열"   -> 붙일때마다 객체를 생성해서 연산하므로 메모리할당을 많이 함
# list.append("붙일 문자열") \ string = ''.join(list)
'''

'''#위의 문자열 붙이는 예제 1번
s = ''
for k in range(1000):
    s += 'str '
print(s)'''

'''#위의 문자열 붙이는 예제 2번 ** 문자열 붙일때는 list에 append하고 , 그것들을 조인 해서 출력하면 됨 **
list = []
for k in range(1000):
    list.append('str ')
    s = ''.join(list)
print(s)'''
# 둘의 출력 결과는 같다.

# 사실 반복되게 같은 스트링을 붙이는 것은 s = 'str ' * 1000 이게 제일 빠르다.
import string
print(string.digits)    # 0~9
print(string.ascii_letters)   # a~z , A~Z   = lowerclase + uppercase 얘네들은 ascii_ 붙여야함
print(string.punctuation)
x = 'a'
print(x in string.ascii_letters)    # True
print(x in string.ascii_uppercase)  # False
d = string.ascii_letters + " " + string.digits
print(d)
print(u'spam and egg') #유니코드
print('a'+u'bc')
print(ord('A'))
print(chr(65))
# 한줄 주석 // 와 같음
'''
문서 문자열 주석  /* ~ */ 와 같음
'''
s = 'spam'
# print(s[100]) 오류
print(s[1:100]) # 1번쨰부터 100번쨰까지 출력 -> pam
print(s[4:0])   # 4~0 음 말이안됨 공차를 넣어야함 공차 -1 넣으면 ,map 뜸
s = '''1
31
312
3123
123
123
13
123'''
print(s.count("\n"))
s = 'user/local/bin/python'
k = s.find('p')
l1 = s.split('/')
s1 = ""
s1 = '/'.join(l1[0:3]) + ' python'
print(s1)
s = 'spam ham'
s = s[5:]+" "+s[0:4]
print(s)

print(s[0])
print(s[0][0])
