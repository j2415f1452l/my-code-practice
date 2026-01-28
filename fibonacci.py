def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print("斐波那契数列前10项：")
for i in range(10):
    print(fib(i), end=" ")