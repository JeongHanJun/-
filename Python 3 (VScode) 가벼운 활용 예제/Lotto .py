from random import *

people = list(range(1, 50))
shuffle(people)
#print(type(people))
#print(people)
winners = sample(people, 4)
print("{}번님이 1등에 당첨되었습니다. 상품은 치킨입니다. Winner winner Chicken Dinner".format(winners[0]))
print("{}번 님이 2등에 당첨되었습니다. 상품은 커피(**벅스 기프티콘)입니다.".format(winners[1:]))