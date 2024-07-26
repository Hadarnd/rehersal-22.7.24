# # loop-1)
top: int = int(input("enter a number:"))

for i in range(1,top + 1):
     print(i , end=",")


#loop-2)
x: int = int(input("enter first number:"))
y: int = int(input("enter second number:"))

if x > y:
     for j in range(y, x+1):
         print(j, end=",")
else:
     for j in range(x, y+1):
         print(j, end=",")

#loop-3)
n: int = int(input("enter a number:"))

for h in range(1 , n+1 ,2):
    print(h, end=",")

# #loop-4)
max: int = int(input("enter a number:"))
den: int = int(input("enter a number:"))

for h in range(1 , max+1):
    if max % den == 0:
         print(h, end=",")
else:
     print(f"{max} un divided by {den}")
