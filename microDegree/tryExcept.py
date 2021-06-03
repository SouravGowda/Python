income = 0

try:
    income = int(input("please enter the input: "))

except Exception:

    print("Enter the proper Input")

finally:
    print("should run always")
     
print(income)