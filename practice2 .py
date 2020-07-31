movies = ["Dr.strang","Hulk","Thor","Avengers","HarryPotter"]
print(movies)
# insert(index, value/string)
movies.insert(5, "the Lord of the Ring")
print(movies)
movies.append("append method is append at end of list")
#insert 는 내가 원하는 위치에 넣을 수 있으므로 insert 가 더 유용하다
del(movies[6])
print(movies)
# delete
# del(list.[index])
del(movies[4]) # delete Harry Potter
print(movies)
del(movies[4]) # delete the Lord of the Ring 이유는 해리포터 삭제되고 땡겨졌으므로
print(movies)
langlist1 = ["C", "C++", "java"]
langlist2 = ["Python", "Go", "C#"]
llist = langlist1+ langlist2
print(langlist1)
print(langlist2)
print(llist)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("max :", max(nums))
print("min :", min(nums))
# 주의!! 여기서 print("max : "+max(nums)) 를 할수는 없다. +로 이어붙이는 경우에는 max(nums)가 integer type 이어야 한다.
print("max :", max(nums))
#print("max :"+max(nums))   이 부분이 위에서 작성한 이유로 실행되지 않고 오류가 발생한다.


print(sum(nums))    # 1 ~ 9 의 합 = 45   sum(listname)
dishes = ["pizza", "bab", "mandu", "chicken", "salad", "kimchi"]
#list의 원소의 갯수 = l    len(list의이름)
print(len(dishes))
print(sum(nums) / len(nums))    # 45 / 9 = 5인데 5.0
nums2 = [1, 2, 4]
print(sum(nums2) / len(nums2))
# avg 는 따로 함수 없음 합을 갯수로 나눠서 출력하는 방법뿐이다.

nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums3[::])    # 일반적으로 전체 출력 [], ',' 포함
print(nums3[::1])   # 위랑 같다. 전체 원소들에 대해 공차가 1로 출력
print(nums3[::2])   # 전체를 처음부터 공차가 2 단위로 출력
#  for(int i = 0 ; i  <  n ;  i++ ) 이면 i의 값 변화는 마지막에 있는것처럼 위에도 index 변화값은 맨 마지막에 존재
print(nums[1:])     # nums list에서 1번째 원소를 제외하고 출력
print(nums[1::])    # 위와 같다 .
print(nums)         #보다 시피 제외하고 출력이지, list의 값이 변하지는 않음을 보여주기 위해 출력
print(nums[2:])     # nums에서 2번째 항목까지 제외해서 출력
print(nums3[1::2])  # 짝수만 출력됨, 첫번쨰 원소를 제외하고 2단위로 출력하니까 
# 2, 3, 4, 5, 6, 7, 8, 9, 10을 만들고 2부터 2단위인 2, 4, 6, 8, 10출력
print(nums3[:-1])   # -1번째 원소(마지막 원소인 10)를 제외하고 출력
print(nums3[-1:])   # -1번째 원소인(마지막 원소인 10) 을 출력
print(nums3[::-1])  # 역순으로 출력  index값을 -1 이므로 i-- 의 의미

companies = ['SamSung', 'LG', 'KT', "SK", 'HanHwa', 'NHN']
print(companies[2], companies[3])   # index 2, 3인 즉 3,4번쨰 원소인 KT, SK 출력
print(" ".join(companies))        # companies 라는 list에 대해 값공백값공백값공백 이런식으로 출력
#companies[0] companies[1] ...이런식으로
print("\n")
print("/".join(companies))
# 문자열을 원소/원소/원소 이렇게 출력
# "구분자".join(list이름)

print("\n".join(companies))
# \n단위로 원소 출력

ex1 = "123a456a789aend"
print(ex1.split('a'))
# pinrt ['123', '456', '789', 'end']
print(ex1.split("a"))   # 위랑 똑같다. 문자로 구별하든 string으로구별하든
ex2 = "12aa34aa45aa67aaopaaend"
print(ex2.split("aa"))  # 문자열로 구분한 결과 12, 34, 45, 67, op, end

# sort, 오름차순 정렬  2가지 방법
# 1번쨰 복사 해서 sort 방법
nums4 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
nums4_1 = sorted(nums4)
print(nums4_1)
# 2번쨰 기존 리스트를 sort
nums4.sort()
print(nums4)

# list를 역순으로
nums4.reverse()     # nums4[::-1] 과 같다.
print(nums4)


exstr = "파이썬의 리스트에 관한 함수 및 메소드 자습"
exstr1 = exstr.split()
print(exstr1)
#sort(exstr1(key = len))      # 얘는 안되고
exstr1.sort(key = len)        # 얘는 된다. sort(key = 정렬 기준 함수)
print(exstr1)


# 세미콜론은 구문을 이어서 쓸때
print(nums);print(nums) 
import math
print(math.sqrt(81))
print(math.factorial(5))
# hep(Math) 하면 math 라이브러리의 내용을 볼 수 있음
# 내용을 보면 삼각함수들, ceil(올림) , comb(n, k, /) nCk  조합 의 경우의수 , dist(p, q, /) 두점 p,q의 거리, degrees(x,/) x를 radians to degrees degree 는 각도, 라디안 단위
# exp(x,/) x의 제곱   fabs(x,/) float x의 절댓값 return gammafunc 
