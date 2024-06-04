
# 모듈 module

# python 코드 파일로, 관련된 코드의 집합이다. 모듈은 함수, 클래스, 변수 등을 정의할 수 있으며
# 다른 python 프로그램에서 이를 가져와 사용할 수 있다.
# 모듈을 사용하면 코드의 재사용성을 높이고 코드 관리가 용이해지는 장점이 있다.
# 모듈로 나누는 기준은 클래스로만 나누는 건 아니지만 파이썬을 객체지향으로 쓸 때, 대부분 클래스로 모듈을 나누는 편!

# 코드들의 집합
# .py 가 붙어있는 파일 -> 모듈
# 라이브러리 -> 모듈
# 객체지향 쪽에서는 클래스로 분류해서 모듀러럼 사용


# import ohgiraffersModule
# print(ohgiraffersModule.ohgiraffers.Gorilla())
# print(ohgiraffersModule.another())


# from ohgiraffersModule import another as an # as 별칭
# print(an)


# from ohgiraffersModule import ohgiraffers as oh
# print(oh.tiger())

import math
import random

# math #
# 절댓값
print(math.fabs(-5.5))

# 제곱근
print(math.sqrt(25))

# 거듭제곱
print(math.pow(2,3))

# 올림, 내림, 버림
print(math.ceil(4.2))
print(math.floor(4.2))
print(math.trunc(4.2))

# 반올림
print(round(3.145))
print(round(3.1451, 3))
print(round(3.1451, 2))

# 팩토리얼
print(math.factorial(5))


# random #
# randrange(시작값, 끝값) - 1부터 6까지 랜덤 값 출력
print(random.randrange(1,7)) # 시작값, 끝값 => 끝값 전까지 랜덤값 출력

# shuffle - 랜덤으로 섞음.
abc = ['a', 'b', 'c', 'd', 'e']
random.shuffle(abc) 
print(abc)

# choice - 아무 원소나 랜덤으로 하나 뽑아주는 함수
print(random.choice(abc))

