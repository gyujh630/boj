def factorial(a):
    if a == 0:
        return 1
    result = 1
    for i in range(1, a+1):
        result *= i
    return result


n, k = map(int, input().split())
print(int(factorial(n) / (factorial(k) * factorial(n-k))))