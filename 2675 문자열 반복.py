# 왜 틀렸을까 ㅠㅠ
T = int(input())
for i in range(T):
    a = input().split()
    for b in a[1]:
        print(int(a[0])*b, end='')