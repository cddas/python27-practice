input_number = raw_input("Enter any number : ")
input_number = int(input_number)

print("You entered " + str(input_number))
if (input_number % 2) == 0:
    if (input_number % 4) == 0:
        print("The entered number is a multiple 4")
    else:
        print("The entered number is an even number but not divisible by 4")
else:
    print("The entered number is an odd number")

num, check = raw_input("Enter two numbers : ").split(" ")
num = int(num)
check = int(check)

if (num % check) == 0:
    print(str(check) + " divides " + str(num) + " evenly")
else:
    print(str(num) + " is not divisible by " + str(check) )