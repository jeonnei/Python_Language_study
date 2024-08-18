#1-1
'''x=int(input("0~9까지 숫자를 입력하세요:"))
for i in range(10):
    print(f"{x}"*10,end='\n')'''
#1-2
"""while(1):
    x=int(input("0~9까지 숫자를 입력하시오 : "))
    if x>=0 and x<=9:
        for i in range(x):
            print(' '*(x-1-i),end='')
            print('5'*((2*i)+1))
    else:
        print("다시 입력하세요")"""
#3-21)
'''input_string = input("문자열을 입력 >> ")
len_string = len(input_string)
input_index = int(input("참조하고 싶은 문자의 위치 입력(0~%d)"%len_string))
print(f"문자열 : {input_string}, 길이:{len_string}")
print(f"{int(input_index)+1}번째 문자 : {input_string[input_index]}")'''

#5-30)
'''while(1):
    string1,string2 = map(str,input("두개의 문자열을 입력하세요(예시:abc,bca) : ").split(','))
    string1_sorted = sorted(string1)
    string2_sorted = sorted(string2)

    if(string1_sorted == string2_sorted):
        print(f"\"{string1}\"과\"{string2}\"는 순열 관계입니다.")
    else:
        print(f"\"{string1}\"과\"{string2}\"는 순열 관계가 아닙니다.")'''

#4-20)
# 현재 알람 시간을 입력받습니다.
hour, minute = map(int, input("알람 시간을 입력하세요 (시, 분): ").split(','))

# 분에서 45분을 뺍니다.
minute -= 45

# 분이 0보다 작으면 시간을 조정합니다.
if minute < 0:
    minute += 60
    hour -= 1

# 시간이 0보다 작으면 23으로 변경합니다.
if hour < 0:
    hour += 24

print(f"새로운 알람 시간: {hour}시 {minute}분")
