#제출한 답
T = int(input())
for i in range(T):
    x = input()
    y = ''
    for k in x[2:]:
        y += int(x[0])*k
    print(y)
#
T = int(input())
for i in range(T):
    num, ss = input().split()
    num = int(num)
    ans = ''
    for ch in ss:
        ans += ch * num
    print(ans)
'''
a, b = input().split()으로 넣으면
인풋이 "2 abc"라고 치면
['2', 'abc']가 되고
a에 '2'가, b에 'abc'가 들어감
-------------------------------
join 함수 : 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐
하나의 문자열로 바꾸어 변환. 리스트의 각 요소가 문자열 타입이여야 가능
'구분자'.join(리스트)
'''