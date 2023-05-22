names1 = ['navid', 'bahram', 'hichkas', 'sorena', 'rez']
for i in names1:
    if i == 'hichkas':
        continue
    print(i, end=' . ')
print('\t')

names2 = ['ho3ein', 'pishro', 'zedbazi', 'tataloo', 'tk']
for j in names2:
    if j == 'zedbazi':
        break
    print(j, end=' . ')

char = ['a', 'b', 'c', 'd', 'c', 'd']
for l in char:
    print(l,end=' . ')
else:
    print('\n''DONE','\t')

for k in char:
    pass
for k in char:
    ...

n1, n2, op = 8, 2, '*'
match op:
    case '+':
        print(n1, ' + ', n2, ' = ', n1 + n2)
    case '-':
        print(n1, ' - ', n2, ' = ', n1 - n2)
    case '*':
        print(n1, ' * ', n2, ' = ', n1 * n2)
    case '/':
        print(n1, ' / ', n2, ' = ', n1 // n2)
