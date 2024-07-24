#11)

d: float = float(input("how old are you?"))
h: float = float(input("what is your height?"))

if h > 115 and 8 <= d <= 18:
    print("Welcome aboard! you allow to get on the Roller Coaster :)")
if h > 115 and d > 18:
    print("We're sorry we cannot allow you to get on the Roller Coaster due to your age")
elif h > 100 and d > 18:
    print("Welcome aboard! you allow to get on the Roller Coaster :)")
else:
    print("We're sorry we cannot allow you to get on the Roller Coaster. You're welcome to try next time:)")
