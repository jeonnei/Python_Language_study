#문제 2)
"""increment = lambda x: x + 1
print(increment)
"""

#문제 3)

"""process_number = lambda x: x**2 if x % 2 == 0 else x

#테스트
test_number = 5
result = process_number(test_number)
print(f"입력받은 정수: {test_number}, 결과: {result}")"""

#문제 4)
"""# 람다 함수 정의
lambda_func = lambda x: x**2 if x % 2 == 0 else x

# 리스트
numbers = [1, 2, 3, 4, 5]

# map 함수를 사용하여 람다 함수를 numbers 리스트에 적용
result = map(lambda_func, numbers)

# map 객체를 리스트로 변환하여 출력
print(list(result)) """

#문제 5)
"""checkNum = lambda x: x if x < 3 else (x * 2 if x < 6 else x * 3)

numbers = [2, 3, 4, 5, 6, 7]
result = map(checkNum, numbers)
print(list(result))
"""

#문제 6)
"""def calculate_elements(list1, list2):
    result = []
    for i in range(len(list1)):
        if list1[i] % 2 == 0:  # list1의 요소가 짝수이면
            result.append(list1[i] + list2[i])  # list2의 요소를 더함
        else:  # list1의 요소가 홀수이면
            result.append(list1[i] * list2[i])  # list2의 요소를 곱함
    return result

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

result = calculate_elements(list1, list2)
print(result)"""

#문제 7)
"""
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

# 람다 함수를 사용하여 리스트 요소들을 처리
result = list(map(lambda x, y: x + y if x % 2 == 0 else x * y, list1, list2))

print(result)"""

#문제 8)
"""words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# 'a'를 포함하는 단어를 걸러내는 함수 정의
def contains_a(word):
    return 'a' in word

# filter 함수를 사용하여 'a'를 포함하는 단어 걸러내기
filtered_words = list(filter(contains_a, words))

print(filtered_words)"""

#문제 9)
"""words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# 람다 함수를 사용하여 'a'를 포함하는 단어 걸러내기
filtered_words = list(filter(lambda word: 'a' in word, words))

print(filtered_words)
"""

#문제 10)
"""def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("정수를 입력하세요: "))
if is_prime(number):
    print(f"{number}는 소수입니다.")
else:
    print(f"{number}는 소수가 아닙니다.")

"""

#추가문제 1)
"""
# GCD를 구하는 함수
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 리스트에 있는 여러 숫자의 GCD를 구하는 함수
def gcd_list(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = gcd(result, number)
    
    return result

# 주어진 리스트
numbers = [48, 64, 16, 32]

# 결과 출력
print("리스트에 있는 숫자들의 최대공약수는:", gcd_list(numbers))
"""

#추가문제 2_
"""
# GCD를 구하는 람다 함수
gcd = lambda a, b: a if not b else gcd(b, a % b)

# 리스트에 있는 여러 숫자의 GCD를 구하는 함수 (reduce 사용 안 함)
def gcd_list(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = gcd(result, number)
    return result

# 주어진 리스트
numbers = [48, 64, 16, 32]

# 결과 출력
print("리스트에 있는 숫자들의 최대공약수는:", gcd_list(numbers))
"""
#추가문제 3)
"""data = {'apple': 5, 'banana': 2, 'orange': 8, 'kiwi': 3}
sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

print(sorted_data)
"""
#추가문제 4)
data = {'apple': 5, 'banana': 2, 'orange': 8, 'kiwi': 3}

def sort_dict_by_value(d):
    # 딕셔너리의 아이템들을 값 기준으로 정렬
    sorted_items = sorted(d.items(), key=lambda item: item[1])
    # 정렬된 결과를 다시 딕셔너리로 변환하여 반환
    return dict(sorted_items)

sorted_data = sort_dict_by_value(data)

print(sorted_data)

