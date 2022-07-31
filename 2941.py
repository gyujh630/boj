#크로아티아 알파벳

s = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(len(croatia)):
    if s.count(croatia[i]) > 0:
        s = s.replace(croatia[i], '1')
print(len(s))