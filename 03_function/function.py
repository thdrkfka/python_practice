
# 함수

# def 키워드를 사용해 함수를 정의하고 함수 이름, 다음에 괄호와 콜론을 작성한다.

# def function():
#   함수가 실행하는 코드 내용

def myfunction() :
  print('hello world!')
myfunction()


def addNum(num1, num2):
  print(num1 + num2)
addNum(2,4)


def multiplyNum(num1):
  return num1 * 8
result = multiplyNum(8)
print(result)


# 1. 위치 인자 = 위치로 매칭하는 방법
# 2. 키워드 인자 = 매개변수 이름으로 매칭하는 방법

def func(a,b):
  print(a,b,sep=' ')

# 위치 매칭
func('hello','world!')

# 키워드 매칭
func(b='world', a='hello')


# 매개변수 기본 값 지정
def func2(a, b=3):
  return a+b

print(func2(10,10)) # 20
print(func2(10)) # 13

# 패키지
# *을 붙여서 많은 인자들을 한꺼번에 args 라는 걸로 받음.
def add_many(*args):
  result = 0
  for i in args:
    result = result + i
  return result
print(add_many(1,2,3,4,5,6,7,8,9,10))

# 언패키지
def sum(a,b,c):
  return a+b+c

numbers = [1,2,3]
# sum(numbers) # => 이렇게 넘기면 에러남. numbers 는 하나의 리스트 이니까
print(sum(*numbers))


# 람다 표현식

# 매개변수로 함수를 전달하기 위해 함수 구문을 상요하는 것이 번거롭고
# 코드 낭비라고 생각될 때 함수를 간단하고 쉽게 선언하는 방법

# 람다 기본식 예시 # lambda 매개변수 : 결과값
add = lambda x,y : x+y
print(add(3,5))

numbers1 = [1,2,3,4,5]
squared_numbers = map(lambda x : x**2, numbers1) # x**2 => x의 제곱
print(list(squared_numbers))


# 조건에 맞는 요소 필터링
numbers2 = [1,2,3,4,5,6]
even_number = filter(lambda x : x%2 == 0, numbers2)
print(list(even_number))


# 정렬
points = [(1,2),(3,1),(5,-1)]
sorted_points = sorted(points, key=lambda x : x[1]) # (1,"2"),(3,"1"),(5,"-1") x[1] 인덱스 1번쨰의 수로 오름차순 정렬
print(sorted_points)
