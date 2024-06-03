
# Sequence Type

# 값이 연속적으로 나열된 자료형을 의미하며 다음 자료형이 해당한다.
# str : 문자열 값을 가지는 자료형
# list : 여러 값을 담을 수 있는 가변형 자료형
# tuple : 여러 값을 담을 수 있는 불변형 자료형

name = 'ohgiraffers'
print(type(name))

list = [0,1,2,3]
print(type(list))

tuple = (1,2,3)
print(type(tuple))

# Tuple : 소괄호를 사용하여 묶어줌.

# python 에서 사용하는 자료형 중 하나로, 여러 개의 값을 하나의 데이터 구조로 묶어서 관리할 수 있는 "불변 시퀀스"이다.
# list 와 유사하지만 한 번 생성되면 각 요소 값을 수정하거나 삭제할 수 없다.
# 주로 데이터의 집합을 안전하게 유지하거나, 함수에서 여러 값을 반환할 때 사용된다.

safari_tuple = ('Bear', 'Koarla', 'Gorilla', 'pig')
print(safari_tuple)

# 튜플은 중첩으로 표현할 수 있다.
tuples = (1,2, 'hello'),('test', 1,2,3,4)
print(tuples)

# list 처럼 index로 접근 가능
print(tuples[0])
print(tuples[0][2])

# tuple 연산
# 불변 객체이므로 요소 값을 한번 할당하면 추가, 수정, 삭제가 불가하다.
# tuples[0] = (1,2,3,4)
# print(tuples[0]) # 새롭게 변화시키려면 에러남.

# 파이썬은 선언과 할당이 같이 일어남. 그래서 각각 다른 변수가 선언된거라고 보면 됨.
testList = (1,2,3,4) # 아래의 testList 와 다른 변수
print(id(testList))

testList = (3,4,5)
print(id(testList))

# 튜플 간 연산

another_safari_tuple = ('monkey', 'tiger', 'wolf')
print(safari_tuple + another_safari_tuple)

print(safari_tuple * 3)

print(len(safari_tuple + another_safari_tuple))

