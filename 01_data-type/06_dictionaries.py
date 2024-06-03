
# Dictionaries

# java -> map()
# 키(key)와 값(value)의 쌍으로 구성된 데이터 구조
# 키를 통해 값을 찾을 수 있으므로 매우 빠른 조회 성능을 보여준다.
# key => 고유한 값, 중복되면 안됨. value는 중복 가능

teacher = {'name':'pig', 'team' :'ohgiraffers'}
print(type(teacher))
print(teacher['name'])
print(teacher['team'])

# 생성 후 키-값 쌍 추가/ 수정/ 삭제
teacher['age'] = 20
print(teacher['age'])

# in 키워드 : bool 타입
print('name' in teacher)


# 1. get() : 매개변수로 전달받은 key에 해당하는 값을 반환
print(teacher.get('name'))

# 2. keys() : dictionaries 안에 있는 모든 key값 반환
print(teacher.keys())

# 3. values() : dictionaries 안에 있는 모든 value값 반환
print(teacher.values())

# 4. items() : items 안의 모든 항목 반환
print(teacher.items()) # dict_items([('name', 'pig'), ('team', 'ohgiraffers'), ('age', 20)])
print(teacher) # {'name': 'pig', 'team': 'ohgiraffers', 'age': 20}

# 5. pop(키) : key에 대한 value를 반환하고 제거
print(teacher.pop('age'))
print(teacher)

# 6. clear() : 모든 항목을 제거하는 메소드
teacher.clear()
print(teacher) # {} 없으니까 다음과 같이 반환
