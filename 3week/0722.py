#문제 4)
'''def find_common_items(dict1, dict2):
    # 공통된 키-값 쌍을 저장할 새로운 딕셔너리 생성
    common_dict = {}

    # dict1의 각 키-값 쌍에 대해 반복
    for key, value in dict1.items():
        # dict2에 같은 키가 있고, 값도 같은 경우
        if key in dict2 and dict2[key] == value:
            # 공통된 키-값 쌍을 새로운 딕셔너리에 추가
            common_dict[key] = value

    return common_dict

# 예시 딕셔너리
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'a': 1, 'b': 2, 'c': 4, 'e': 5}

# 함수 호출 및 결과 출력
print(find_common_items(dict1, dict2))'''

#문제 6)
'''s1 = {1,2,3}
s2 = {1,2,4,5}

# (1) s1과 s2의 합집합
union_set = s1.union(s2)
print(f"합집합: {union_set}")

# (2) s1과 s2의 교집합
intersection_set = s1.intersection(s2)
print(f"교집합: {intersection_set}")'''

#문제 7)
'''def get_personal_info():
    name = input("이름을 입력하세요: ")
    phone_number = input("전화번호를 입력하세요: ")
    gender = input("성별을 입력하세요: ")
    age = int(input("나이를 입력하세요: "))
    university = input("대학교를 입력하세요: ")

    # 딕셔너리에 저장
    personal_info = {
        "이름": name,
        "전화번호": phone_number,
        "성별": gender,
        "나이": age,
        "대학교": university
    }

    return personal_info

# 딕셔너리 출력
personal_info = get_personal_info()
print(personal_info)'''

#문제 8)
'''str1 = "Hello World"
str2 = "Python Programming"

def find_common_chars(str1, str2):
    # 두 문자열을 소문자로 변환
    str1 = str1.lower()
    str2 = str2.lower()

    # 문자열을 집합으로 변환하여 공통 문자를 찾음
    common_chars = set(str1) & set(str2)

    # 공백 문자 제거
    common_chars.discard(' ')

    return common_chars

print(find_common_chars(str1, str2))'''

#문제 9)
# 주식 가격을 저장한 딕셔너리 생성
'''books = {
    '파이썬 개론': ['홍길동'],
    'Perfect C': ['김영수', '이동준'],
    '컴퓨터 개론': ['최환수', '주용호', '박해성']
}

# 책 이름과 저자를 출력하는 함수
def print_book_info(book_name):
    if book_name in books:
        authors = ', '.join(books[book_name])
        print(f"책 이름: {book_name}")
        print(f"저자: {authors}")
    else:
        print(f"책 '{book_name}'을 찾을 수 없습니다.")

# 예시 실행
print_book_info('Perfect C')'''

#추가문제 1)
'''import random

def generate_unique_numbers():
    numbers = set() #set은 중복된 값 자동으로 제거
    #numbers의 길이가 10이 될 때까지 반복
    while len(numbers) < 10:
        num = random.randint(1, 20)

        numbers.add(num)

    return list(numbers)

unique_numbers = generate_unique_numbers()
print(unique_numbers)
'''

#추가문제 2)
'''student_courses = {
    "학생1": {"수학", "과학", "영어"},
    "학생2": {"수학", "음악", "미술"},
    "학생3": {"수학", "과학", "음악"}
}

# 모든 학생이 듣는 과목
all_courses = set.intersection(*student_courses.values())

# 한 명이라도 듣는 과목
any_courses = set.union(*student_courses.values())

# 한 명씩만 듣는 과목
course_count = {}
for courses in student_courses.values():
    #print(courses)
    for course in courses:
        #print(course)
        if course in course_count:
            course_count[course] += 1
        else:
            course_count[course] = 1
        #print(course_count)

# 유일한 과목을 저장할 빈 집합
unique_courses = set()
for course, count in course_count.items():
    if count == 1:
        unique_courses.add(course)

print("모든 학생이 듣는 과목:", all_courses)
print("한 명이라도 듣는 과목:", any_courses)
print("한 명씩만 듣는 과목:", unique_courses)
'''
#추가문제 3)
'''text = """
The first they had heard of the strangers from outer space was when the new ultra short-wave frequencies were used. Professor Kennicot of Palmira University was the first to find how to generate and control them. He tried to transform the wavelengths upward to a range either auditory or visual but for some reason power was lost in the process.

Apparently he gave them a sufficient jolt with extra voltage, however, because they were picked up by the strangers in outer space as a signal. The heaviside layer did not stop these wavelengths.

Professor Kennicot was startled one day when he heard, or thought he heard, a soundless voice in his mind.
"""

# 특수 문자 제거 및 소문자로 변환
clean_text = ''
for char in text:
    if char.isalnum() or char.isspace():#공백이나 숫자 영어
        clean_text += char.lower()

# 단어로 분리(공백기준)
words = clean_text.split()
#print(words)
# 단어 빈도수 계산
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# 빈도수 상위 2개 추출
most_common_word = max(word_counts, key=word_counts.get)
most_common_word_count = word_counts[most_common_word]
word_counts.pop(most_common_word)   #빈도수가 가장 높은값 제거
second_most_common_word = max(word_counts, key=word_counts.get)
second_most_common_word_count = word_counts[second_most_common_word]

# 결과 출력
print(f"가장 많이 반복된 단어: {most_common_word} ({most_common_word_count}회)")
print(f"두 번째로 많이 반복된 단어: {second_most_common_word} ({second_most_common_word_count}회)")'''

#추가문제 4)
'''text = """
The first they had heard of the strangers from outer space was when the new ultra short-wave frequencies were used. Professor Kennicot of Palmira University was the first to find how to generate and control them. He tried to transform the wavelengths upward to a range either auditory or visual but for some reason power was lost in the process.

Apparently he gave them a sufficient jolt with extra voltage, however, because they were picked up by the strangers in outer space as a signal. The heaviside layer did not stop these wavelengths.

Professor Kennicot was startled one day when he heard, or thought he heard, a soundless voice in his mind.
"""

# 특수 문자와 공백 제거, 소문자로 변환
clean_text = ''
for char in text:
    if char.isalpha():#숫자추출
        clean_text += char.lower()

# 알파벳 빈도수 계산
char_counts = {}
for char in clean_text:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

# 가장 많이 나타난 알파벳 추출
most_common_char = max(char_counts, key=char_counts.get)
most_common_char_count = char_counts[most_common_char]

# 결과 출력
print(f"가장 많이 나타난 알파벳 문자: {most_common_char} ({most_common_char_count}회)")
'''

#추가문제 5)
'''text = """
The first they had heard of the strangers from outer space was when the new ultra short-wave frequencies were used. Professor Kennicot of Palmira University was the first to find how to generate and control them. He tried to transform the wavelengths upward to a range either auditory or visual but for some reason power was lost in the process.

Apparently he gave them a sufficient jolt with extra voltage, however, because they were picked up by the strangers in outer space as a signal. The heaviside layer did not stop these wavelengths.

Professor Kennicot was startled one day when he heard, or thought he heard, a soundless voice in his mind.
"""

# 특수 문자와 공백 포함, 소문자로 변환
clean_text = ''
for char in text:
    if char.isalnum() or char in ['.', ',']:
        clean_text += char.lower()

# 글자 빈도수 계산
char_counts = {}
for char in clean_text:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

# 빈도수 상위 2개 추출
most_common_char = max(char_counts, key=char_counts.get)
most_common_char_count = char_counts[most_common_char]
char_counts.pop(most_common_char)   #가장 빈도수가 높은것 제거
second_most_common_char = max(char_counts, key=char_counts.get)
second_most_common_char_count = char_counts[second_most_common_char]

# 결과 출력
print(f"두 번째로 많이 나타난 글자: {second_most_common_char} ({second_most_common_char_count}회)")
'''
#추가문제 6)
'''text = """
The first they had heard of the strangers from outer space was when the new ultra short-wave frequencies were used. Professor Kennicot of Palmira University was the first to find how to generate and control them. He tried to transform the wavelengths upward to a range either auditory or visual but for some reason power was lost in the process.

Apparently he gave them a sufficient jolt with extra voltage, however, because they were picked up by the strangers in outer space as a signal. The heaviside layer did not stop these wavelengths.

Professor Kennicot was startled one day when he heard, or thought he heard, a soundless voice in his mind.
"""

# 알파벳 세트
alphabet_set = set('abcdefghijklmnopqrstuvwxyz')

# 텍스트에서 알파벳만 추출하여 소문자로 변환
used_chars = set()
for char in text:
    if char.isalpha():
        used_chars.add(char.lower())

# 사용되지 않은 알파벳 찾기
unused_chars = alphabet_set - used_chars

# 결과 출력
if unused_chars:
    print(f"나타나지 않은 알파벳: {', '.join(sorted(unused_chars))}")
else:
    print("나타나지 않은 알파벳은 없습니다")
'''
#추가문제 7)
'''text = """
The first they had heard of the strangers from outer space was when the new ultra short-wave frequencies were used. Professor Kennicot of Palmira University was the first to find how to generate and control them. He tried to transform the wavelengths upward to a range either auditory or visual but for some reason power was lost in the process.

Apparently he gave them a sufficient jolt with extra voltage, however, because they were picked up by the strangers in outer space as a signal. The heaviside layer did not stop these wavelengths.

Professor Kennicot was startled one day when he heard, or thought he heard, a soundless voice in his mind.
"""

# 특수 문자 제거 및 소문자로 변환
clean_text = ''
for char in text:
    if char.isalnum() or char.isspace():
        clean_text += char.lower()

# 단어로 분리
words = clean_text.split()

# 알파벳별로 시작하는 단어들을 저장할 사전 생성
alphabet_words = {}
for word in words:
    first_letter = word[0]
    if first_letter in alphabet_words:
        alphabet_words[first_letter].add(word)
    else:
        alphabet_words[first_letter] = {word}

# 결과 출력
for letter in sorted(alphabet_words.keys()):
    print(f"{letter} : {', '.join(sorted(alphabet_words[letter]))}")
'''

#추가문제 8)
'''
# 구별 인구 문자열
guPopulation = "강남구:561800,강동구:428500,강북구:315800,강서구:585400,관악구:500000,광진구:360400,구로구:395300,금천구:231900,노원구:535300,도봉구:348200"

# 딕셔너리로 변환
population_dict = {}
items = guPopulation.split(',')
for item in items:
    gu, population = item.split(':')
    population_dict[gu] = int(population)

# 사용자 입력
num = int(input("정수를 입력하세요: "))

# 인구가 입력한 정수보다 작은 구 찾기
result = {}
for gu, population in population_dict.items():
    if population < num:
        result[gu] = population

# 결과 출력
if result:
    for gu, population in result.items():
        print(f"{gu}: {population}")
else:
    print("인구가 num보다 작은 구가 없습니다")'''

#추가문제 9)
'''def check_password_strength(password):
    length = len(password)
    special_chars = 0
    digits = 0
    uppercase = 0
    special_char_set = set("~`!@#$%^&*(),./?><|")

    for char in password:
        if char in special_char_set:
            special_chars += 1
        elif char.isdigit():
            digits += 1
        elif char.isupper():
            uppercase += 1

    if length > 10 and special_chars >= 2 and digits >= 1 and uppercase >= 1:
        return "안전함"
    elif 8 <= length <= 10 and special_chars >= 1 and digits >= 1:
        return "보통"
    elif 8 <= length <= 10 and (special_chars >= 1 or digits >= 1 or uppercase >= 1):
        return "보통이하"
    else:
        return "안전하지않음"

# 사용자로부터 비밀번호 입력 받기
password = input("비밀번호를 입력하세요: ")
strength = check_password_strength(password)
print(f"비밀번호 안전도: {strength}")
'''

#추가문제 10)
'''students_per_class = {
    2021: 23.0,2020: 23.4,
    2019: 24.5,2018: 26.2,
    2017: 28.2,2016: 29.3,
    2015: 30.0,2014: 31.9,
    2013: 31.9,2012: 32.5,
    2011: 33.1,2010: 33.7
}

# 1. 전해에 비해 가장 급격하게 학생 수가 줄어든 해는 언제인가?
max_decrease_year = None
max_decrease = 0

for year in range(2021, 2010, -1):
    decrease = students_per_class[year - 1] - students_per_class[year]
    if decrease > max_decrease:
        max_decrease = decrease
        max_decrease_year = year

print(f"전해에 비해 가장 급격하게 학생 수가 줄어든 해는 {max_decrease_year}년입니다.")

# 2. 학급당 학생 수가 30명 미만으로 떨어진 해는 언제인가?
below_30_years = []
for year, count in students_per_class.items():
    if count < 30:
        below_30_years.append(year)

print(f"학급당 학생 수가 30명 미만으로 떨어진 해는 {below_30_years}년입니다.")

# 3. 2010년부터 2021년 사이에 평균적으로 학급당 학생 수는 어느 정도 감소했는가?
total_decrease = students_per_class[2010] - students_per_class[2021]
average_decrease_per_year = total_decrease / (2021 - 2010)
print(f"2010년부터 2021년 사이에 평균적으로 학급당 학생 수는 {average_decrease_per_year:.2f}명 감소했습니다.")'''

#추가문제 11)
import collections
import string

def word_frequency(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # 소문자로 변환하고 구두점 제거
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    # 단어 분리
    words = text.split()

    # 단어 빈도수 계산
    counter = collections.Counter(words)

    # 빈도수 높은 순으로 정렬
    sorted_words = sorted(counter.items(), key=lambda item: item[1], reverse=True)

    # 출력
    for word, freq in sorted_words:
        print(f"{word}: {freq}")

# 파일 경로를 지정하고 함수 호출
word_frequency('input.txt')

