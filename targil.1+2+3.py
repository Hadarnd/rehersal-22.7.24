#start
#1)
x: float = float(input("please enter first mumber:"))
y: float = float(input("please enter second mumber:"))

print(3*(f"{x} , {y} , "))


#2)
x: int = int(input("please enter a mumber between 1 - 100:"))
y: int = int(input("please enter another mumber between 1 - 100:"))
sum: int = 0
avg: float = 0

sum = x + y
avg = sum / 2

print(f"the average is: {avg}")


#3)
a: float = float(input("please enter first number:"))
b: float = float(input("please enter first number:"))
c: float = float(input("please enter first number:"))

if a > b and a > c:
    print(f"the number {a} is the largest")
if b > a and b > c:
    print(f"the number {b} is the largest")
if c > a and c > b:
    print(f"the number {c} is the largest")

# ראיתי עוד אפשרויות עם אלאיף לולאת פור אבל זו נראית לי הכי פשוטה וקצרה בכתיבה שלה



#end