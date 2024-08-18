#문제 4)
#(1)foo함수의 private선언
"""class MyClass:
    def __init__(self):
        self.__foo()

    def __foo(self):
        print("This is a private method")

# 객체 생성
my_object = MyClass()

# 객체를 통해 private 메소드 호출 시도 (실패)
my_object.__foo()"""

#(2)foo함수의 protected선언
"""class MyClass:
    def __init__(self):
        self._foo()

    def _foo(self):
        print("This is a protected method")

class SubClass(MyClass):
    def call_protected(self):
        self._foo()

# 객체 생성
my_object = MyClass()

# 객체를 통해 protected 메소드 호출 (성공)
my_object._foo()

# 서브 클래스 객체를 통해 protected 메소드 호출 (성공)
sub_object = SubClass()
sub_object.call_protected()
"""
#(3)foo함수의 public선언
"""class MyClass:
    def __init__(self):
        self.foo()

    def foo(self):
        print("This is a public method")

# 객체 생성
my_object = MyClass()

# 객체를 통해 public 메소드 호출 (성공)
my_object.foo()
"""
#문제 7)
"""class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def display_info(self):
        print(f"사각형의 좌측 상단 좌표: ({self.x}, {self.y})")
        print(f"사각형의 너비: {self.w}")
        print(f"사각형의 높이: {self.h}")

# 객체 생성
rect1 = Rectangle(10, 20, 30, 40)

# 정보 출력
rect1.display_info()
"""
#문제 8)
"""class Parent:
    def __init__(self):
        self.value = "부모 클래스의 값"

    def foo(self):
        print("부모 클래스의 foo() 메소드 호출")
        print(f"부모 클래스의 값: {self.value}")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_value = "자식 클래스의 값"

    def foo(self):
        print("자식 클래스의 foo() 메소드 호출")
        super().foo()
        print(f"자식 클래스의 값: {self.child_value}")

# 객체 생성
child_instance = Child()

# 자식 클래스의 foo() 메소드 호출
child_instance.foo()
"""
#추가문제 1)
"""class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def display_info(self):
        print(f"사각형의 좌측 상단 좌표: ({self.x}, {self.y})")
        print(f"사각형의 너비: {self.w}")
        print(f"사각형의 높이: {self.h}")

# 객체 생성
rect1 = Rectangle(10, 20, 30, 40)

# 정보 출력
rect1.display_info()"""
#추가문제 2)
"""class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Vehicle initialized: {self.brand} {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, horsepower):
        super().__init__(brand, model)  # 부모 클래스의 생성자 호출
        self.horsepower = horsepower
        print(f"Car initialized: {self.brand} {self.model} with {self.horsepower} HP")

# 객체 생성
my_car = Car("AAA", "BBB", 350)"""

#추가문제 3)
"""
import math
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def calcArea(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return width * height

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    def calcArea(self):
        return math.pi * self.r ** 2

shapeList = []

for i in range(3):
    s = input("도형 모양을 입력하세요 (1:사각형 0:원): ")
    if s == "1":
        x1 = int(input("왼쪽 상단의 x좌표를 입력: "))
        y1 = int(input("왼쪽 상단의 y좌표를 입력: "))
        x2 = int(input("오른쪽 하단의 x좌표를 입력: "))
        y2 = int(input("오른쪽 하단의 y좌표를 입력: "))
        shapeList.append(Rectangle(x1, y1, x2, y2))
    elif s == "0":
        x = int(input("중심의 x좌표를 입력: "))
        y = int(input("중심의 y좌표를 입력: "))
        r = int(input("반지름을 입력: "))
        shapeList.append(Circle(x, y, r))
    else:
        print("잘못된 입력입니다.")

for shape in shapeList:
    print(f"면적: {shape.calcArea()}")
"""

#추가문제 4)
"""import math

class Rectangle:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
    def calcArea(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return width * height
    def getCoordsInfo(self):
        self.x1 = int(input("왼쪽 상단의 x 좌표값을 정수로 입력하세요: "))
        self.y1 = int(input("왼쪽 상단의 y 좌표값을 정수로 입력하세요: "))
        self.x2 = int(input("오른쪽 하단의 x 좌표값을 정수로 입력하세요: "))
        self.y2 = int(input("오른쪽 하단의 y 좌표값을 정수로 입력하세요: "))

class Circle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.r = 0
    def calcArea(self):
        return math.pi * self.r ** 2
    def getCoordsInfo(self):
        self.x = int(input("중심의 x 좌표값을 정수로 입력하세요: "))
        self.y = int(input("중심의 y 좌표값을 정수로 입력하세요: "))
        self.r = int(input("반지름을 정수로 입력하세요: "))

shapeList = []

for i in range(3):
    s = input("도형 모양을 입력하세요 (1:사각형 0:원): ")
    if s == "1":
        rect = Rectangle()
        rect.getCoordsInfo()
        shapeList.append(rect)
    elif s == "0":
        circle = Circle()
        circle.getCoordsInfo()
        shapeList.append(circle)
    else:
        print("잘못된 입력입니다.")
        continue
for shape in shapeList:
    print(f"면적: {shape.calcArea()}")

"""
#추가문제 5)
"""class Point:
    #(1)
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #(2)
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
    #(3)
    def getX(self):
        return self.x

    def getY(self):
        return self.y
# 객체 생성
point = Point(2, 3)

# 초기 x, y 값 출력
print(f"Initial point: ({point.getX()}, {point.getY()})")

# x 값 변경
point.setX(5)
# y 값 변경
point.setY(7)

# 변경된 x, y 값 출력
print(f"Updated point: ({point.getX()}, {point.getY()})")
"""

#추가문제 6)
"""class Problem:
    def __init__(self, studentsNumDictionary):
        self.studentsNumDictionary = studentsNumDictionary

    def subproblem1(self):
        max_decrease = 0
        year = 0

        previous_year = None
        for k, v in sorted(self.studentsNumDictionary.items()):
            if previous_year:
                decrease = previous_year - v
                if decrease > max_decrease:
                    max_decrease = decrease
                    year = k
            previous_year = v

        print(f"(1) {year}년에 {max_decrease:.1f}명 감소한 것이 최근 가장 급격하게 줄어든 경우입니다.")

    def subproblem2(self):
        for k, v in sorted(self.studentsNumDictionary.items()):
            if v < 30:
                print(f"(2) 학생 수가 30명 미만으로 떨어진 첫 해는 {k}년입니다.")
                break

    def subproblem3(self):
        total_decrease = 0
        years_count = len(self.studentsNumDictionary) - 1

        previous_year = None
        for k, v in sorted(self.studentsNumDictionary.items()):
            if previous_year:
                total_decrease += previous_year - v
            previous_year = v

        avg_decrease = total_decrease / years_count
        print(f"(3) 2010년부터 2021년까지 평균적으로 감소한 학생 수는 {avg_decrease:.2f}명입니다.")

# 딕셔너리 데이터
d = {2010:33.7, 2011:33.1, 2012:32.5, 2013:31.9, 2014:30.9, 2015:30.0, 2016:29.3, 2017:28.2, 2018:26.2, 2019:24.5, 2020:23.4, 2021:23}

# 객체 생성 및 메소드 호출
p = Problem(d)
p.subproblem1()
p.subproblem2()
p.subproblem3()"""

#추가문제 7)
class Car:
    def __init__(self, company, year, color):
        self.company = company
        self.year = year
        self.color = color

    def __str__(self):
        return f"자동차 회사: {self.company}, 년식: {self.year}, 색상: {self.color}"

    def __eq__(self, other):
        return (self.company == other.company and
                self.year == other.year and
                self.color == other.color)

# 예시 코드
mycar = Car('ABC', 2020, '검정')
yourcar = Car('DEF', 2021, '백색')

print(mycar)
print(yourcar)
print(mycar == yourcar)

