
# 예외처리
# 문장이나 표현식이 문법적으로 올바르다 할지라도, 실행하려고 하면 에러를 일으킬 수 있다.

# 예외 처리 기본 문법

# try:
# except:

try:
  4 / 0
except:
  print("예외발생")

try:
  4 / 0
except ZeroDivisionError as e:
  print(e)

try:
  a = [1,2]
  print(a[2])
  4/0
except ZeroDivisionError:
  print("0으로 나눌 수 없습니다.")
except IndexError:
  print("인덱싱 할 수 없습니다.")


# try-finally 문
# 예외 발생 여부와 상관 없이 항상 수행되는 내용을 finally에 작성할 수 있다.
try:
  f = open('foo.txt', 'w')

finally: # finally는 무조건 실행됨.
  f.close()


# try-else 문
# try 문에는 else 절도 사용할 수 있다. 오류가 나지 않을 때만 else 실행
# try 문 수행 중 오류가 발생하면 except절, 오류가 발생하지 않으면 else 절이 수행된다.
try:
  age = int(input('나이를 입력 해주세요 : '))
except:
  print("입력이 정확하지 않습니다.")
else:
  if age <= 18:
    print("미성년자는 출입이 불가합니다.")
  else:
    print("환영합니다.")


# 오류 회피하기
# 코드를 작성하다 보면 특정 오류가 발생할 경우 그냥 통과시켜야 할 경우가 있다.
# try 문 안에서 error 가 발생할 경우 pass 를 상요하여 오류를 그냥 지나가도록 작성할 수 있다.
try:
  f=open("없는 파일", 'r')
except FileNotFoundError:
  pass


# 예외 만들기
# 프로그램을 수행하다 보면 특수한 경우에 예외 처리를 하려고 예외를 만드는 경우가 발생한다.
# 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다.
class MyError(Exception):
  pass

def say_nick(nick):
  if nick == '돼지':
    raise MyError()
  print(nick)

try:
  say_nick('곰')
  say_nick('돼지')
except MyError:
  print('허용되지 않은 별명입니다.')


