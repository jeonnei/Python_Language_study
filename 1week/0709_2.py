import math
"""
#문제.1

a = float(input("실수를 입력하세요:"))
a = a*10
b = int(a)
c = a - b

if(c>=0.5):
    c=1
else:
    c=0

b=float(b+c)/10
print("반올림 결과:",b)

#문제.2

round_get = float(input("실수를 입력하세요:"))
round_get = round(round_get,1)
print("반올림 결과:",round_get)


#문제 3.

x = 1
y = 2
resultx = (math.sin(math.radians(30))*15)+x
resulty = (math.cos(math.radians(30))*15)+y

resultx = round(resultx,1)
resulty = round(resulty,1)
print("x,y좌표는 : (",resultx,resulty,")")

#문제 4.
x1,y1=1,2
x2,y2=4,6
result = math.sqrt((x2-x1)**2+(y2-y1)**2)
result = round(result,2)
print("거리:",result)
"""
"""
#문제 5.
def sum_numbers_in_variables(*args):
    total_sum=0
    for value in args:#isinstance(자료형 확인하는 함수)
        if isinstance(value,str) and value.isdigit():#value가 str형이고 모두 숫자로 이루어졌는지 확인
            total_sum += int(value)
        else:
            print(f"error={value}")

    return total_sum

var1 = "123"
var2 = "abc"
var3 = "456"
var4 = 789

result = sum_numbers_in_variables(var1,var2,var3,var4)
print(result)
"""
#문제 6)
"""
함수안의 error값이 var4가 뜬걸로 보면 var4값이 포함되지 않았다.
var4가 str형이 아닌 int형이기 때문이다.
"""
"""
#문제 7)
import calendar
year = int(input("년도를 입력하세요 : "))
month = int(input("달을 입력하세요 : "))
calendar.prmonth(year,month)
"""
"""
#문제 8)
hours = input("시간을 입력하세요(예:2시간30분->2 30):")
split_hours = hours.split()
#print(type(split_hours[0]))
min =int(split_hours[0])*60+int(split_hours[1]) #사칙연산을 위한 int형으로 변환
print(f"총 {min}분입니다.")
"""
"""
#문제 9)
def sum_numbers_in_variables(input):
    total_sum=0
    for value in input:
        if value.isdigit(): #문자가 숫자인지 확인
            total_sum += int(value)
        else:
            print(f"error={value}")

    return total_sum

var = input("문자열을 입력하세요 : ")
result = sum_numbers_in_variables(var)
print(f"입력한 문자열의 모든 숫자의 합:{result}")
"""
#문제 10)
total_sum=0
for i in range(1,101):
    if(i%3==0):
        total_sum=total_sum+i
    elif(i%5==0):
        total_sum=total_sum+i
print(f"1부터100까지 3또는5의배수 합의 결과는 : {total_sum}")
