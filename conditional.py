num=float(input("Enter number: "))

result="Odd" if num%2 ==0 else "Even"


print(f"This number : {num} is {result}")


username=input("Enter username?: ")

if len(username)>=10:
    print("Your username can't be more than 10 characters")
elif not username.find(" ") ==-1:
    print("Your username can't contain space")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome back {username}")


credit_card="1234-5678-9076-4321"

first=credit_card[:4]
last=credit_card[-4:]

print(f"{first}-XXXX-XXXX-{last}")