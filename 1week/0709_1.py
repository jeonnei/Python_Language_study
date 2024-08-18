import math
#문제 1)
"""
컴퓨터는 전기적 신호를 기반으로 동작한다.
이러한 신호를 0과 1로 표현하는 것이 가장 효율적이고 신뢰성이 높기때문이다.
"""
#문제 2)
"""
문자열 자료형과 문자열 자료형 사이에는 뺄셈 연산이 지원되지 않기 때문이다.
하지만 덧셈연산은 지원하기 때문에 오류가 발생하지 않는다.
"""
#문제 3)
"""
파이썬에서 정수(int)의 메모리 공간 크기 제한이 없고
실수(float)의 메모리 공간 크기제한은 8바이트 제한이 있다.
"""
#문제 4)
print("그가 \"안녕하세요\"라고 말했다")

#문제 5)

#문제 6)
"""
-3444
"""
#문제 7)
print("She said, \"It's a beautiful day.\"")
print("He replied, \"Yes, it is!\"")

#문제 8)
uni = u"\u03a9"
print(chr(0x1F60A),uni)

#문제 9) 답:2

#문제 10)
print(round(124.578,2))

#문제 11)
print("디비딥 디비딥 딥디비딥\n디비디비딥 딥디비딥\n디비딥 디비딥 딥디비딥\n"*3)

#문제 12)
"""
(1) 10,15
(2) 8,15
"""
#문제 13)
a = int(input("네자릿수 정수 입력\n"))
a1 = int(a/1000)
a2 = int((a%1000)/100)
a3 = int((a%100)/10)
a4 = a%10
result = a4*1000+a3*100+a2*10+a1
print(result)

#문제 14)
x1,y1=1,4
x2,y2=3.5,2.4
result = math.sqrt((x2-x1)**2+(y2-y1)**2)
result = round(result)
print("거리:",result)

#문제 15)
day = 265
mon = 30
result1 = (265/30)   #달
result2 = 265%30        #일
print("%d달%d일입니다."%(result1,result2))

#문제 16)
num1=float(input("첫번쨰 실수를 입력하시오.\n"))
num2=float(input("두번쨰 실수를 입력하시오.\n"))

add = num1+num2
sub = num1-num2
mul = num1*num2
div = num1/num2

print(f"{num1}+{num2}={add}")
print(f"{num1}-{num2}={sub}")
print(f"{num1}*{num2}={mul}")
print(f"{num1}/{num2}={div}")

exp=input("연산식을 입력하시오: ")
result=eval(exp)
print(f"{exp} = {result}")

#문제 17)
"""
(1)input()함수는 사용자로 입력받으면 항상 문자열로 반환한다 
따라서, data는 문자열이므로 1을 더하려고하면 정수와 문자열 더하는 연산은 지원하지 않으므로
타입 에러가 발생한다.
(2)int()함수는 정수로 변환가능한 문자열만 변환가능하다.
'3.14'는 부동 소숫점 숫자를 나타내는 문자열이므로 int()함수로 변환 할 수 없다.
ValueError가 발생한다.
(3)문자열과 정수는 직접적으로 연걸할 수가 없다. TypeError발생
(4)'a=b=8=c=9'구문에서 '8=c'부분이 문법적으로 잘못되었다.
SyntaxError 발생.
"""
#문제 18)

value = int(input("십진수 입력 : "))

b = bin(value)
o = oct(value)
h = hex(value)

print(b,o,h)

#문제 19)
a = 0.1
b = 0.2
print(a+b)
"""
이 코드를 실행하면 0.300000000000004가 나오는데 그이유는
컴퓨터가 숫자를 비트로 표현하는데 실수의 경우 유리수+무리수 이기 때문에 정확한 표현이 어렵기 때문이다.
그래서 제한적인 비트를 사용하여 근삿값을 표현하기 때문에 0.3의 근삿값인 0.300000004가 나온다.

"""


#문제 20)
from tkinter import *

window = Tk()
window.title = ("GUI창 연습")
window.geometry("400x100")
window.resizable(width=FALSE,height=FALSE)
window.mainloop()