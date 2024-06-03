
# SET

# "중복을 허용하지 않으며 순서 없이" 요소를 저장하는 컬렉션이다.
# 따라서 중복 제거가 필요할 때 유용하게 사용할 수 있다.
# {} 중괄호를 사용하여 집합을 생성한다.

# 순서와 상관없이 출력
ohgiraffers = {'pig', 'squirrel', 'bear', 'gorilla', 'pig'}
print(ohgiraffers)

# 리스트로 set 생성
another_safari_set = set(['monkey', 'tiger', 'wolf'])
print(another_safari_set)

mixed_set = {1, 'bear', (1,2,3)}
print(mixed_set)

ohgiraffers.remove('pig')
print(ohgiraffers)

ohgiraffers.add('pig')
print(ohgiraffers)

# SET 메소드

# 1. update()
ohgiraffers1 = set(['monkey','tiger','wolf'])
print(ohgiraffers1)
ohgiraffers1.update(['squirrel','bear', 'gorilla'])
print(ohgiraffers1)

# 2. discard() : 없는 값이면 에러났는데 이걸 사용하면 없는 값이 입력이 되면 괜찮다.
ohgiraffers1.discard('pig')

# 3. pop() : 어떤 게 제거될지 모름
ohgiraffers1.pop()
print(ohgiraffers1)

# 4. clear() : 모든 값을 제거하는 메소드 ; 제거가 되면 빈값으로 set() 이 나옴.
ohgiraffers1.clear()
print(ohgiraffers1)

# 5. union() : 두 set "합집합"

javaTeam = {'gorilla', 'tiger', 'monkey'}
pythonTeam = {'pig', 'bear','gorilla', 'tiger'}

ohgiraffers2 = javaTeam.union(pythonTeam)
print('ohgiraffers2 : ' , ohgiraffers2)

# 6. interserction() : 두 set 자료형의 "교집합"을 반환
print('interserction() : ', javaTeam.intersection(pythonTeam))

# 7. difference() : 좌향을 기준으로 우향의 차집합을 반화
print('difference() : ', javaTeam.difference(pythonTeam))
print(pythonTeam.difference(javaTeam))

# 8. copy() : 대상 set을 복사하여 반환
javaTeam1 = javaTeam.copy()
print('javaTeam1 : ', javaTeam1)
print('javaTeam 주소 : ', id(javaTeam))
print('javaTeam1 주소 : ',id(javaTeam1))
