
#문제 5)
"""def max_find(numbers):
    max_value = numbers[0]  #리스트의 첫번째 값을 최대값으로 지정
    for i in numbers:
        if i>max_value:
            max_value=i     #현재 숫자가 최대값 보다 크면 최대값으로 저장
    return max_value

while True:
    input_numbers = input("0보다 큰 양수 5개를 공백으로 구분하여 입력하세요: ")
    numbers = list(map(int, input_numbers.split()))
    
    if len(numbers) == 5:
        break
    else:
        print("다시 입력하세요. 5개의 숫자를 입력해야 합니다.")

# 최대값 찾기
max_value = max_find(numbers)

# 결과 출력
print("입력된 숫자들 중 가장 큰 값은:", max_value)"""

#문제 6-1
'''i=100
total = 0
while(i<=199):
    total +=i
    i+=1
print(total)'''

#문제 6-2
'''i=100
total = 0
while(i<=199):
    if(i%2==0):
        total +=i
    i+=1
print(total)
'''
#문제 6-2
'''i=100
total = 0
while(i<=199):
    if(i%3==0):
        total +=i
    i+=1
print(total)'''

#문제 7)
'''def getSum(start, end, divisor=None):
    total = 0
    current = start

    while current <= end:
        if divisor is None or (divisor is not None and current % divisor == 0):
            total += current    #divisor이 0 또는 current%divisor==0일때 참
        current += 1
    return total

# (1) 100 ~ 199까지의 합계 계산
sum1 = getSum(100, 199)
print("100 ~ 199까지의 합계:", sum1)

# (2) 100 ~ 199까지 짝수의 합계 계산
sum2 = getSum(100, 199, 2)
print("100 ~ 199까지 짝수의 합계:", sum2)

# (3) 100 ~ 199까지 3의 약수만 합계 계산
sum3 = getSum(100, 199, 3)
print("100 ~ 199까지 3의 약수만 합계:", sum3)'''

# 문제 8)
"""
def get_integer(x):
    result = []
    for i in range(1,x+1):
        if(x%i==0):
            result.append(i)
    return result

print(f"12의 약수는 {get_integer(12)}")
print(f"16의 약수는 {get_integer(16)}")
"""
# 문제 9)
"""def get_integer(n1,n2):
    result = []
    for i in range(n1,n2+1):
        for j in range(1,i+1):
            if(i%j==0):
                result.append(j)
        print(f"{i}의 약수는{result}")
        result=[]

get_integer(10,16)"""

#문제 10)
"""import random

def random_get():
    result_list=[]
    duplicates_count=0
    for _ in range(5):
        j=random.randint(1,6)
        result_list.append(j)
    
    # 중복된 숫자를 체크하고 중복된 숫자의 개수를 세는 방식
    for i in range(len(result_list)):
        for j in range(i + 1, len(result_list)):
            if result_list[i] == result_list[j]:
                duplicates_count += 1
                break  # 중복이 확인되면 더 이상 같은 숫자를 세지 않음

    print(result_list)
    print(f"중복된 숫자 개수: {duplicates_count}")

random_get()"""

#문제 11)
"""import random

def random_get():
    result_list=[]
    for i in range(10):
        j=random.randint(1,6)
        while(j>4):         #4보다 큰수가 나오면 작은수가 나올때까지 무작위 선택
            j=random.randint(1,6)#4보다 작은수가 나올때까지 무작위 선택
        result_list.append(j)
    print(result_list)

random_get()"""

#문제 10)
"""import random

def random_get():
    result_list = []

    for _ in range(5):
        j = random.randint(1, 6)
        result_list.append(j)

    print(f"무작위로 선택된 숫자들: {result_list}")
    # 중복된 숫자들을 저장할 리스트
    duplicates = []

    # 중복된 숫자를 체크하는 반복문
    for i in range(len(result_list)):
        for j in range(i + 1, len(result_list)):
            if result_list[i] == result_list[j] and result_list[i] not in duplicates:
                duplicates.append(result_list[i])

    # 중복된 숫자가 있는 경우 출력
    if duplicates:
        output = ", ".join(f"{num}이 {result_list.count(num)}번" for num in duplicates)
        print(f"{output} 중복으로 출력됐습니다.")
    else:
        print("중복된 숫자가 없습니다.")

# 함수 호출
random_get()
"""

#문제 12)
"""def remove_newline(input_string):
    # 마침표, 느낌표, 줄바꿈 기호를 빈 문자열로 replace하여 제거
    cleaned_string = input_string.replace(".", "").replace("!", "").replace("\n", "")
    return cleaned_string

# 주어진 문자열
input_string = "...What a beautiful day!\n"

# 함수 호출하여 처리된 결과를 출력
processed_string = remove_newline(input_string)
print(processed_string)"""

#문제 13)
"""
def cube_out():
    result=0
    i=1
    while(result<100):
        result = i*i*i
        if(result>=100):
            return i,result
        else:
            i+=1

answer = cube_out()
print(f"100을 넘는 최초의 a값은 {answer[0]}이고 {answer[1]}입니다")"""

#문제 14)
"""def find_numbers():
    numbers = []

    for n in range(1000, 10000):
        # 각 자리수 구하기
        n4 = n % 10
        n3 = (n // 10) % 10
        n2 = (n // 100) % 10
        n1 = (n // 1000) % 10

        # n1^4 + n2^4 + n3^4 + n4^4 계산
        sum= n1**4 + n2**4 + n3**4 + n4**4

        # 조건에 맞는 경우 special_numbers 리스트에 추가
        if sum == n:
            numbers.append(n)

    return numbers

special_numbers = find_numbers()
print("1000에서 9999 사이의 특별한 숫자들:")
for number in special_numbers:
    print(f"{number} = {number // 1000}^4 + {(number // 100) % 10}^4 + {(number // 10) % 10}^4 + {number % 10}^4")"""

#문제 15)
"""def find_prime():
    num = int(input("정수를 입력하세요 : "))
    if(num>1):      #1보다 클 때
        prime = True
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(f"{num}은 소수입니다.")
        else:
            print(f"{num}은 소수가 아닙니다.")
    else:
        print("%d는 소수가 아닙니다"%num)

while(1):
    find_prime()"""

#문제 16)
"""def find_result():
    for i in range(1,10):       #i=n1
        for j in range(1,10):   #j=n2
            sum = i*10+j+j*10+i
            if(sum==110):
                print(f"n1:{i},n2:{j}")

find_result()"""

#문제 17)
"""from random import randint
def coin_percentage(n):
    cnt=[0,0]   #앞,뒤
    for _ in range(n):
        cnt[0]+=randint(0,1)
    cnt[1]=n-cnt[0]
    print(f"{n}번 던졌을 때, 앞면이 나올 확률{cnt[0]/n}")
    print(f"{n}번 던졌을 때, 뒷면이 나올 확률{cnt[1]/n}")
    print()

coin_percentage(100)
coin_percentage(1000)
coin_percentage(10000)"""

#문제 18)
"""def printing_table():
    for i in range(0,11):
        for j in range(1,9):
            if(i==0):
                print(f"{j}*n",end='\t')
            else:
                print(f"{i*j}",end='\t')
        print()

printing_table()"""

#문제 19)
def calculate_compound_interest(principal, annual_rate, years):
    # 연간 복리 계산 횟수
    n = 1
    # 연이자율을 소수로 변환 (예: 5% -> 0.05)
    r = annual_rate / 100
    # 복리 총액 계산
    amount = principal * (1 + r / n) ** (n * years)
    # 총 이자액 계산
    interest = amount - principal
    return amount, interest

def print_compound_interest(principal, annual_rate, years):
    # 각 연도별로 계산 및 출력
    for year in range(1, years + 1):
        amount, interest = calculate_compound_interest(principal, annual_rate, year)
        print(f"{year}년: 복리총액 {amount:,.0f}원, 총이자액 {interest:,.0f}원")
# 입력 데이터
principal = 1000000  # 원금 (예: 1,000,000원)
annual_rate = 2.5    # 연이자율 (예: 2.5%)
years = 5            # 투자기간 (예: 5년)
# 복리 계산 결과 출력
print_compound_interest(principal, annual_rate, years)