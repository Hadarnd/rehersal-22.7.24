#start
#1)
num = 0
sum = 0

while True:
    num = int(input("please enter numbers:"))

    if not num == -99:
        sum += num
        continue
    else:
        break
print(f"Sum numbers are:{sum}")
print(f" {num} = None")

#2)

num = 0
neg_num = 0
zero_num = 0
numbers: list = []
small_num = 0
big_num = 0

for numbers in num:
    if num < small_num:
        small_num = num

    elif num > big_num:
        big_num = num

while True:
    num = int(input("please enter numbers:"))

    if not num < 0 or num == 0 or num == -99:
        break
    else:
        continue


print(f"smallest number is: {small_num}")
print(f"biggest number is: {big_num}")
print(f" {num} = None")


#4)
num = 0
num1 = 0
num2 = 0
num3 = 0
for i in range(2):
    num: float = float(input("enter 2 numbers:"))
    num3 = num1 + num2
print(f"{num3}")

#end