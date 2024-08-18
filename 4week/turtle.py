import turtle as t

def draw_hangul(text, x, y, size=100):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(text, font=("Arial", size, "normal"))

# 화면 설정
t.setup(800, 600)
t.bgcolor("white")
t.title("파이썬 Turtle 모듈로 한글 그리기")

# 한글 그리기
draw_hangul("하송미", -200, 0, 50)

# 터틀 종료
t.hideturtle()
t.done()
