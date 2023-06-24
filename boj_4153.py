l = []

while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        l.append([a,b,c])

for i in range(len(l)):
    if l[i][0]**2 + l[i][1]**2 == l[i][2]**2 or l[i][0]**2 + l[i][2]**2 == l[i][1]**2 or l[i][1]**2 + l[i][2]**2 == l[i][0]**2:
        print('right')
    else: print('wrong')