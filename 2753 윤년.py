# True, False to 1, 0
# int() turns the boolean into 1 or 0.
x = True
y = False
print(int(x))
print(int(y))

# +를 사용하여 boolean int로 캐스팅
print(+True)
print(+False)

#제출한 답
#윤년 계산 calendar.isleap()
from calendar import isleap
print(int(isleap(int(input()))))

#숏코딩
# 1 or 2 / 1 | 2=> 작은수 반환 but 0 | 1 :1 반환
# 1 and 2 => 큰 수 반환 but 0 and 2 : 0 반환
y=int(input())
print(+((y%100 | y//100)%4<1))