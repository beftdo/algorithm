#제출한 답
a = list(map(int,input().split()))
b = 0
for i in a:
    b += i**2 # **은 제곱, 함수는 pow()
print(b%10)

#숏코딩
print(sum(int(a)**2 for a in input()[::2])%10)
'''
Comprehension
출력하고자하는 값(x) for x in iterator 
'''