# List

# 일련의 값이 모인 집합을 다루기 위한 자료형
# 일반적인 프로그래밍 언어와 다르게 길이를 동적으로 조절할 수 있어 list 라고 부른다.
# 파이썬에서는 list 가 배열, 하지만 동적으로 길이 조절 가능

fruits = ['orange', 'apple', 'pear', 'kiwi', 'apple']

print(fruits)
print(fruits[0])



# List 유용한 메소드

# 1. count() : 해당 리스트에 인자로 준 값이 몇 개 존재하는지 확인하여 그 수를 반환
print('apple : ', fruits.count('apple'))
print('grape : ', fruits.count('grape'))

# 2. index() : 인자로 준 값이 몇 번째 인덱스에 존재하는지 확인하여 그 인덱스를 반환
# 같은 값이 리스트 내에 여러개 존재하면 가장 처음에 존재하는 값의 인덱스 반환
print('index : ', fruits.index('apple'))
# print('index : ', fruits.index('grape')) # 존재하지 않은 것 넣으면 error

print('index : ', fruits.index('apple',3)) # 3번 인덱스 뒤부터 존재하는 인덱스 반환

# 3. reverse() : list 값을 역으로 정렬한다. 원본 list 에 영향을 준다.
fruits.reverse()
print(fruits)

# 4. append() : list 끝에 값을 덧붙여 추가한다.
fruits.append('pineapple')
print(fruits)

# 5. sort() : 요소를 정렬하는 메소드로 원본 list에 영향을 준다.
# 기본적으로 알파벳 첫 글자를 기준으로 오름차순 정렬
fruits.sort()
print(fruits)

# 내림차순 정렬 sort(reverse=True)
fruits.sort(reverse=True)
print(fruits)

# 문자 길이 짧은 순
fruits.sort(key=len, reverse=False)
print(fruits)



# del 키워드
# 원본 배열 list의 일부 요소 혹은 전체 목록 제거 가능

abclist = ['A', 'B', 'C', 'D', 'E', 'F']
print(abclist)

del abclist[0]
print(abclist)

del abclist[1:3] # 슬라이싱 1:3 3번째 전까지 삭제
print(abclist)

del abclist
print(abclist)