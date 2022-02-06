#제출한 답
x = int(input())
y = int(input())
if x>0:
    if y>0:
        print(1)
    elif y<0:
        print(4)
elif x < 0:
    if y>0:
        print(2)
    elif y<0:
        print(3)

#숏코딩 : 수학적 풀이
x=int(input())
y=int(input())
print(int(2-y/abs(y)+int(x*y<0)))