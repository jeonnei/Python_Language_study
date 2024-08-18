#문제 1)
'''a = "문자열의 길이를 확인해요..."
result=a.count('.')
print(f"마침표의 길이 : {result}")'''

#문제 2)
'''a = "우리나라"
print('나' in a)'''

#문제 3)    #문자열.rindex(문자열,시작인덱스,끝인덱스)
'''a = "What a day!".rindex("a")   #검색하는 문자열의 마지막 위치를 반환
print(a)
a = "What a day!".rindex("a",0,5)
print(a)'''

#문제 4)
'''s="Hello World"
print(s[0:2])
print(s[:-1])
print(s[:])'''

#문제 5)    #문자열.strip(문자열) 양쪽 끝의 문자열의 공백제거가능 
'''a="가 helloh 가나".strip("가 h 나") #공백문자가 아닌 다른문자도 제거가능
print(a)'''

#문제 8)
'''input_string = input("세 개 이상의 단어로 구성된 문자열을 입력하세요 : ")
result = input_string.split(' ')
print(result[1])'''

#문제 9)
'''a = "Hello world".rindex('o')
print(a)'''

#문제 10)

'''a="123456789"

first=""
second=""
for i in a:
    if(int(i)%2==1):
        first = first + i
    else:
        second = second + i
print(first)
print(second)'''

#문제 11)
'''
string = input("세 개의 16진수로 구성된 문자열을 입력하세요 : ")

result = int(string,16)
print(result)'''

#문제 12)
'''
string = input(".jpg로 끝나는 파일 이름을 입력하세요 : ")
string = string.replace("jpg","png")
print(string)'''

#문제 14)
'''while(1):
    name = input("문자열을 입력하세요 : ")
    reverse_name=""

    for i in name:
        reverse_name = i+reverse_name
    if(reverse_name==name):
        print("팰린드롬 입니다.")
    else:
        print("팰린드롬이 아닙니다.")'''

#문제 16)
"""while(1):
    string1,string2 = map(str,input("두개의 문자열을 입력하세요(예시:listen,slient) : ").split(','))

    string1_sorted = sorted(string1)
    string2_sorted = sorted(string2)

    if(string1_sorted == string2_sorted):
        print(f"\"{string1}\"과\"{string2}\"는 아나그램입니다.")
    else:
        print(f"\"{string1}\"과\"{string2}\"는 아나그램이 아닙니다.")"""

#문제 17)
'''while(1):
    user = input("섭씨>화씨, 화씨>섭씨 변환 종류를 고르세요 : ")
    if(user=="섭씨>화씨"):
        tem = int(input("섭씨 온도를 입력하세요 : "))
        result = tem*(9/5)+32
        print(f"섭씨온도 {tem}도를 화씨온도로 변환하면 {result}도 입니다.")
    elif(user=="화씨>섭씨"):
        tem = int(input("화씨 온도를 입력하세요 : "))
        result = (tem-32)*(5/9)
        print(f"화씨온도 {tem}도를 섭씨온도로 변환하면 {result}도 입니다.")
    else:
        print("잘못 입력하셨습니다.")'''

#문제 18)
'''while(1):
    string1,string2 = map(str,input("두개의 문자열을 입력하세요(예시:abc,bca) : ").split(','))
    string1_sorted = sorted(string1)
    string2_sorted = sorted(string2)

    if(string1_sorted == string2_sorted):
        print(f"\"{string1}\"과\"{string2}\"는 순열 관계입니다.")
    else:
        print(f"\"{string1}\"과\"{string2}\"는 순열 관계가 아닙니다.")'''

#문제 19)

'''string = input("16진수 색상코드를 입력하세요(예시:FFA501) : ")
R = string[0:2]
G = string[2:4]
B = string[4:6]

R2 = int(R,16)
G2 = int(G,16)
B2 = int(B,16)

print(f"16진수 색상코드 {string} -> ({R2},{G2},{B2})입니다.")'''

#문제 20)
'''while(1):
    p1,p2 = map(str,input("p1,p2에 입력할 가위,바위,보를 하나씩 입력하세요(예:가위,바위):").split(','))
    print(f"p1은 {p1}, p2는 {p2}입니다")

    if p1==p2:
        print("비겼습니다")
    elif(p1=="가위" and p2=="보") or (p1=="보" and p2=="바위") or (p1=="바위" and p2=="가위"):
        print("p1이 이겼습니다.")
    else:
        print("p2가 이겼습니다.")'''

#문제 13)
p1,p2 = map(str,input("문자열 두개를 입력하세요.(예:python,thon):").split(','))
if(p2 in p1)==True:
    print(p1.index(p2))
else:
    print("두번째 문자열이 첫번재 문자열에 포함되지 않음.")