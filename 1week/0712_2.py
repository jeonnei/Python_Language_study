"""my_str = "Hello, World!"

print("String length:", len(my_str))
print("Indexing:", my_str[:5])
print("Replacement string:", my_str.replace("World", "Python"))
print("Is alphanumeric:", my_str.isalnum())
print("Is alphabetic:", my_str.isalpha())
print("Is digit:", my_str.isdigit())
print("Is numeric:", my_str.isnumeric())
print("Is lowercase:", my_str.islower())
print("Is uppercase:", my_str.isupper())
print("Uppercase:", my_str.upper())
print("Lowercase:", my_str.lower())
print("Swap case:", my_str.swapcase())
print("Count of 'l':", my_str.count('l'))
print("Count of 'l' from index 6 to 10:",my_str.count('l', 6, 10))"""

'''my_str = "Hello, World!"

fixed_width = 35

print("String length:".ljust(fixed_width), len(my_str))
print("Indexing:".ljust(fixed_width), my_str[:5])
print("Replacement string:".ljust(fixed_width), my_str.replace("World", "Python"))
print("Is alphanumeric:".ljust(fixed_width), my_str.isalnum())
print("Is alphabetic:".ljust(fixed_width), my_str.isalpha())
print("Is digit:".ljust(fixed_width), my_str.isdigit())
print("Is numeric:".ljust(fixed_width), my_str.isnumeric())
print("Is lowercase:".ljust(fixed_width), my_str.islower())
print("Is uppercase:".ljust(fixed_width), my_str.isupper())
print("Uppercase:".ljust(fixed_width), my_str.upper())
print("Lowercase:".ljust(fixed_width), my_str.lower())
print("Swap case:".ljust(fixed_width), my_str.swapcase())
print("Count of 'l':".ljust(fixed_width), my_str.count('l'))
print("Count of 'l' from index 6 to 10:".ljust(fixed_width), my_str.count('l', 6, 10))
'''
'''a = "Hello,World!,How,are,you,doing,today?"
print(a.replace(',',' '))'''

'''my_var1 = input("변수명을 입력하세요: ")
#.isalpha() 알파벳인지확인 True False반환 .isalnum() 알파벳 or 숫자인지 확인 True False반환
if my_var1 and (my_var1[0].isalpha() or my_var1[0] == '_') and all(c.isalnum() for c in my_var1[1:]):
    print("Variable name is valid")
else:
    print("Variable name is invalid")'''

"""my_password = input("문자열을 입력하시오(길이8이상 30이하) : ")

if 8 <= len(my_password) <= 30:  # 길이 확인
    if my_password.isalnum():  # 문자열이 영문과 숫자로만 구성되었는지 확인
        if any(c.isdigit() for c in my_password) and any(c.isalpha() for c in my_password):  # 영문과 숫자를 모두 포함했는지 확인
            if any(c.islower() for c in my_password) and any(c.isupper() for c in my_password):  # 대소문자를 모두 포함했는지 확인
                print("적합한 비밀번호")
            else:
                print("적합하지 않음. (대소문자 모두 포함되어야 함)")
        else:
            print("적합하지 않음. (영문과 숫자를 모두 포함해야 함)")
    else:
        print("적합하지 않음. (영문과 숫자로만 구성되어야 함)")
else:
    print("적합하지 않음. (길이가 8 이상 30 이하여야 함)")"""
"""
my_input = 'abcd'
answer = "ABCD"

if(my_input.lower() == answer.lower()):#두 문자열 모두 소문자로 변경
    print("Strings are equal")
else:
   print("Strings are not equal")
"""
"""my_str = "Heelo"
my_str = my_str[:2] + "l" + my_str[3:]

print(my_str)"""
"""my_str = "Helllo"
my_str = my_str.replace('l','',1)

print(my_str)
"""
'''import os
file_path = "hello.txt.py"

file_name,file_extension = os.path.splitext(file_path)#파일 이름과 확장자 분리

print("파일 이름:",file_name)
print("파일 확장자:",file_extension)'''
my_sentence = "Hello,World!,How,are,you,doing,today?"

print(my_sentence.replace(',',' '))



