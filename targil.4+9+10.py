#start
#4)
mins: int = int(input("please enter how long the movie is in minutes:"))
hour: float = mins // 60
mins2: int = mins - 60
print(f"{hour} hour and {mins2} minutes")

#5)dont know
#6)dont know
#7)
#x: int = int(input("please enter a number bettween 10 - 99:"))

#9)
x: int = int(input("please enter a number:"))
if x % 2 == 0:
    print(f"{x} is zugi")
else:
    print(f"{x} is E- zugi")

#10)
sal: float = float(input("please enter your salary:"))

if 0 <= sal <= 6000:
    print("you need to pay 0% tax")
if 6000 <= sal <= 12000:
    print("you need to pay 10% tax")
if 12001 <= sal <= 18000:
    print("you need to pay 20% tax")
if 18001 <= sal <= 25000:
    print("you need to pay 30% tax")
if 25001 <= sal <= 35000:
    print("you need to pay 40% tax")
if 35001 <= sal <= 50000:
    print("you need to pay 45% tax")
elif sal >= 50001:
    print("you need to pay 51% tax")

#end