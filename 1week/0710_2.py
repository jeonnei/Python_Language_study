#문제 1)
"""z11,z12 = 4,3
z21,z22 = 2,5
print(f"({z11}+{z12}i)+({z21}-{z22}i)=({z11+z21}-{z22-z12}i)")"""

#문제 2)
"""name = "David"
age = 30

print(f"My name is {name} and I am {age} years old.")"""

#문제 3)
"""tem = int(input("6자리가 넘는 정수를 입력하시오 : "))
result = tem/1000
print(f"{tem}을(를) 1000으로 나눈 결과는 {result:.2f}입니다")"""

#문제 4)
"""
x=4 #상층부 4층
for i in range(x+1):
    for k in range(1+4*(i-1)):
        print("*",end='')
    print("")
x=3 #하층부 3층
for i in range(1,x+1):
    for k in range(4*(x+1-i)-3):
        print("*",end='')
    print("")
"""
#문제 5)
"""pri = int(input("원금을 입력하세요 : "))    #원금
year_rest = float(input("연 이자율(%)를 입력하세요 : "))    #연 이자율
year = int(input("기간(년수)를 입력하세요 : "))  #기간
mon_rest = (year_rest/100)/12   #월 이자율
amount = pri*((1+mon_rest)**(year*12))  #복리계산 공식
print(f"복리를 계산해보면 {amount:.0f}원 입니다")"""

#문제 6)
"""bet = [30,50,20,80,10]  #배터리셀의 잔여용량
result = 0
for i in bet:
    if(result==0):
        result=i           
    if(result>i):       #배열에서 가장 작은수 찾기
        result = i
print(f"AI-Robo의 5개의 배터리셀의 잔여 용량중 가장 적은 배터리 용량은 {result}% 입니다")"""     

#문제 4)
'''x=4 #상층부 4층
y=x-1
for i in range(x):
    print(' '*(2*(x-i-1)),end='')
    print('*'*((4*i)+1))
for i in range(y):
    print(' '*(2*(i+1)),end='')
    print('*'*(4*(y-i-1)+1))'''

#문제 4)
x=4 #상층부 4층
y=x-1
for i in range(x):
    print(' '*(x-1-i),end='')
    print('*'*((2*i)+1))
for i in range(y):
    print(' '*(i+1),end='')
    print('*'*(2*(y-i)-1))