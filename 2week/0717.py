#문제 3)
"""lst2 = list()
print(lst2)"""

#문제 4)

"""for ch in "hello":
    print(ch)
"""

#문제 6)
'''print("He is not my type, \tthanks".split(" \t"))
print("He is not my type, \tthanks".split(" ", 2))
print("He is not my type, \tthanks".split("t"))'''

#문제 7)
'''my = (1, 2)
my.append([3, 4])
'''

#문제 10)
'''
my_list = [1, 2, 3, 4]

my_tuple = tuple(my_list)
print("튜플:", my_tuple)

new_list = list(my_tuple)
print("리스트:", new_list)'''

#문제 11)
"""def input_int(n):
    count = 0
    result = []
    for i in range(1,n+1):
        if(n%i==0):
            result.append(i)
    for _ in result:
        count=count+1
    return count

for i in range(2,21):
    result = input_int(i)
    print(f"{i}의 약수 개수:{result}")"""

#문제 12)
"""arr = [1,2,2,3,4,4,5]
result = [] # 중복 제거된 값들이 들어갈 리스트

for value in arr:
    if value not in result: #value가 result안에 없으면 추가
        result.append(value)

print(result)"""

#문제 13)
'''def get_integer(n1,n2):
    result = []
    for i in range(n1,n2+1):
        for j in range(1,i+1):
            if(i%j==0):
                result.append(j)
        print(f"{i}의 약수는{result}")
        result=[]

get_integer(10,16)'''

#문제 14)
'''def get_sumlist(list1,list2):
    sum_list = []
    sum_list = list1+list2
    sum_list.sort()
    return sum_list


list1=[1,5,8,10,14]
list2=[2,4,5,9]
print(get_sumlist(list1,list2))
'''
#문제 15)
"""def create_list(n):
    integer_list = []
    for i in range(n):
        num = int(input(f"정수를 입력하세요 ({i+1}/{n}): "))
        integer_list.append(num)
    return integer_list

# 사용자 입력을 받아 n개의 정수 리스트 생성
n = int(input("정수의 개수를 입력하세요: "))
result_list = create_list(n)

# 생성된 리스트 출력
print("입력받은 정수 리스트:", result_list)"""

#문제 16)
"""def createDivisorsList(n):
    lists = []
    for i in range(1,n+1):
        if n%i==0:
            lists.append(i)
    return lists

n=int(input("1~1000정수 하나만 입력 :"))
result_list = createDivisorsList(n)

print(f"{n}의 모든 약수:",result_list)
result_sum = sum(result_list)
print(f"{n}의 모든 약수의 합:",result_sum)"""

#문제 17)
"""def create_tuple(n):
    integer_list = []
    for i in range(n):
        num = int(input(f"정수를 입력하세요 ({i+1}/{n}): "))
        integer_list.append(num)
    integer_tuple = tuple(integer_list)
    return integer_tuple

# 사용자 입력을 받아 n개의 정수 리스트 생성
n = int(input("정수의 개수를 입력하세요: "))
result_tuple = create_tuple(n)

# 생성된 리스트 출력
print("입력받은 정수 튜플:", result_tuple)"""

#문제 19)
"""data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 각 행의 합을 저장할 리스트
rsum = []
# 각 열의 합을 저장할 리스트 초기화
columns = len(data[0])  # 열의 개수
csum = [0] * columns
# 행의 합 계산 및 출력
for row in data:
    row_sum = sum(row)
    rsum.append(row_sum)
    print(f"행의 합: {row_sum}")
# 열의 합 계산
for row in data:
    for j in range(columns):
        csum[j] += row[j]
# 열의 합 출력
for index, col_sum in enumerate(csum):
    #print(index,col_sum)
    print(f"열 {index+1}의 합: {col_sum}")"""

#문제 20)
"""def find_second(lst):
    sorted_list=sorted(lst) #오름차순 정렬
    return sorted_list[-2]  #뒤에서 두번째 값 반환
data=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for idx, lst in enumerate(data):    #각 리스트별로 두 번째로 큰 값 출력
    #print(idx,lst)
    second_large = find_second(lst)
    print(f"{idx+1}번째 리스트의 두 번째로 큰 값: {second_large}")"""

#문제 21)
'''lst = [[1,2],[3,4],[5,6],[7,8]]

# 행과 열을 맞춰 출력
print("행과 열을 맞춰 출력:")
for row in lst:#1
    #print(row)
    for elem in row:#4
        print(elem, end=' ')
    print()
#print(len(lst))
# 행과 열을 바꾼 형태로 출력
print("\n행과 열을 바꾼 형태로 출력:")
for i in range(len(lst[0])):#2
    #print(i)
    for j in range(len(lst)):#4
        print(lst[j][i], end=' ')
    print()
'''

#문제 22)
import random

# 1에서 99까지의 난수 10개로 리스트 생성
random_list = [random.randint(1, 99) for _ in range(10)]

# 리스트를 튜플로 변환
tuple_from_list = tuple(random_list)

# 튜플을 정렬하여 정렬된 리스트로 만듦
sorted_list = sorted(tuple_from_list)

# 전체 합, 최대값, 최소값 계산
total_sum = sum(sorted_list)
max_value = max(sorted_list)
min_value = min(sorted_list)
average = total_sum / len(sorted_list)

# 결과 출력
print("원본 리스트:", random_list)
print("변환된 튜플:", tuple_from_list)
print("정렬된 리스트:", sorted_list)
print("전체 합:", total_sum)
print("최대값:", max_value)
print("최소값:", min_value)
print("평균:", average)