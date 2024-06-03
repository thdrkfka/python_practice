# 기본 자료형

# 1. 숫자형
# int : 정수 값을 가지는 자료형
# float : 소수 값을 가지는 자료형

# 변수 선언
num1 = 1
num2 = 3.14

print(type(num1))
print(type(num2))


# 연산

num3 = 11
num4 = 7

print(num3 + num4)
print(num3 - num4)
print(num3 * num4)
print(num3 / num4)
print(num3 % num4)

# 몫만 구하는 연산
print(num3 // num4)

# 제곱 연산
base = 9
exponent = 3
print(base ** exponent)


# 2. 논리형 (Bool)
bool1 = True
bool2 = False

print(type(bool1))
print(type(bool2))


# 3. 문자형 (String)

fruit = 'apple'
print(fruit)

# 정수를 str() 함수를 이용하여 문자열로 변환 가능
capasity = str(300)
print(type(capasity))

# """""" => 여러줄 출력 가능
print("""
Long 코트보다 긴건 ?
  double 코트
짧은 건?
  int 패딩
""")

# 문자열은 index를 가지고 있어 인덱싱을 통해 원하는 위치의 문자 하나를 추출할 수 있다.
# 띄어쓰기 index에 포함됨.
address = '대한민국 서울시 서초구'
print(address[5])
print(address[9])

# 슬라이싱 (slicing) : 원하는 만큼 추출 가능
print(address[9:]) # 9번 인덱스부터 끝까지
print(address[5:8]) # 끝나는 지점도 인덱스 가능
print(address[1:12:4]) # 4개씩 건너띄어서 추출
print(address[::-1]) # 문자열 뒤집기
print(address[-3:]) # - 는 뒤에서부터

# 문자열 * (곱하기) 연산
subject = 'python'
print(subject * 3) # 문자열 반복되어서 출력


# 문자열 관련 메소드

# 1. replace() : 문자열을 치환하는 메소드
enroll_date = '2024/12/16'
rep_enroll_date = enroll_date.replace("/","-")
print(rep_enroll_date)

# 2. strip() : 제거할 문자 집합을 지정하는 메소드
origin = 'ohgiraffers'
with_white_space = '   oh giraffers'

# 공백 제거
print(with_white_space.strip()) # strip()을 그냥 실행시키면 앞에 있는 공백 문자열 제거
print(with_white_space.strip('   o'))
print(with_white_space.strip('   os'))

# 3. 대소문자 관련 메소드
origin_str = 'hELLO wORLD!'
print(origin_str.upper()) # 모두 대문자
print(origin_str.lower()) # 모두 소문자
print(origin_str.capitalize()) # 가장 첫글자만 대문자

# 4. 문자형 포맷
# 변수 포맷을 이용하여 문자열에 변수 값을 삽입할 수 있다.
# 변수 포맷 종류
  # %s : 문자열
  # %c : 문자
  # %d : 정수
  # %f : 실수
x = 10
print("x is %d" % x) # % 어떤 변수랑 매칭되는지
y = 'code'
print('y is %s' % y)

print('x is {0}' .format(x)) # format에 대한 인덱스 번호 인듯,,? {index 번호} 타입을 맞춰주지 않고 format()을 해도 됨.
print('x is {0} y is {1}' .format(x,y))

# 형 변환
  # 암시적 형 변환
print(True + 3)
print(3 + 5.0)
# print(3+'5') # 이렇게 정수와 문자는 안됨. 명시적 형 변환 시는 가능

  # 명시적 형 변환
print(int('3')+4)

print(float('3'))

print(str(1))
print(str(1.0))
print(str({1,2,3}))