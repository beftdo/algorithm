#숏코딩 인덱스
print('FFFFFFDCBAA'[int(input())//10])
#숏코딩 Dict
a = {10:'A', 9:'A', 8:'B', 7:'C', 6:'D'}
try : print(a[int(input())//10])
except : print('F')
#제출한 답
a = int(input())
if a >= 90:
    print("A")
elif 80<=a<90:
    print("B")
elif 70<=a<80:
    print("C")
elif 60<=a<70:
    print("D")
else: print("F")