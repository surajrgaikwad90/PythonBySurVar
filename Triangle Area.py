#Calculate the are aof triangle


# num1 = float(input("Enter Height"))
# num2 = float(input("Enter base"))
# area = num1 * num2 * 0.5
# print(area)


#Multiple inputs from user

height_base = input("ENter height & base: ").split()
numbers = [float(num) for num in height_base]
print("Height & base are: ", numbers)
area = (1/2)*numbers
print("area = ", area)
