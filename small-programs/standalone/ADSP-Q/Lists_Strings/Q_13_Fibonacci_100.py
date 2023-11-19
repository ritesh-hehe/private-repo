# Write a function that computes the list of the first 100 Fibonacci numbers.
# The first two Fibonacci numbers are 1 and 1.
# The n+1-st Fibonacci number can be computed by adding the n-th and the n-1-th Fibonacci number.
# The first few are therefore 1, 1, 1+1=2, 1+2=3, 2+3=5, 3+5=8.

# NOTE: Isn't the first fibonacci 0? Ah, apparently it may start from 0 or 1,1 or 1,2...pretty cool
# Also, fibonacci gets out of hand pretty quick...In Py I don't have to deal with memory or int64 kinda things
# I wonder how I would tackle that...

def compute_fibonacci(k=100) -> list:
    counter = 1
    fib_list = [1, 1]
    while counter <= k:
        fib_list.append(fib_list[counter-1] + fib_list[counter])
        counter += 1
    return fib_list


if __name__ == '__main__':
    print(compute_fibonacci())
