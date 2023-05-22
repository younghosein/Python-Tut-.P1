a = {'A':1, 'B':2, 'C':3}
print(a)

a['D'] = 4
print(a)

a['B'] = 5
print(a)

del a['A']
print(a)

print('C' in a)
print('C' not in a)

print(a.items())

for i, j in a.items():
    print(i, j)

d = dict((('A',20),('B',30),('C',12)))
print(d)

z = "Soos", "Uuun", "Noon", "Lool"
for l, k in enumerate(z):
    print(l, k)