#문제 2)
"""
numbers = [1, 2, 3, 4, 5]

# 리스트를 이터레이터로 변환
iterator = iter(numbers)

# next() 함수를 이용해 요소 출력
print(next(iterator)) 
print(next(iterator))  
print(next(iterator))  
print(next(iterator))
print(next(iterator)) 

"""
#문제 3)
"""numbers = [1, 2, 3, 4, 5]

# 리스트를 이터레이터로 변환
iterator = iter(numbers)

# next() 함수를 이용해 요소 출력
try:
    while True:
        print(next(iterator))
except StopIteration:
    print("반복이 끝났습니다.")"""

#문제 5)
"""class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# 사용 예제
numbers = [1, 2, 3, 4, 5]
iterator = MyIterator(numbers)

for num in iterator:
    print(num)"""

#문제 6)
"""class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.data[index]

# 사용 예제
numbers = [1, 2, 3, 4, 5]
iterator = MyIterator(numbers)

for num in iterator:
    print(num)

# 인덱스를 통한 접근
print(iterator[2])  
"""

#문제 7)
"""def file_line_iterator(file_path):
    # 파일을 열고, 각 줄을 반환하는 이터레이터를 작성합니다.
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# 예제 파일을 생성하고 테스트해 보겠습니다.
with open('example.txt', 'w') as f:
    f.write("First line\\n")
    f.write("Second line\\n")
    f.write("Third line\\n")

# 파일 경로를 입력하여 이터레이터를 생성하고 사용합니다.
iterator = file_line_iterator('example.txt')

for line in iterator:
    print(line)"""

#문제 8)
"""
class FibonacciIterator:
    def __init__(self):
        self.a, self.b = 0, 1  # 첫 두 숫자 초기화

    def __iter__(self):
        return self  # 이터레이터 객체 반환

    def __next__(self):
        if self.a > 100:  # 100을 넘으면 멈춤
            raise StopIteration
        current = self.a  # 현재 숫자 저장
        self.a, self.b = self.b, self.a + self.b  # 다음 피보나치 숫자 계산
        return current  # 현재 숫자 반환

# 사용 예시
fib_iter = FibonacciIterator()

for number in fib_iter:
    print(number)"""

#문제 10)
"""def fibonacci_generator():
    a, b = 0, 1  # 첫 두 숫자 초기화
    while a <= 100:  # 100을 넘으면 멈춤
        yield a  # 현재 숫자 반환
        a, b = b, a + b  # 다음 피보나치 숫자 계산

for number in fibonacci_generator():
    print(number)"""

#추가문제 1)
"""def fsm_generator():
      state = 'START'
      while True:
            input_char = yield state
            if state == 'START':
                if input_char == 'a':
                    state = 'STATE_A'
            elif state == 'STATE_A':
                if input_char == 'b':
                    state = 'STATE_B'
                else:
                    state = 'START'
            elif state == 'STATE_B':
                if input_char == 'a':
                    state = 'STATE_A'
                elif input_char == 'b':
                    state = 'STATE_B'
                else:
                    state = 'START'

# 사용 예시: 문자열을 입력하여 상태 변화를 추적
fsm = fsm_generator()
next(fsm) # 제네레이터 초기화

input_string = "ababab"
for char in input_string:
      state = fsm.send(char)
      print(f"Input: {char}, State: {state}")

"""
#추가문제 2)
def process_line(line):
    # 각 줄에 대해 추가 처리를 수행하는 함수
    print(f"Processing line: {line}")

def read_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

def filter_lines(lines, keyword):
    for line in lines:
        if keyword in line:
            yield line

# 제네레이터 사용 예시
file_path = 'example.txt'
keyword = 'search_term'

lines = read_lines(file_path)
filtered_lines = filter_lines(lines, keyword)

for line in filtered_lines:
    process_line(line)

"""#추가문제 5)
import asyncio

async def simple_coroutine(): # async def 는 코루틴 함수를 정의
    print("코루틴 시작")
    await asyncio.sleep(1) # 1초간 대기
    print("코루틴 종료")

def call_coroutine():
    coroutine = simple_coroutine() # 코루틴 객체 생성
    asyncio.run(coroutine) # 코루틴 실행

call_coroutine()
"""