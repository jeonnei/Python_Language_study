'''if 1 = 2:
    print("Hello")'''
'''num = 0

if 5 / num > 0:
    print("Hello")
else:
    print("Bye")
'''

'''num = 0

if num > 0 and 5 / num:
    print("Hello")
else:
    print("Bye")'''

'''num = 13

if num > 10:
    if num % 5 == 3:
        if num // 4 == 3:
            print("Hello")'''

'''num = int(input("정수입력 : "))
if(num%2==0):
    print("짝수")
else:
    print("홀수")'''
'''
numbers = list(map(int, input("4개의 정수를 입력하세요: ").split(',')))

numbers.sort()

print("큰 순서대로 출력한 결과 : ",(numbers))'''


'''year = int(input("연도를 입력해주세요 : "))
month = int(input("월을 입력해주세요 : "))

if(year>0) and 0<month<=12:
    print("True")
else:
    print("False")'''

'''num = int(input("4자리 정수를 입력하시오 : "))

if num < 1000  or num > 9999:
    print("잘못 입력하셨습니다. 4자리 연도를 입력해주세요.")

else:
    # TODO: 4자리 정수의 첫 두자리와 마지막 두자리를 나누어 print
    print("첫 두자리 : ", num//100)
    print("마지막 두자리 : ", num%100)'''

date_input=input("년/월/일을 입력하시오.(예: 2024/7/11)")
date = date_input.split('/')

if len(date)==3:    #날짜 형식을 정확하게 입력했을때, 각부분 정수로 변환
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])

y1=year%100
y2=year//100
M=month
D=day

week_day = int((y1 + (y1/4) - (2*y2) + (y2/4) + (13*(M+1)/5) + D)%7)

if(week_day==1):
    print(f"{year}년{month}월{day}일의 요일은 일요일입니다.")
elif(week_day==2):
    print(f"{year}년{month}월{day}일의 요일은 월요일입니다.")
elif(week_day==3):
    print(f"{year}년{month}월{day}일의 요일은 화요일입니다.")
elif(week_day==4):
    print(f"{year}년{month}월{day}일의 요일은 수요일입니다.")
elif(week_day==5):
    print(f"{year}년{month}월{day}일의 요일은 목요일입니다.")
elif(week_day==6):
    print(f"{year}년{month}월{day}일의 요일은 금요일입니다.")
else:
    print(f"{year}년{month}월{day}일의 요일은 토요일입니다.")