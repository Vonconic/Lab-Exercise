celsius = int(input("Enter tempearture in Celsius:"))
farenheit = (celsius * 9/5) + 32

print(f"Temperature in Fahrenheit is {farenheit}")
if celsius > 25:
    print("Go to the beach")
elif celsius > 15:
    print("Go hiking")
else:
    print("Stay inside")