#map은 리스트의 요소를 지정된 함수로 처리해주는 함수.
#형식
#list(map(함수, 리스트))
#tuple(map(함수,튜플))

a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)

#map에는 리스트 뿐만 아니라 모든 반복 가능한 객체를 넣을 수 있다.
#range를 사용해서 숫자를 만든 뒤 숫자를 문자열로 변환

a = list(map(str, range(10)))
print(a)

#input().split()의 결과가 문자열 리스트 라서 map 사용 가능

a, b = map(int, input().split())
#map이 반환하는 맵 객체는 이터레이터라서 변수 여러 개에 저장하는
#Unpacking이 가능 따라서 맨앞 list 생략

#open(0) : 파일 오브젝트를 반환
#파일 오브젝트의 readlines() 메소드는 오브젝트를 리스트에 담아서 반환