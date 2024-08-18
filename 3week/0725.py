#문제 2)
"""# 1부터 100까지의 정수를 가진 리스트 생성
sequence = list(range(1, 101))

# 사용자로부터 정수 입력 받기
user_input = int(input("정수를 입력하세요: "))

# 입력 받은 정수가 리스트에 있는지 확인
if user_input in sequence:
    print(True)
else:
    print(False)"""

#문제 3)
# 리스트와 튜플을 연결하려고 시도
"""list_example = [1, 2, 3]
tuple_example = (4, 5, 6)

try:
    result = list_example + tuple_example
except TypeError as e:
    print(f"Error: {e}") 
# 문자열과 바이트를 연결하려고 시도
string_example = "hello"
bytes_example = b"world"

try:
    result = string_example + bytes_example
except TypeError as e:
    print(f"Error: {e}") 
# 리스트와 문자열을 연결하려고 시도
list_example = [1, 2, 3]
string_example = "456"

try:
    result = list_example + string_example
except TypeError as e:
    print(f"Error: {e}")  
# 튜플과 튜플을 연결
tuple_example1 = (1, 2, 3)
tuple_example2 = (4, 5, 6)

try:
    result = tuple_example1 + tuple_example2
    print(result)  
except TypeError as e:
    print(f"Error: {e}")"""

#문제 4)
"""list_1 = [1, 2, 3]
tup_1 = (4, 5, 6)

# 튜플을 리스트로 변환
list_2 = list(tup_1)

# 두 리스트를 연결
result = list_1 + list_2

print(result)  # 출력: [1, 2, 3, 4, 5, 6]"""

#문제 6)
"""my_tuple = (1, 2, 3, 4, 5)
# 리스트 컴프리헨션을 사용하여 3을 제외한 새로운 리스트 생성
new_list = [x for x in my_tuple if x != 3]
# 새로운 리스트를 튜플로 변환
new_tuple = tuple(new_list)
print(new_tuple)  # 출력: (1, 2, 4, 5)"""

#문제 8)
"""alp = ['a', 'b', 'c', 'd', 'e']
del alp[3]
print(alp)  # 출력: ['a', 'b', 'c', 'e']"""

#문제 9)
"""alp = ['a', 'b', 'c', 'd']
del alp[:]
print(alp) """

#문제 10)
"""def is_palindrome(word):
    # 문자열을 뒤집어서 원래 문자열과 비교
    return word == word[::-1]

# 테스트
test_word = "radar"
print(is_palindrome(test_word)) """

#문제 11)
"""# 주어진 문자열
data = '잣밤배귤감'

# 문자열을 리스트로 변환
data_list = list(data)

# 리스트를 오름차순으로 정렬
data_list.sort()

# 오름차순으로 정렬된 리스트 출력
print("오름차순 정렬:", data_list)

# 리스트를 역순으로 정렬
data_list.sort(reverse=True)

# 역순으로 정렬된 리스트 출력
print("역순 정렬:", data_list)"""

#문제 12)
"""strings = ["mango", "apple", "banana", "cherry", "date", "fig", "apple", "banana"]

# 중복된 단어 제거
unique_strings = list(set(strings))

# 오름차순으로 정렬
unique_strings.sort()

print(unique_strings)  
"""

#추가문제 1)
"""even = [i for i in range(2, 11, 2)]
print(even)"""

#추가문제 2)
"""s = [i**2 for i in range(10) if i % 2 == 1]
print(s)"""
#추가문제 3)
"""mylist = [1, 5, 1, 7, 1]
mylist[mylist.count(1)] = 70
mylist[len(mylist) - 1] = 80
mylist.insert(1, 50)
print(mylist)
"""
#추가문제 4)
"""import random

# 1에서 99까지의 난수 10개로 리스트 생성
random_list = [random.randint(1, 99) for _ in range(10)]

print("원본 리스트:", random_list)

# 오름차순
sorted_list = sorted(random_list)
print("정렬된 리스트:", sorted_list)
# 내림차순
reverse_sorted_list = sorted(random_list, reverse=True)
print("역순 리스트:", reverse_sorted_list)
"""
#추가문제 5)
"""# 한글과 영어에 대응되는 튜플 생성
korean = ('정렬', '문자', '내포', '사전')
english = ('sorting', 'text', 'comprehension', 'dictionary')

# 표준 입력으로 한글 단어를 입력받음
input_korean = input("한글 단어를 입력하세요: ")

# 한글 단어가 튜플 korean에 있는지 확인
if input_korean in korean:
    # 인덱스를 사용해 대응되는 영어 단어 출력
    index = korean.index(input_korean)
    print(f"영어 단어: {english[index]}")
else:
    # 단어가 사전에 없으면 적절한 메시지 출력
    print("해당 단어는 사전에 없습니다.")"""

#추가문제 6)
"""data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

# 각 행의 합 구하기
rsum = [sum(row) for row in data]

# 각 열의 합 구하기
csum = [sum(col) for col in zip(*data)]

print("각 행의 합:", rsum)
print("각 열의 합:", csum)"""

#추가문제 7)
"""m = [[1, 2], [3, 4], [5, 6], [7, 8]]

# 행과 열을 바꾸는 리스트 컴프리헨션
transpose = [[row[i] for row in m] for i in range(len(m[0]))]

# 변환된 리스트 출력
print(transpose)"""

#추가문제 8)
import random

# 1에서 20까지의 난수 5개를 생성하여 집합 A와 B에 저장
A = set(random.sample(range(1, 21), 5))
B = set(random.sample(range(1, 21), 5))

union_set = A | B  # 합집합
intersection_set = A & B  # 교집합
difference_set = A - B  # 차집합
complement_set = B - A  # 여집합

print(f"집합 A: {A}")
print(f"집합 B: {B}")
print(f"합집합: {union_set}")
print(f"교집합: {intersection_set}")
print(f"차집합 (A - B): {difference_set}")
print(f"여집합 (B - A): {complement_set}")




