num1 = int(input("Number please... "))
num2 = int(input("Number please... "))
num3 = int(input("Number please... "))
num4 = int(input("Number please... "))

if (num1 >= num2) and (num1 >= num3) and (num1 >= num4):
    largest = num1
elif (num2 >= num1) and (num2 >= num3) and (num2 >= num4):
    largest = num2
elif (num3 >= num1) and (num3 >= num2) and (num3 >= num4):
    largest = num3
else:
    largest = num4

print("The largest number is" , largest)
