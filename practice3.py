'''
print("정수 입력 : \n")
a = int(input())
if a > 50:
    print("50보다 크면 실행")
elif a > 30:
    print("30 <  < 50 이면 실행")
elif a >4 10:
    print("10 <  < 30 이면 실행")
else:
    print(" < 10 이면 실행")

if True:
    print("this area is True area")
else:
    print("this area is false")
print("this area is the end")
## 조건이 없다면 기본적으로는 True 이다


a = input("입력: ")     # 이렇게 하면 입력: 출력하고 여기서 입력된 내용을 저장 가능
print(a*2)
print(10+ int(a))       # java 는 (int) a 이지만 , 파이썬은 int(a) 이다. 자료형변환 참고!!
'''
'''
a = input("입력: ")
a = int(a)
if a % 2 == 0 :
    print(a,"는 짝수입니다.")
else:
    print(a,"는 홀수입니다.")
if a > 255:
    print(a,"는 255를 초과")
b = int(a) * 10
print(b)
'''
'''
time = input("현재 시각 : ")
if time[-2:] == "00":
    print("현재 시각은 정각입니다")
else:
    print("현재 시각은 정각이 아닙니다")
'''
'''
fru = ["바나나", "수박", "토마토", "망고"]
arr = input("내가 좋아하는 과일은(한글로)? ")
if arr in fru:
    print("정답입니다!")
else:
    print("떙!!!!")
# if for a in b  ==  if(b.contains(a))
'''
'''
score = input("점수 입력: ")
score = int(score)
if score > 80:print("학점 = A")
elif score > 60:print("학점 = B")
elif score > 40:print("학점 = C")
elif score > 20:print("학점 = D")
else:  print("학점 = E")
'''
'''
rate = { "달러": 1200, "엔": 1.1, "유로":1300, "위안":200 }
a = input("입력:  금액 단위 ")
n, cur = a.split()
print(float(n) * rate[cur], "원" )

#입력을 금액과 단위 두개에 대하여 받으면 이것을 split해서 다른 변수 n, cur 에 저장을 해서
# 저장받은 변수를 형변환 시켜서 곱해서 출력한다.
'''
'''
n1 = input("input num1 : ")
n2 = input("input num2 : ")
n3 = input("input num3 : ")
n1 = int(n1);n2 = int(n2);n3 = int(n3)
#Brute Force Approach
if n1 > n2:
    if n2 > n3:
        #n1 > n2 > n3
        print("max num above n1, n2, n3 is n1")
    else:
        if n3 > n1:
            # n3 > n1 > n2
            print("max num above n1, n2, n3 is n3")
        else:
            #n1 > n3 > n2 
            print("max num above n1, n2, n3 is n1")
else:   #n2 > n1
    if n1 > n3:
        #n2 > n1 > n3
        print("max num above n1, n2, n3 is n2")
    else:#n2 > n1, n3 > n1
        if n2 > n3:
            # n2 > n3 > n1
            print("max num above n1, n2, n3 is n2")
        else:
            #n3 > n2 > n1
            print("max num above n1, n2, n3 is n3")
  ''''''
n1 = input("input num1 : ")
n2 = input("input num2 : ")
n3 = input("input num3 : ")
n1 = int(n1);n2 = int(n2);n3 = int(n3)
max = 0
if n1 > n2:
    max = n1
else:
    max = n2
if max < n3:
    max = n3
print(max)'''
'''
pn = input("휴대폰 번호 입력('-' 를 포함해서 입력) : ")
fn = ["011", "016", "019", "010"]
comp = ["SKT", "KT", "LG", "Unknown"]
first = pn.split('-')[0]
second = pn.split('-')[1]
third = pn.split('-')[2]
if len(second) != 4 or len(third) != 4:
    print("Wrong Input")
    pass
    if first == "011":
        print("You are in SKT")
    elif first == "016":
        print("You are in KT")
    elif first == "019":
        print("You are in LG")
    else:
        print("Unknown")
'''
'''
addnum = input("우편번호 : ")
add3 = addnum[:3]
강북구 = ["010", "011", "012"]
도봉구 = ["014", "015", "016"]
노원구 = ["017", "018", "019"]
if add3 in 강북구:
    print("강북구")
elif add3 in 도봉구:
    print("도봉구")
elif add3 in 노원구:
    print("노원구")
else:
    print(" I don't know written area number")
'''

#주민번호로 남녀 판별 ->  string split and compare
#jnum = input("주민등록번호를 입력하세요: ")
'''
jnum1 = jnum.split("-")[1]
if jnum1[0] == '1' or jnum1[0] == '3':
    print("Man")
elif jnum1[0] == '2' or jnum1[0] == '4':
    print("Woman")
else:
    print("not 1, 2, 3, 4")
'''
'''
jnum2 = jnum.split('-')[1]
# 주민번호 뒷자리 7자리 중 2, 3번쨰 자리는 지역 코드를 의미
if 0 <= int (jnum2[1:3]) <= 8:
    print("서울")
elif 9 <= int(jnum2[1:3]) <= 12:
    print("부산")
else:
    print ("Not 서울 or 부산")
'''
'''
아래 내용은 왜 안될까
jnum1 = jnum.split('-')[0]
jnum2 = jnum.split('-')[1]
val = ( (int(jnum1[0]) * 2 ) + (int(jnum1[1]) * 3 ) + (int(jnum1[2]) * 4 ) +
(int(jnum1[3]) * 5 ) + (int(jnum1[4]) * 6 ) + (int(jnum1[5]) * 7 ) + (int(jnum2[0]) * 8 ) + (int(jnum2[1]) * 9 ) + (int(jnum2[2]) * 2 )
 + (int(jnum2[3]) * 3 ) + (int(jnum2[4]) * 4 ) + (int(jnum2[5]) * 5 )) % 11
last = 11 - val
if jnum2[6] == last:
    print("written number is correct")
else:
    print("written number is incorrect")
    
nums = input("주민등록번호 : ") 
val = (int(nums[0])*2 + int(nums[1])*3 + int(nums[2])*4 + int(nums[3])*5 + int(nums[4])*6 + int(nums[5])* 7 + int(nums[7])*8 + int(nums[8])*9 + int(nums[9])* 2 + int(nums[10])*3 + int(nums[11])*4 +int(nums[12]*5)) % 11
lastnum = 11 - val
if int(nums[11]) == lastnum:
    print("valid")
else:
    print("invalid")
    '''

import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price']) 
종가 = float(btc['closing_price'])
최고가 = float(btc['max_price'])
최저가 = float(btc['min_price'])
if (시가+변동폭) > 최고가:
    print("시가, 변동폭 , 최고가 ", 시가, 변동폭, 최고가)
    print("현재 장은 상승장")
else:
    print("시가, 변동폭 , 최고가 ", 시가, 변동폭, 최고가)
    print("하락장")