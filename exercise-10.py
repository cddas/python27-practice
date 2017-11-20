def fib_count(count_fib):
    global a,b
    global val
    while val in range(count_fib-1):
        a, b = b, a + b
        val += 1
        list_fib.append(b)

a, b = 0, 1
list_fib = [a, b]
val = 1
count_fib = raw_input("How many Fibonacci numbers you want to generate ? ")
count_fib = int(count_fib)

fib_count(count_fib)

print(list_fib)