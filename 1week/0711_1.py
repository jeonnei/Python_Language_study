#문제 1)

#문제 2)
"""print(2==2.0)
print(2.0<2.1)
print(2<2.1)
print("3.2"==3.2)"""

#문제 3)
"""ans = "에어컨을 켠다"
tem = 30
rh = 80
if(tem>=25):
    if(rh>=70):
        print(ans)"""

#문제 4)
"""CODE_A= int(input("정수입력:"))

if(CODE_A>=10):
    print("(10이상)")
elif(CODE_A>=5):
    print("(5이상~10미만)")
else: 
    print("(5미만)")"""

#문제 5)
"""score = 90
if score >= 90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
else:
    print("D")"""

#문제 6)
"""
if문이 평가되지 못한다.
divisor이 0 이면 (divisor !=0)에서 FALSE가 되고
num/divisor 에서 컴파일 오류가 난다.
"""
#문제 7)
'''if 'o' in 'python':
    print('o')
else:
    print('x')
if not 27 % 3:
    print('27은 3의 배수이다.')
else:
    print('27은 3의 배수가 아니다')'''

#문제 8)
"""date_input=input("년/월/일을 입력하시오.(예: 1999/6/6)")
date = date_input.split('/')
#print(len(date))
if len(date)==3:    #날짜 형식을 정확하게 입력했을때, 각부분 정수로 변환
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])

    if (1<= month <= 12) and 1 <=day<=31:
        print(f"입력한 날짜는 {year}년 {month}월 {day}일입니다.")
        if(month==2)and 1<day<=28:
            print("적절한 날짜입니다.")
        elif(month==2)and day>28:
            print("적절하지 않은 날짜입니다.")
        else:
            print("적절한 날짜입니다.")"""

#문제 9)
'''hour_money = 12000
hour = int(input("일주일 간 근로시간을 입력하시오 : "))

weekly_salary=hour_money*hour
if(hour>=40):
    weekly_salary *=1.5
print("주급은 %d원 입니다."%weekly_salary)'''

#문제 10)
'''while(1):
    weight = float(input("우편물의 무게를 입력하시오:"))

    if(weight>50):
        print("우체국에 문의하십시오")
    elif(weight>25):
        print("우편물 가격은 450원입니다.")
    elif(weight>5):
        print("우편물 가격은 430원입니다.")
    else:
        print("우편물 가격은 400원입니다.")'''

#문제 11)
'''while(1):
    ta = float(input("건구 온도를 입력하세요 : "))
    tw = float(input("습구 온도를 입력하세요 : "))
    Discomfortindex = 0.72*(ta+tw)+40.6 #불쾌지수

    if(Discomfortindex>=80):
        print("모든 사람이 불쾌감을 느낍니다.")
    elif(Discomfortindex>=75):
        print("반 정도의 사람이 불쾌감을 느낍니다.")
    elif(Discomfortindex>=68):
        print("불쾌감을 느끼기 시작합니다.")
    else:
        print("모든 사람이 쾌적함을 느낍니다.")'''

#문제 12)
'''while(1):
    a,b,c = map(float, input("a,b,c를 입력하세요.").split(','))#실수형으로 3개 한번에 입력받기

    result = b**2-4*a*c
    print("b^2-4ac의 결과값:%f"%result)

    if(result>0):
        print("해는 실수이고 2개의 다른 값이 존재함")
    elif(result==0):
        print("해는 실수이고 1개 값만 존재함.")
    else:
        print("해는 복소수이고 2개의 다른 값이 존재한다.")'''

#문제 13)
"""import math

#정수형으로 5개 한번에 입력받기
a,b,c,p1,p2 = map(int, input("a,b,c,p1,p2를 입력하세요.").split(','))

dis1 = a*p1+b*p2+c
dis2 = math.sqrt(a**2+b**2)
dis3 = dis1/dis2
distance = abs(dis3)
print(f"직선과 점사이의 거리는 {distance}입니다.")"""

#문제 14)
"""while(1):
    s1,s2=map(int,input("기울기 s1,s1값을 입력하세요(예시 2,1) : ").split(','))

    if(s1*s2==-1):
        print("두 직선은 직교합니다")
    elif(s1==s2):
        print("두 직선은 평행합니다.")
    else:
        print("두 직선은 평행,직교하지 않습니다.")"""

#문제 15)
'''vip,s,a,b=150000,110000,90000,70000 #좌석별 가격
while(1):
    user=input("구매 할 좌석의 종류를 선택하세요(vip,s,a,b) : ")
    if(user=="vip"):
        print("vip급 좌석의 가격은 %d원입니다."%vip)
    elif(user=='s'):
        print("s급 좌석의 가격은 %d원입니다."%s)
    elif(user=='a'):
        print("a급 좌석의 가격은 %d원입니다."%a)
    elif(user=='b'):
        print("b급 좌석의 가격은 %d원입니다."%b)
    else:
        print("잘못 입력했습니다.")
'''

#문제 16)
'''from random import *    #import random하면 random.함수이름 해야하지만
                        #from random imoprt *하면 함수 이름만 써도 사용가능해짐.
a=range(101)       #0~100까지 숫자 생성
print(sample(a,k=3))   #sample(변수,k=정수)3개의 수를 출력합니다.(중복x)'''


#문제 17)
'''while(1):
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
        print("%d는 소수가 아닙니다"%num)'''

#문제 18)
'''
h,w=map(int,input("당신의 키(cm)와 몸무게(kg)는?\n").split(','))
bmi=w/((h/100)**2)

if(bmi>=40):
    print(f"BMI: {bmi:.1f} 고도 비만.")
elif(bmi>=35):
    print(f"BMI: {bmi:.1f} 증등도 비만.")
elif(bmi>=30):
    print(f"BMI: {bmi:.1f} 비만.")
elif(bmi>=25):
    print(f"BMI: {bmi:.1f} 과체중.")
elif(bmi>=18.5):
    print(f"BMI: {bmi:.1f} 정상.")
else:
    print(f"BMI: {bmi:.1f} 저체중.")'''

#문제 19)
'''while(1):
    interest=input("[없음, 조금, 보통, 많음, 매우 많음]중 하나의 값을 입력하세요 : ")
    efforts=input("[상, 중, 하]중 하나의 값을 입력하세요 : ")

    if(interest=="보통") or (interest=="많음") or (interest=="매우 많음"):
        if(efforts=='상'):
            print("예비 파이썬 고수")
        elif(efforts=='중'):
            print("예비 파이썬 중수")
        else:
            print("노력 필요")
    else:
        print("파이썬에 대해 관심을 가져보세요.")'''
