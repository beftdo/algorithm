# 제출한 답
a,b = map(int, input().split())
c = 60*a + b - 45
if [a,b] == [0, 45]:
    print(0, 0)
elif c>0:
    print(c//60, c%60)
else :
    print(24+(c//60), c%60)

#숏코딩
a,b=map(int,input().split())
print((a-(b<45))%24,(b-45)%60)
#b가 45보다 작으면 True로 1반환하여
#(a-1%24)가 됌. False라면 시간은 1 빼지 않고 그대로 24로 나눈 나머지를 출력