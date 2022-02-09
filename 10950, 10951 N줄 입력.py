T = int(input())
c = [map(int, input().split()) for a in range(T)]
for a, b in c:
    print(a+b)

'''
N줄 인풋하기
input() for a in range(N)
리스트, 셋으로 둘러쌓아야함

몇줄인지 모를 때
while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break
'''