# **문제 2: 학생 성적 관리 프로그램**

# 학생들의 성적을 관리하는 프로그램을 작성하세요. 프로그램은 다음 기능을 포함해야 합니다:

# 1. 학생의 이름과 성적을 입력 받아 저장합니다.
# 2. 특정 학생의 성적을 조회합니다.
# 3. 모든 학생의 평균 성적을 계산하여 출력합니다.
# 4. 성적이 특정 점수 이상인 학생들의 이름을 출력합니다.

#### 선생님 답안 ####

grades = {}

def display_menu():
    print("1. 학생 성적 입력")
    print("2. 학생 성적 조회")
    print("3. 평균 성적 계산")
    print("4. 특정 점수 이상인 학생 조회")
    print("5. 종료")

def add_grade():
    name = input("학생 이름을 입력하세요: ")
    grade = int(input("학생 성적을 입력하세요: "))
    grades[name] = grade
    print(f"{name}님의 성적이 저장되었습니다.")

def get_grade():
    name = input("조회할 학생의 이름을 입력하세요: ")
    grade = grades.get(name)
    if grade is not None:
        print(f"{name}님의 성적은 {grade}점입니다.")
    else:
        print("해당 학생의 성적을 찾을 수 없습니다.")

def calculate_average():
    if not grades:
        print("저장된 성적이 없습니다.")
    else:
        average = sum(grades.values()) / len(grades)
        print(f"평균 성적: {average:.2f}점")

def get_high_achievers():
    threshold = int(input("기준 점수를 입력하세요: "))
    high_achievers = [name for name, grade in grades.items() if grade >= threshold]
    if high_achievers:
        print(f"{threshold}점 이상인 학생: {', '.join(high_achievers)}")
    else:
        print(f"{threshold}점 이상인 학생이 없습니다.")

while True:
    display_menu()
    choice = int(input("선택하세요: "))
    if choice == 1:
        add_grade()
    elif choice == 2:
        get_grade()
    elif choice == 3:
        calculate_average()
    elif choice == 4:
        get_high_achievers()
    elif choice == 5:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 시도하세요.")


##### gpt #####
# # 학생 성적을 저장할 리스트
# students = []

# # 1. 학생의 이름과 성적을 입력 받아 저장합니다.
# def add_student(name, score):
#     students.append({'name': name, 'score': score})

# # 2. 특정 학생의 성적을 조회합니다.
# def get_student_score(name):
#     for student in students:
#         if student['name'] == name:
#             return student['score']
#     return None

# # 3. 모든 학생의 평균 성적을 계산하여 출력합니다.
# def calculate_average_score():
#     if not students:
#         return 0
#     total_score = sum(student['score'] for student in students)
#     return total_score / len(students)

# # 4. 성적이 특정 점수 이상인 학생들의 이름을 출력합니다.
# def get_students_above_score(threshold):
#     return [student['name'] for student in students if student['score'] >= threshold]

# # 프로그램 테스트
# add_student('Alice', 85)
# add_student('Bob', 90)
# add_student('Charlie', 78)

# print("Alice's score:", get_student_score('Alice'))
# print("Average score:", calculate_average_score())
# print("Students with score >= 80:", get_students_above_score(80))


###### 내 답안 작성 중 ######

students = []

def add_info(name, score):
  # name = input('이름을 입력하세요 : ')
  # score = int(input('점수를 입력하세요 : '))
  students.append({'name' : name , 'score': score})
print(students)

def get_info(name1):
  name1 = input('성적을 조회할 학생의 이름을 입력하세요 : ')
  