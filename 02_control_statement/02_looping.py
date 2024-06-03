
# For 문

# for 변수 in 객체 :
#    실행문

# 객체는 일반적으로 문자열, 리스트, 튜플, 딕셔너리 등을 의미한다.
# 변수는 객체의 첫 "인덱스"에 "해당하는 값"부터 마지막에 해당하는 값까지 차례대로 정의된다.

for x in 'abc' :
  print(x)

# Set - {}
# set 이라서 순서 상관없음.
for x in {'one', 'two','three'}:
  print(x)

# List - []
for [x, y] in [[1,2], [3,4], [5,6]] :
  print(x,y)

# 문자열
words = ['pig','bear','gorilla','squirrel']
for w in words :
  print(w, len(w))

a = 'abcde'
b = [val + 'k' for val in a]
print(b) # ['ak', 'bk', 'ck', 'dk', 'ek']


# range() : 일련의 숫자를 반복해야 하는 경우에 사용

# for 변수 in range(시작값, 끝값, 증감크기):
#   실행문

for i in range(5):
  print(i)

# 구구단 출력
print('출력할 구구단 단 수를 입력해주세요.')
dan = int(input()) # input() 은 문자로 들어옴. 그래서 정수로 형 변환

for i in range(1,10):
  print(str(dan) + '*' + str(i) + '=' + str(dan*i))

# 출력하는 단에 홀수만 출력하기
print('출력할 구구단의 단 수를 입력해주세요.')
dan = int(input())

for i in range(1,10,2):
  print(str(dan) + '*' + str(i) + '=' + str(dan*i))

a = ['i', 'am', 'a', 'boy']

for i in range(len(a)):
  print(i, a[i])

print(range(10)) # range(0, 10)
print(sum(range(4))) # 6

for dan in range(2,10):
  for i in range(1,10):
    print(str(dan) + "*" + str(i) + '=' + str(dan*i))
  print()


# while 문

# while 조건문:
#   수행할 내용

i = 1
while i <= 10:
  print(i)
  i += 1 

dan = 1
while dan < 10:
  su = 1
  while su < 10:
    print(str(dan) + '*' + str(su) + '=' + str(dan*su))
    su += 1
  print()
  dan += 1