L = ['Tupac', 'Eminem', 'IceCube', 'Russ', 'NF']
for i in L:
    print(i, len(i))

S = "Oldschool is real hiphop"
for j in S:
    print(j,end='-')
print('\t')

N = "1999 2000"
for l in N:
    print(l,end='_')
print('\t')

print(range(5))
for k in range(5):
    print(k,end=' , ')
print('\t')

for m in range(1,21):
    print(m, end=' , ')
print('\t')

for z in range(0,30,3):
    print(z, end=' . ')
print('\t')

print(list(range(10)))
print(tuple(range(10)))

a = ['Messi', 'Ronaldo', 'Neymar', 'Carlos']
for f in range(len(a)):
    print(f, a[f])

print(sum(range(5)))