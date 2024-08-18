#문제 2)
"""
import re #정규표현식을 사용하여 문자열 검색, 매칭, 치환 등의 작업을 수행할 수
            # 있게 해주는 모듈
# 테스트할 문장 목록
sentences = [ "I love programming in Python.",
"JavaScript is a versatile language.",
"The Python snake is a non-venomous species."]

# 정규표현식 패턴
pattern = r'Python'

# 문장 판별
for sentence in sentences:
    if re.search(pattern, sentence):
        print(f"'Python' found in: \"{sentence}\"")
    else:
        print(f"'Python' not found in: \"{sentence}\"")
"""
#문제 4)
"""
import re

text = "alice@example.com 이 첫 번째 이메일이고, 다음은 bob.smith@mail.co.uk 입니다."

# 일반 문자열로 이메일 패턴을 정의
pattern = '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'

# findall 메소드를 이용해 문자열에서 패턴에 매칭되는 모든 이메일 주소 찾기
matches = re.findall(pattern, text)
#print(matches)
if matches:
    for match in matches:
        print(match)
else:
    print("이메일 주소를 찾을 수 없습니다.")"""

#문제 5)
"""
import re

text = "Hello, how are you today? Hello, I'm fine."
# 일반 문자열로 'Hello'로 시작하는지 확인하는 패턴 정의
pattern = r'^Hello'

# match 메소드를 이용해 문자열의 시작에서 패턴에 매칭되는지 확인
match = re.match(pattern, text)

if match:
    print("문자열은 'Hello'로 시작합니다.")
else:
    print("문자열은 'Hello'로 시작하지 않습니다.")
"""
#문제 6)
"""
import re

text = "This is a sample text with the word 'sample' in it."
pattern = r'sample'
match = re.search(pattern, text)

if match:
    print("문자열에 'sample' 단어가 포함되어 있습니다.")
else:
    print("문자열에 'sample' 단어가 포함되어 있지 않습니다.")
"""

#문제 9)
"""import re

text = "상품의 가격은 19.99달러와 100.0달러, 0.99달러 입니다."

# 소수점을 포함한 숫자를 찾는 정규표현식 패턴 정의
pattern = r'\\d+\\.\\d+'

# findall 메소드를 이용해 문자열에서 패턴에 매칭되는 모든 숫자 찾기
matches = re.findall(pattern, text)

# 결과 출력
for match in matches:
    print(match)"""

#문제 10)
"""import re

text = "<html><head><title>Test</title></head><body><h1>Header</h1><p>Paragraph</p></body></html>"

# 모든 태그를 찾는 패턴 정의
pattern = r'<[^>]+>'

# findall 메소드를 사용하여 모든 태그 찾기
matches = re.findall(pattern, text)

# 결과 출력
if matches:
    for match in matches:
        print(match)
else:
    print("태그를 찾을 수 없습니다.")
"""

#문제 11)
"""import re

def check_password_strength(password):
    # 최소 8자 이상, 숫자와 특수문자를 포함하는지 확인하는 정규표현식
    pattern = r'^(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-zA-Z]).{8,}$'
    return bool(re.match(pattern, password))

# 테스트
password1 = "StrongPassword123!"
print(f"Password '{password1}' is strong: {check_password_strength(password1)}")

newPswd = input('\n패스워드를 입력하세요: ')
if check_password_strength(newPswd):
    print('안전한 패스워드입니다.')
else:
    print('패스워드의 기준에 맞지 않습니다')
"""
#문제 12)
import re

text = "Hello! @world! This is 2024. @#$%^&*"

pattern = r'[^\w\s]'

cleaned_text = re.sub(pattern, '', text)

print(cleaned_text)
