def fibonacci(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(n):
        c = a + b
        print(c)
        a, b = b, c

fibonacci(10)

#RECURSIVE
def fibonacci_recur(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_recur(n-1)+fibonacci_recur(n-2))

terms = 10
if terms <= 0:
    print("Enter a positive integer")
else:
    print("Fibonacci Series using recursive function call")
    for i in range(terms):
        print(fibonacci_recur(i))