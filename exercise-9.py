# solution to exercise-4
num = raw_input("Enter a number : ")
num = int(num)
num_dev = []

num_dev = [div for div in range(1, num + 1) if (num % div) == 0]

if len(num_dev) > 2:
    print("The number " + str(num) + " is not a prime number. It has " + str(len(num_dev)) +
          " divisors which are : " + str(num_dev))
else:
    print("The number " + str(num) + " is a prime number")