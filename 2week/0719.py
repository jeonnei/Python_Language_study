#문제 2)
"""try:
    n = int(input("정수를 입력하세요: "))
except ValueError:
    print("정수를 입력해야합니다.")"""

#문제 3)
"""try:
    s = input("정수를 입력하세요: ")
    n = int(s)
except ValueError:
    print("숫자를 입력하지 않았어요")"""

#문제 4)
"""import sys

def read_file():
    while True:
        file_name = input("파일 이름을 입력하세요: ")
        try:
            with open(file_name, 'r') as file:
                print(file.read())
                break
        except FileNotFoundError:
            print("파일이 존재하지 않습니다. 다시 입력해주세요.")
            if input("다시 파일 이름을 입력하시겠습니까? (y/n): ").lower() != 'y':
                print("프로그램을 종료합니다.")
                sys.exit()
read_file()"""

#문제 5-1)
'''try:
    A = [1, 2, 3]
    A[3]
except IndexError as e:
    print(type(e))'''

#문제 5-2)
'''try:
    {'fb': 11, 'bb': 9, 'vb': 6}['foot']
except KeyError as e:
    print(type(e))'''

#문제 5-3)
'''try:
    pl = 'python' + 3
except TypeError as e:
    print(type(e))'''

#문제 6)
'''def divide(x, y):
    try:
        answer = x / y
    except ZeroDivisionError:
        return "0으로는 나눌 수 없습니다."
    else:
        return answer

# 함수 호출 예시
result1 = divide(8, 5)
result2 = divide(8, 0)

print(result1)  # 1.6
print(result2)  # 0으로는 나눌 수 없습니다.'''
#문제 7)
'''try:
    print(int("abc"))
except Exception as e:
    print(f"예외 발생 이름: {type(e)}") 
print(f"예외 발생 이유: {e}") 
else:
    print("잘 실행됐습니다.")
finally:
    print("예외 처리가 잘되는군요!")'''
'''try:
    print(int("10"))
except Exception as e:
    print(f"예외 발생 이름: {type(e)}")
    print(f"예외 발생 이유: {e}")
else:
    print("잘 실행됐습니다.")
finally:
    print("예외 처리가 잘되는군요!")'''


#문제 8)
'''try:
    s = input("정수를 입력하세요: ")
    n = int(s)
except ValueError:
    print("오류: 정수로 변환할 수 없는 값을 입력했습니다.")
else:
    print(f"사용자가 입력한 정수: {n}")
finally:
    print("프로그램 종료")
'''

#문제 9)
'''try:
    with open('10차이론.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
else:
    print("파일을 성공적으로 읽었습니다.")
    print(content)
finally:
    print("파일 읽기 작업이 종료되었습니다.")'''

#문제 10)
'''def calculator():
    try:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))
        operator = input("연산자를 입력하세요 (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            raise ValueError("잘못된 연산자입니다")

        print(f"결과: {result}")
        print("계산이 성공적으로 완료되었습니다.")

    except ValueError as ve:
        print(f"입력 오류 발생: {ve}")
    except ZeroDivisionError:
        print("오류: 0으로 나눌 수 없습니다.")
    except Exception as e:
        print(f"알 수 없는 오류 발생: {e}")
while(1):
    calculator()'''

#문제 11)
'''def sum_numbers():
    try:
        input_string = input("여러 개의 숫자를 쉼표로 구분하여 입력하세요: ")
        # 입력받은 문자열을 쉼표로 분리하여 각 숫자를 추출
        numbers = input_string.split(',')
        # 각 숫자를 정수로 변환하여 합계 계산
        total = sum(int(number) for number in numbers)
        print(f"입력한 숫자의 합계: {total}")
    except ValueError:
        print("오류: 숫자가 아닌 값이 포함되어 있습니다.")

sum_numbers()'''

'''import random
def generate_lotoo_numbers():
    numbers=[]
    for i in range(6):
        a = random.randint(1,46)
        while a in numbers:
            a=random.randint(1,46)
        numbers.append(a)
    numbers = sorted(numbers)
    return numbers
numbers=generate_lotoo_numbers()
print(numbers)'''

'''def solution(matrix):
    n = len(matrix)  # 행렬의 크기 (n x n)
    answer= [[0] * n for _ in range(n)]  # 회전된 행렬을 저장할 빈 리스트 생성
    print(n)
    print(answer)
    for i in range(n):
        for j in range(n):
            # 회전된 행렬의 각 요소를 원래 행렬의 적절한 위치에서 복사
            answer[j][n - 1 - i] = matrix[i][j]

    return answer

# 예시 테스트
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]'''

def solution(matrix):
    # 행렬이 비어있거나, 행렬이 비어있는 리스트를 포함하는 경우를 처리
    if not matrix or not matrix[0]:  
        print("Input matrix is empty or contains empty lists.")
        return []

    n = len(matrix)  # 행렬의 행 수 (n x n 가정)
    m = len(matrix[0])  # 행렬의 열 수

    # 행렬이 정사각형이 아닌 경우를 처리
    for row in matrix:
        if len(row) != m:
            print(f"Input matrix is not square. Row {row} has length {len(row)} instead of {m}.")
            raise ValueError("Input matrix must be square (n x n).")
    
    if n != m:
        print(f"Input matrix is not square. Matrix has {n} rows and {m} columns.")
        raise ValueError("Input matrix must be square (n x n).")

    # 디버깅: 입력 행렬 출력
    print("Input matrix:")
    for row in matrix:
        print(row)
    
    answer = [[0] * n for _ in range(n)]  # 회전된 행렬을 저장할 빈 리스트 생성

    for i in range(n):
        for j in range(n):
            # 디버깅: 각 단계의 값을 출력
            print(f"Setting answer[{j}][{n - 1 - i}] to matrix[{i}][{j}] ({matrix[i][j]})")
            answer[j][n - 1 - i] = matrix[i][j]
    
    # 디버깅: 결과 행렬 출력
    print("Rotated matrix:")
    for row in answer:
        print(row)

    return answer

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# 비어 있는 행렬
print(solution([]))

# 빈 리스트를 포함하는 행렬
print(solution([[], [], []]))

# 정사각형이 아닌 행렬
try:
    print(solution([[1, 2], [3, 4, 5]]))
except ValueError as e:
    print(e)
