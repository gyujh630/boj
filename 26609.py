import sys
a, b = map(int, sys.stdin.readline().split())

i = 0
while i <= min(a,b):
    if a % (min(a,b)-i) == 0 and b % (min(a,b)-i) == 0:
        m = min(a,b) - i
        print(m)
        break
    i += 1

print(int(a*b/m)) #유클리드 호제법