import sys
from collections import Counter

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))

#산술평균
print(round(sum(a)/n))

#중앙값
print(sorted(a)[len(a)//2])

#최빈값
count = Counter(a)
order = count.most_common()  #딕셔너리 형태로 수와 빈도수가 저장된 배열
max_frequency = order[0][1]  #최대 빈도수

fq = []                      #최대 빈도수를 가진 수들을 저장하는 리스트
for i in order:
    if i[1] == max_frequency:
        fq.append(i[0])

if len(fq) == 1:
    print(fq[0])
else:
    print(sorted(fq)[1])

#범위
print(max(a)-min(a))