#1764번: 듣보잡

import sys
n, m = map(int, sys.stdin.readline().split())
n_set = set()
m_set = set()
nm_list = []

for i in range(n+m):
    check = sys.stdin.readline().rstrip()
    if i < n:
        n_set.add(check)
    else:
        m_set.add(check)
    nm_list.append(check)

count = 0
print_list = []
for i in sorted(set(nm_list)):
    if i in n_set and i in m_set:
        count += 1
        print_list.append(i)

print(count)
print("\n".join(print_list))