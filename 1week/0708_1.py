#문제 1.답: O

#문제 2.답:2,7

#문제 3.답:4

#문제 4. 

print("전성현",end=" ")
print("1999년","06월","06일",sep="/")

#문제 5. 답:2

#문제 6. 답:2

#문제 7. 
print("안녕하세요. 같이 파이썬 실습해요.")
print("\t앞에 공간을 띄우세요.")
print("\t\t두번을 띄워보세요.")

#문제 8. 답:4

#문제 9. 답:1

#문제 10. 답:3

#문제 11.
name = "전성현"
f_string = f"\"안녕하세요, [{name}]님!\""
print(f_string)

#문제 12.
a = 5
b = 10
c = a+b
abc = f"{a}와 {b}의 합은 {c}입니다."
print(abc)

#문제 13. 답:1

#문제 14. 파이썬에서는 코드 블록을 구분하는데 필요한 {}대신 들여쓰기를 한다.
#if,for,while,edf와 같은 문장 뒤에 콜론(:)이 오며 이후의 라인부터 들여쓰기가 시작된다. 
#같은 블록 내에서는 들여쓰기 칸 수가 같아야한다.

#문제 15.
print("Hello","world!","This","is","Python",sep=' ',end='.')

#문제 16.

pen=[20,100]
note = [4,80]
eraser = [100,75]
print("{0:>10}".format("item"),"{0:>10}".format("count"),"{0:>10}".format("price"))
print("{0:>10}".format("pen"),"{0:>10}".format(pen[0]),"{0:>10}".format(pen[1]))
print("{0:>10}".format("note"),"{0:>10}".format(note[0]),"{0:>10}".format(note[1]))
print("{0:>10}".format("eraser"),"{0:>10}".format(eraser[0]),"{0:>10}".format(eraser[1]))
#문제 17.

a = 90
b= 95
c = 100
sum = a+b+c
avg = sum/3
print("국어",a,sep='\t',end='\n')
print("수학",b,sep='\t',end='\n')
print("과학",c,sep='\t',end='\n')
print("합계",sum,sep='\t',end='\n')
print("평균",avg,sep='\t',end='\n')

#문제 18. 답:3

#문제 19.
name = input("이름을 입력하세요\n")
age = int(input("나이를 입력하세요\n"))
num = int(input("숫자를 입력하세요\n"))

name_st = f"\"안녕하세요, [{name}]님! 당신은 [{age}]살입니다.\""
name_ri = f"\"[{num}]년 후에는 [{num+age}]살이 됩니다.\""
print(name_st)
print(name_ri)

#문제 20.
cap = 298,000,000,000,000
cprice = 50,000
PER = 15.79
print(type(cap))
print(type(cprice))
print(type(PER))

#문제 21.
#Print() 를 print()로 바꾸면 된다. 에러가 발생하는 이유는 print()라는 함수로 정해져있기 때문에 대소문자 구분을 해야한다.

#문제 22.

for i in range(1,12):
    if i==4:
        print("✳ ✳     ✳ ✳ ✳ ✳     ✳ ✳")
    elif i==5:
        print("✳ ✳ ✳    ✳ ✳ ✳    ✳ ✳ ✳")
    elif i==6:
        print("✳ ✳ ✳ ✳    ✳    ✳ ✳ ✳ ✳")
    elif (i==7 or i==8 or i==9):
        print("✳ ✳ ✳ ✳ ✳     ✳ ✳ ✳ ✳ ✳")
    else:
        print("✳ ✳ ✳ ✳ ✳ ✳ ✳ ✳ ✳ ✳ ✳ ✳")