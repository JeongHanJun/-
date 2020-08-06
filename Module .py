'''
    Module
    모듈은 파이썬 정의와 문장들(?) 을 담고있는 파일이다.
    함수 정의, 실행 가능한 문장들(?)

    1) import ModuleName
    2) from ModuleName import 이름(들)
    3) from 모듈명 import *
    4) imoort 모듈명 as 새 이름
    5) from 모듈명 import 이름 as 새 이름

'''
'''
import sys
print(dir())
print(__doc__)
'''
n1 = 16
n2 = 3
c1 = 5
c2 = 2
fn = 10.123
deg1 = 30
deg2 = 45
# 1번 import ModuleName
'''import math
print(math.ceil(fn))
'''
# 2) from ModuleName import 이름(들)
'''from math import ceil, sqrt
print(ceil(fn), sqrt(n1), sqrt(n2)) # 이러면 math.이름 이런식으로 안하고 바로 이름으로 사용 . 즉 직접 참조 가능
'''
# 3) from 모듈명 import *
'''from math import *
print(ceil(fn), sqrt(n1), sqrt(n2), comb(c1, c2))
'''
# 4) imoort 모듈명 as 새 이름
'''import math as m
print(m)    # print -> <module 'math (built-in)
'''
# 5) from 모듈명 import 이름 as 새 이름
'''from math import sqrt as root
print(root(n1), root(n2))'''
'''import string
import math
print(dir(string))
print()
print(dir(math))'''
'''
import string
print(string.__dict__)
'''
#import ExofModule
#print(ExofModule.pi)
# 모듈을 내가 만들어서 return까지 하고 저장한 상태를 import 받기만 해도 출력이 나온다.
# 한마디로 import 가 코드를 가져오는 것 뿐만이 아니라 수행도 한다.

# 만약 모듈이름과 이미 사용하던 이름이 같다면
'''string = 'Example String'
import string
print(string)   # Module의 string 에 대해 출력됨 가장 최근에 실행되서인가? -> O
# import는 치환이다. 현재 Module.py 라는 모듈에 string이라는 이름을 생성하고 이름을 모듈객체와 연결 이경우에는 이전의 string이 없어지고 새롭게 재생성
''''''
import string
string.a = 1    # 얘는 string module에 내가 a=1 이라는 사전형으로 이름을 등록한것
string = "Example String"
print(string)
#print(string.a)    # 이거 오류다 지금 이상태에서 string은 모듈이 아니라 Example string이기 때문
# 모듈을 다시 import 해서 써야한다
import string
print(string.a)'''

# 모듈은 공유된다 공유되니까 import만 한다면, 어디에서 사용가능, but 가장 최근에 입력된 모듈의 내용이 사용됨
'''
    같은 모듈에 대한 재적재

''''''
import ModuleShareTest1
ModuleShareTest1.testnum = ' 기존에는 123이었다.'
print(ModuleShareTest1.testnum)
import ModuleShareTest1
#MT.testnum = " 123 -> 기존에는 123이었다. -> 지금" # 이걸 선언하면 이게 출력됨
print(ModuleShareTest1.testnum)
'''
# 교착상태를 피하기 위해서 메모리에 적재된 모듈은 다시 물리적으로 import 하지 않고 이용한다.

'''
    현재 우선적으로 실행되고 이쓴ㄴ 모듈이 최상위 모듈인가?
    아니면 import 된 모듈인가?
        
        -> use __name__
        일반적으로 자신의 모듈이름을 가진다.
''''''
import Mtest1
import string
print(string.__name__)
import os
print(os.__name__)
import sys
print(sys.__name__)
print(__name__) # 지금 Module.py 가 프로그램 모드로 수행되므로 main이란 이름을 가진다.
                # 즉 지금 최상위 모듈, 현재 가장 먼저 수행되는 모듈은 Module.py 라는걸 알 수 있다.
if __name__ == '__main__':
    print("지금 실행하는 py 가 최상위 모듈, 현재 가장 먼저 실행되는 모듈이다.")'''
import calendar
getattr(calendar, 'prmonth')
print('---------------------')
# getattr( object, name) object에서 문자열로 주어진 이름에 해당하는 attribute를 return 한다. 만약 없으면 AttributeError
calendar.prmonth(2020,8)
print('-------------위는 직접 모듈에 접근해서 호출--------------')
getattr(calendar, 'prmonth')(2020, 8)
print('--------------위는 getattr 메소드를 이용해 문자열이용해 호출----------')
f = getattr(calendar, 'prmonth')
f(2020,8)
print('-------------------위는 함수포인터가 메소드를 가지고, 그 함수의 인자에 문자열을 넣어서 출력----------------')