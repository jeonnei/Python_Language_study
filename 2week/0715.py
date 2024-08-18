#문제 2

'''def add(num1, num2, num3):
    return num1 + num2 + num3
 
add(2, 3, 5)
add(2, num3 = 5, num2 = 3)
add(2, num3 = "5", num2 = "3")
add(2, (num2 = 3), 5)

print(2, 3, sep = ",") '''

'''num = 3
def printNum3():
    print(num)
    num = 5
    print(num)
printNum3()'''

#문제 5)
'''def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
print(sum(100))'''

#문제 6)
'''import math
def dew_point(humid,temperature) :
    d1 = math.log(humid / 100)
    d2 = (17.62 * temperature) / (243.12 + temperature)
    return (243.12 * (d1 + d2)) / (17.62 - (d1 + d2))

a,b=map(int,input("습도와 온도를 입력하세요(예시:60,25):").split(','))
dew = dew_point(a,b)
print(f"이슬점:{dew:0.1f}")'''

#문제 7)
'''def PrintDate(year,month,day):
    month_list=["January", "February", "March", "April", "May", "June", "July", 
                "August","September",  "October", "November", "December"]
    print(f"Year:{year}")
    print(f"Month: {month_list[month-1]}")
    print(f"Day: {day}")
PrintDate(2022,9,20)
PrintDate(2023,3,3)'''

#문제 8)
'''def list_count(input_string):
    string = input_string.split()
    return len(string)

test_list="이것을 바꾸면 됩니다."   #결과 3
print(list_count(test_list))'''

#문제 10)
'''def GetWord(sen,pos):
    words = sen.split()
    if 1<=pos<=3:
        return words[pos-1]
print(GetWord("A beautiful day",1))
print(GetWord("A beautiful day",3))'''

#문제 11)
"""def is_leap_year(year):
    # 연도가 400으로 나누어지면 윤년
    if year % 400 == 0:
        return True
    # 연도가 100으로 나누어지면 윤년 아님
    elif year % 100 == 0:
        return False
    # 연도가 4로 나누어지면 윤년
    elif year % 4 == 0:
        return True
    # 나머지 경우는 윤년 아님
    else:
        return False

# 사용자로부터 입력을 받는 함수
# 사용자로부터 정수를 입력받습니다.
year = int(input("연도를 입력하세요: "))
# 윤년 여부를 확인합니다.
if is_leap_year(year):
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 윤년이 아닙니다.")"""

#문제 12)
'''import re
def get_second_word(sentence):
    # 문자열의 양끝에 있는 공백 문자를 제거합니다.
    trimmed_sentence = sentence.strip()
    # 단어를 공백 문자, 웹 문자, 줄바꿈 문자로 분리합니다.
    words = re.split(r'[ \t\n]', trimmed_sentence)
    # 두 번째 단어를 반환합니다.
    return words[1]

#검수
test_sentences = [
    "Hello world!",
    "\tThis is a test.",
    "Python programming language\n",
    "  Data science and machine learning  "
]
for sentence in test_sentences:
    print(f"입력 문장: '{sentence}'")
    print(f"두 번째 단어: '{get_second_word(sentence)}'")
    print()'''

#문제 13)
"""def print_scores(score1, score2, score3, ascending=False):
    scores = [score1, score2, score3]
    
    if ascending:
        scores.sort()  # 오름차순 정렬
        print("=오름차순 정렬=")
        for idx in range(len(scores)):
            rank = len(scores) - idx
            score = scores[idx]
            print(f"{rank}등: {score}")
    else:
        scores.sort(reverse=True)  # 내림차순 정렬
        print("=내림차순 정렬=")
        for idx in range(len(scores)):
            rank = idx + 1
            score = scores[idx]
            print(f"{rank}등: {score}")

a, b, c = map(int, input("성적 입력 (예시 13, 78, 45): ").split(','))

# 내림차순 정렬
print_scores(a, b, c)

# 오름차순 정렬
print_scores(a, b, c, ascending=True)"""

#문제 14)
"""def fibo_recur(n):
    if n <= 2:
        number = 1
    else:
       number = fibo_recur(n-1) + fibo_recur(n-2)
    return number

print(fibo_recur(6))"""

#문제 15)
"""def gcd(m, n):
    if m == n:
        return m
    elif m > n:
        return gcd(m - n, n)
    else:
        return gcd(m, n - m)

# 예시
print(gcd(4, 6)) 
print(gcd(10, 15))"""

#문제 16)
"""def reverse_string(s):
    #문자열이 비어있거나 길이가 1인 경우
    if len(s) <= 1:
        return s
    #문자열의 첫 번째 문자를 제외한 나머지 부분을 뒤집고 맨 앞에 첫 번째 문자를 붙임
    return reverse_string(s[1:]) + s[0]

# 예시
print(reverse_string("hello"))  
print(reverse_string("apple"))  
"""
#문제 17)
"""def hello(*names):
      for each in names: #names 내의 모든 요소들을 순서대로 참조하는 순환문
            print('안녕, {}!'.format(each))
 
hello('민정')
hello('David','Veronica','Paul')
hello('방탄소년단','블랙핑크')"""

#문제 18)
def factorial(n):
    if n == 0 or n == 1:    #0이나 1 은 1출력
        return 1
    else:
        return n * factorial(n - 1)
#예시출력
print(factorial(5))
print(factorial(4))
print(factorial(3))