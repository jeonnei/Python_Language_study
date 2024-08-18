#문제 4)
"""import glob

# (1) "bc.txt"로 끝나는 3글자 파일명 ex) abc.txt, qbc.txt
files_3char_bc_txt = glob.glob('???.bc.txt')
print(files_3char_bc_txt)

# (2) 확장자 ".txt"를 가진 모든 파일
files_txt = glob.glob('*.txt')
print(files_txt)

# (3) 모든 파일
all_files = glob.glob('*')
print(all_files)"""

#문제 5)
"""from datetime import datetime

# 오늘의 년도, 월, 일 출력
today = datetime.today()
print(f"오늘의 년도: {today.year}, 월: {today.month}, 일: {today.day}")

# 현재 일자를 형식에 맞추어 출력
formatted_date = today.strftime("%Y년 %m월 %d일 요일: %A")
print(formatted_date)

# 현재 시각을 형식에 맞추어 출력
current_time = today.strftime("%H시 %M분 %S초")
print(current_time)
"""

#문제 6)
"""import time

# 1970년 1월 1일 00:00:00 UTC 이후 현재까지 경과한 초
elapsed_seconds = time.time()

print(f"1970년 1월 1일 00:00:00 UTC 이후 현재까지 {elapsed_seconds}초가 경과했습니다.")"""

#문제 7)
"""import time_utils
import time

print("Current time:", time_utils.current_time())  # a

print("Sleeping for 2 seconds...")
start_time = time.time()

time_utils.sleep_for(2)  # b

print("Current time:", time_utils.current_time())  # c
print("Elapsed time after sleeping:", time_utils.time_elapsed(start_time), "seconds")"""

#문제 8)
"""import Triangle

t = Triangle.Triangle(0, 0, 0, 0, 0, 0)
t.getCoordsInfo()
area = t.calcArea()
print(f"삼각형의 면적은: {area}")

"""

#추가문제 1)
"""import os

# 폴더 경로 지정
folder_path = "C:\\\\Temp\\\\test"

# 폴더 내의 모든 파일과 디렉토리 목록 가져오기
items = os.listdir(folder_path)

print("폴더에 있는 모든 파일 목록:")
for item in items:
    # 각 항목의 전체 경로 생성
    item_path = os.path.join(folder_path, item)

    # 해당 항목이 파일인지 확인
    if os.path.isfile(item_path):
        print(item)
"""

#추가문제 2)
"""import divisors

number = 28
print(f"The divisors of {number} are: {divisors.getDivisorsList(number)}")

"""
#추가문제 3)
"""import os

# 현재 디렉토리의 파일 목록을 가져옵니다.
file_list = os.listdir()

# 확장자가 "txt"인 파일들을 필터링합니다.
txt_files = [file for file in file_list if file.endswith('.txt')]

# 확장자가 "txt"인 파일들의 이름을 출력합니다.
for txt_file in txt_files:
    print(txt_file)
"""

#추가문제 4)
"""import os

def calcFileSize(subdirectory):
    lst = os.listdir(subdirectory)
    size = 0
    for item in lst:
        item_path = os.path.join(subdirectory, item)
        if os.path.isfile(item_path):
            size += os.path.getsize(item_path)
    return size

def listDir(directory):
    fileLst = os.listdir(directory)
    for item in fileLst:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            folder_size = calcFileSize(item_path)
            print(f"Directory: {item}, Size: {folder_size} bytes")

listDir(".")
"""

#추가문제 5)
"""
import shutil

# 파일 복사 예제
source_file = 'ex1.txt'
destination_file = 'ex1_copy.txt'

# source_file에서 destination_file로 파일 복사
shutil.copyfile(source_file, destination_file)
print(f"{source_file}가 {destination_file}로 복사되었습니다.")
"""

#추가문제6)
from datetime import date, timedelta

# 오늘 날짜
today = date.today()
print(f"오늘 날짜: {today}")

# 크리스마스 날짜
christmas = date(today.year, 12, 25)
print(f"크리스마스 날짜: {christmas}")

# 오늘부터 크리스마스까지 남은 일수 계산
days_until_christmas = (christmas - today).days
print(f"오늘부터 크리스마스까지 남은 일수: {days_until_christmas}일")

# 오늘부터 100일 후의 날짜 계산
hundred_days_later = today + timedelta(days=100)
print(f"오늘부터 100일 이후의 날짜: {hundred_days_later}")

