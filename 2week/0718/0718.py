
#문제 )
'''with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello\nThis is data.txt\n이 파일은 utf-8 형식으로 저장했습니다\n")

# data.txt 파일에서 한 줄을 읽고 출력
with open("data.txt", "r", encoding="utf-8") as file:
    line = file.readline()
    print(line)'''

#문제 7)
'''with open("data.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())'''

#문제 8)
# data.txt 파일의 끝에 문자열 추가
'''with open("data.txt", "a", encoding="utf-8") as file:
    file.write("Here comes to the end.\n")

# 파일 내용을 확인하기 위해 출력
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())'''

#문제 9)
'''with open("python.utf8.txt", "r", encoding="utf-8") as f:
    s = f.read()
    print(s)
'''
#문제 10)
'''# 사용자로부터 새로운 파일 이름 입력 받기
new_file_name = input("새로운 파일 이름을 입력하세요: ")

# "data.txt" 파일 읽고 새로운 파일에 저장하기
with open("data.txt", "r", encoding="utf-8") as original_file:
    with open(new_file_name, "w", encoding="utf-8") as new_file:
        for line in original_file:
            new_file.write(line)

# 새로운 파일에 저장된 내용 확인하기 위해 출력
with open(new_file_name, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())'''

#문제 11)
"""# data2.txt 생성
content2 = "Hi\nThis is data2.txt\n두 번째 파일입니다\n"
with open('data2.txt', 'w', encoding='utf-8') as file2:
    file2.write(content2)

# Step 2: 두 파일의 내용을 각각 리스트로 읽어오기
list_data1 = []
list_data2 = []

# data.txt 읽어오기
with open('data.txt', 'r', encoding='utf-8') as file1:
    list_data1 = file1.readlines()
    list_data1 = [line.strip() for line in list_data1]  

# data2.txt 읽어오기
with open('data2.txt', 'r', encoding='utf-8') as file2:
    list_data2 = file2.readlines()
    list_data2 = [line.strip() for line in list_data2]  

# Step 3: 두 리스트를 연결하여 새로운 리스트 생성
list_data3 = list_data1 + list_data2

# Step 4: 새로 생성된 리스트의 내용을 세 번째 파일인 merged_data.txt에 저장
with open('data3.txt', 'w', encoding='utf-8') as data3_file:
    for item in list_data3:
        data3_file.write(item + '\n')

print("새로운 리스트가 data3.txt 파일에 저장되었습니다.")"""

#문제 12)
'''#사용자로부터 검색할 문자열 입력받기
search_string = input("검색할 문자열을 입력하세요: ")

#news.txt 파일에서 검색하여 포함된 모든 라인 번호 출력하기
found_line_numbers = []

# news.txt 파일 열기
with open('news.txt', 'r', encoding='utf-8') as file:
    # 파일의 각 줄을 순회하며 검색할 문자열이 포함되어 있는지 확인
    for line_num, line in enumerate(file, 1):  # line_num은 줄 번호 (1부터 시작)
        if search_string in line:
            found_line_numbers.append(line_num)

# 검색된 문자열이 포함된 모든 라인의 번호 출력
if found_line_numbers:
    print(f"검색된 문자열 '{search_string}'이(가) 포함된 라인 번호:")
    for line_num in found_line_numbers:
        print(line_num)
else:
    print(f"검색된 문자열 '{search_string}'이(가) 포함된 라인이 없습니다.")'''

#문제 13)
"""#사용자로부터 검색할 문자열 입력받기
search_string = input("검색할 문자열을 입력하세요: ")

#news.txt 파일에서 검색하여 포함된 모든 라인 번호 출력하기
found_line_numbers = []

# news.txt 파일 열기
with open('news.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()  # 파일의 모든 줄을 읽어 리스트로 반환
    
    # 각 줄에 대해 검색할 문자열이 포함되어 있는지 확인
    for line_num, line in enumerate(lines, 1):  # line_num은 줄 번호 (1부터 시작)
        if search_string in line:
            found_line_numbers.append(line_num)

#검색된 문자열이 포함된 모든 라인의 번호 출력
if found_line_numbers:
    print(f"검색된 문자열 '{search_string}'이(가) 포함된 라인 번호:")
    for line_num in found_line_numbers:
        print(line_num)
else:
    print(f"검색된 문자열 '{search_string}'이(가) 포함된 라인이 없습니다.")"""

#문제 14)
'''#사용자로부터 검색할 문자열 입력받기
search_string = input("검색할 문자열을 입력하세요: ")

#파일에서 검색하여 검색 결과를 리스트에 저장하기
found_lines = []

with open('news.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()  # 파일의 모든 줄을 읽어 리스트로 반환
    
    for line_num, line in enumerate(lines, 1):
        if search_string in line:
            found_lines.append(line.strip())  # 검색된 줄을 리스트에 추가

#검색 결과가 있는 경우 결과를 파일에 저장하기
if found_lines:
    output_file = input("저장할 파일 이름을 입력하세요: ")
    with open(output_file, 'w', encoding='utf-8') as output:
        for line in found_lines:
            output.write(line + '\n')
    
    print(f"검색된 결과가 '{output_file}' 파일에 저장되었습니다.")
else:
    print("검색 단어가 파일에 없습니다.")'''

#문제 15)
'''#data1.txt와 data2.txt 파일에서 데이터 읽어오기
data1 = []
data2 = []

with open('data1.txt', 'r') as file1:
    for line in file1:
        data1.append(float(line.strip()))  # 각 줄의 데이터를 실수형으로 변환하여 리스트에 추가

with open('data2.txt', 'r') as file2:
    for line in file2:
        data2.append(float(line.strip()))  # 각 줄의 데이터를 실수형으로 변환하여 리스트에 추가

#두 리스트를 합쳐 오름차순으로 정렬하기
merged_data = sorted(data1 + data2)

#정렬된 결과를 data3.txt 파일에 저장하기
with open('data3.txt', 'w') as file3:
    for num in merged_data:
        file3.write(f"{num}\n")

print("데이터가 정렬되어 data3.txt 파일에 저장되었습니다.")

'''

#문제 16)
'''import math
with open('shapes.txt', 'r',encoding='utf-8') as file:
    lines = file.readlines()
    
    i = 0
    while i < len(lines):
        shape_type = lines[i].strip()
        if shape_type == "사각형":
            x1, y1 = float(lines[i+1].strip()), float(lines[i+2].strip())
            x2, y2 = float(lines[i+3].strip()), float(lines[i+4].strip())
            width = abs(x1 - x2)
            height = abs(y1 - y2)
            area = width * height
            print(f"사각형의 면적: {area:.2f}")
            i += 5
        elif shape_type == "삼각형":
            x1, y1 = float(lines[i+1].strip()), float(lines[i+2].strip())
            x2, y2 = float(lines[i+3].strip()), float(lines[i+4].strip())
            x3, y3 = float(lines[i+5].strip()), float(lines[i+6].strip())
            a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
            c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print(f"삼각형의 면적: {area:.2f}")
            i += 7
        elif shape_type == "원":
            radius = float(lines[i+1].strip())
            area = math.pi * (radius ** 2)
            print(f"원의 면적: {area:.2f}")
            i += 2'''

#문제 17)
'''source_filename = input("복사할 파일의 이름을 입력하세요: ")
target_filename = input("복사된 파일의 이름을 입력하세요: ")
with open(source_filename, 'r', encoding='utf-8') as source_file:
    with open(target_filename, 'w', encoding='utf-8') as target_file:
        for line in source_file:
            target_file.write(line)'''

#문제 18)
'''def remove_comments(source_filename):
    with open(source_filename, 'r', encoding='utf-8') as source_file:
        lines = source_file.readlines()

    # 주석 제거
    clean_lines = []
    for line in lines:
        # 주석 기호(#)가 있는 위치를 찾아서 해당 위치 이전의 내용만 가져옴
        if '#' in line:
            index = line.index('#')
            clean_lines.append(line[:index] + '\n')
        else:
            clean_lines.append(line)

    # 새 파일에 저장
    new_filename = f"new_{source_filename}"
    with open(new_filename, 'w', encoding='utf-8') as target_file:
        target_file.writelines(clean_lines)

    print(f"{source_filename} 파일에서 주석을 제거하여 {new_filename} 파일을 생성하였습니다.")

source_filename = input("주석을 제거할 파이썬 코드 파일의 이름을 입력하세요: ")

remove_comments(source_filename)'''

#문제 19)
filename = input("파일 이름을 입력하세요: ")
with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()
    words = content.split()  # 공백을 기준으로 단어들을 분리하여 리스트로 만듦
    word_count = len(words)
    print(f"{filename} 파일에는 총 {word_count}개의 단어가 포함되어 있습니다.")