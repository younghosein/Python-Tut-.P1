l = [2002, 80, 28, 77, 80]
print(l)

l.append(85) #add at end
print(l)

l.extend([10, 992, 1]) #add at end(Obj)
print(l)

l.insert(2,85)
print(l)

l.remove(80)
print(l)

l.pop()
print(l)

x = l.pop(2)
print(x)
print(l)

z1 = l.index(85)
print(z1)
z2 = l.index(85,2,5)
print(z2)

print(l.count(85))

l.sort()
print(l)

l.reverse()
print(l)

del l[1:4]
print(l)

l.clear()
print(l)
