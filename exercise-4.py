#solution to exercise-4
num = raw_input("Enter a number : ")
num = int(num)

print("The divisors of " + str(num) + " are : " + str([div for div in range(1, num+1) if (num % div) == 0]))