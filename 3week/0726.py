#문제 3,4)
"""import turtle as t

# 창 설정
screen = t.Screen()
screen.title("Turtle Graphics")

# 터틀 객체 생성
t.Turtle()

# 정사각형 그리기
for _ in range(4):
    t.forward(100)  # 100 픽셀 앞으로 이동
    t.right(60)     # 오른쪽으로 90도 회전

screen.exitonclick()"""
#문제 5)
"""import turtle as t

# 창 설정
screen = t.Screen()
screen.title("Turtle Graphics")

# 터틀 객체 생성
t.Turtle()

# 정사각형 그리기
for _ in range(6):
    t.forward(100)  # 100 픽셀 앞으로 이동
    t.right(60)     # 오른쪽으로 90도 회전

screen.exitonclick()"""
#문제 6)

"""import turtle

# 창 설정
screen = turtle.Screen()
screen.title("Turtle Graphics")

# 터틀 객체 생성
t = turtle.Turtle()

# 색상 설정
t.color("blue")
t.fillcolor("red")

# 색칠 시작
t.begin_fill()

# 반지름 100 픽셀의 원 그리기
t.circle(100)

# 색칠 종료
t.end_fill()

# 화면을 클릭하면 종료
screen.exitonclick()"""

#문제 7)
"""
import turtle

screen = turtle.Screen()
screen.title("Turtle Graphics")

t = turtle.Turtle()

# 부채꼴 그리기
t.circle(120, 90)  # 반지름 120, 원주 각도 90도 그리기
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)
screen.exitonclick()"""

#문제 8)
"""import turtle
turtle.speed(0) #숫자가 클수록 빠르게 그립니다. 0는 가장 빠른 속도입니다.
turtle.bgcolor("black") # 배경색
colors = ["red", "yellow", "blue", "green"]
for i in range(100):
    turtle.color(colors[i % 4]) # colors 인덱스를 만들어 색상을 순환시킵니다.
    turtle.forward(i * 4) # 현재 반복 횟수 i에 4를 곱한 만큼 앞으로 전진합니다.
#이로 인해 반복할 때마다 그리는 선의 길이가 점점 길어집니다.
    turtle.left(91)
turtle.done()"""

#문제 9)
import turtle

# 창 설정
screen = turtle.Screen()
screen.title("Turtle Graphics")

t = turtle.Turtle()
t.pendown()
t.shape('turtle')
# 앞으로 이동 함수
def move_forward():
    t.forward(10)
# 뒤로 이동 함수
def move_backward():
    t.backward(10)
# 오른쪽 회전 함수
def move_right():
    t.right(5)
# 왼쪽 회전 함수
def move_left():
    t.left(5)
def pen_up():
    t.penup()
def pen_down():
    t.pendown()

# 키보드 이벤트 처리 설정
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "Left")
screen.onkeypress(pen_up, "a")   
screen.onkeypress(pen_down, "s") 
screen.onkeypress(t.circle(50), "c") 

# 키 이벤트를 활성화
screen.listen()

# 화면을 클릭하면 종료
screen.exitonclick()


#문제 10)
"""import matplotlib.pyplot as plt

# 데이터
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 산포그래프 그리기
plt.scatter(x, y)

# 그래프 제목과 축 라벨 설정
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 그래프 표시
plt.show()"""
