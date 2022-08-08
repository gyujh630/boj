#1620번: 나는야 포켓몬 마스터 이다솜
import sys

n, m = map(int, sys.stdin.readline().split())
n_dict1 = {}
n_dict2 = {}
for i in range(n):
    text = sys.stdin.readline().rstrip()
    n_dict1[text] = i+1     #이름 : 숫자 형태의 딕셔너리1
    n_dict2[i+1] = text     #숫자 : 이름 형태의 딕셔너리2

for i in range(m):
    check = sys.stdin.readline().rstrip()
    if check.isdigit():
        print(n_dict2[int(check)])
    else:
        print(n_dict1[check])



"""
import sys

n, m = map(int, sys.stdin.readline().split())

n_dict = {sys.stdin.readline().strip() : str(i+1) for i in range(n)}
m_list = []

for _ in range(m):
    m_list.append(sys.stdin.readline().rstrip())

for i in m_list:
    if i in n_dict.keys(): #key중에 있다면
        print(n_dict[i]) #value 출력
    if i in n_dict.values(): #value중에 있다면
        print(list(n_dict.keys())[int(i)-1]) #key를 출력
"""


