
age = int(input("Inter Your Age: (By Years): "))

years = age
months = years * 12
days = months * 30
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
milli_second = seconds * 1000


print("=" * 70)
print("Your Age is:")
print(f"Your Years is: {years}")
print(f"Your Months is: {months}")
print(f"Your Days is: {days}")
print(f"Your Hours is: {hours}")
print(f"Your Minutes is: {minutes}")
print(f"Your Seconds is: {seconds}")
print(f"Your Milliseconds is: {milli_second}")
print("=" * 70)
