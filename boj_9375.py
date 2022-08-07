import sys

def test(n):
    if n == 0:                   #옷 개수가 0인 경우엔 0을 리턴하고 종료
        return 0
    dict = {}
    count = 1                    #곱연산을 해야하므로 0이 아닌 1로 설정
    for i in range(n):
        item, category = sys.stdin.readline().rstrip().split()
        if category not in dict: #dictionary에 카테고리와 그 개수를 추가하는 부분
            dict[category] = 1
        else: dict[category] += 1

    if len(dict) > 1:            #카테고리가 2개 이상일 때(여러 종류의 옷)
        for i in list(dict.values()):
            count *= (i + 1)     #i개 중의 하나를 고르는 경우의 수(iC1) = i ... + 하나도 고르지 않는 경우의 수 = 1
        return count - 1         #모든 옷들을 하나도 고르지 않는 경우의 수는 문제 조건 위배이므로 뺀다.
    else:                        #카테고리가 1개일 때(옷이 한종류)
        return list(dict.values())[0]

t = int(sys.stdin.readline())
for i in range(t):
    print(test(int(sys.stdin.readline().rstrip())))