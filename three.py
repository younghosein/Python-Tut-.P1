L = []
print(L)
print(type(L))
L = ['a', 'b', 'c', 1, 2, 3]
print(L)

names = ['amo', 'daei', 'ame', 'khale','dady', 'momy']
print(names)
print(names[0])
print(names[-1])
print(names[3:])

print(L + names)

names[1] = 'pesare baba bozorg'
print(names)
names[4:] = 'DAD', 'MOM'
print(names)

names.append('Lana')
print(names)

names[2:4] = []
print(names)

print(len(names))