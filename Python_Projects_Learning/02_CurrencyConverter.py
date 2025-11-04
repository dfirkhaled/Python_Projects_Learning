y = input("You Want to convert EGP to USD?! Type (True or False): ")

if y == "True":
    x = float(input("Enter your amount in EGP: "))
    print("In USD:", x / 50)
else:
    z = float(input("Enter your amount in USD: "))
    print("In EGP:", z * 50)
