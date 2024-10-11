N = 7
a = [[0]*N for _ in range(N)]

x = 1
y = 3
d1 = 2
d2 = 2

for i in range(N):
    for j in range(N):
        if 0 <= i < x + d1 and 0 <= j <= y:
            a[i][j] = 1
        elif 0 <= i <= x + d2 and y < j < N:
            a[i][j] = 2
        elif x + d1 <= i < N and 0 <= j < y-d1+d2:
            a[i][j] = 3
        elif x + d2 < i < N and y-d1+d2 <= j < N:
            a[i][j] = 4

for b in a:
    print(b)