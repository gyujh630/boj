#피보나치 수 5
#재귀함수

import sys

def fibonacci(n):
   if n == 0:
       return 0
   elif n == 1 or n == 2:
       return 1
   else:
       return fibonacci(n-1) + fibonacci(n-2)

n = int(sys.stdin.readline())
print(fibonacci(n))

