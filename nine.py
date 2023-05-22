t1 = ('tupac', 'eminem', 'drake', 'icecube')
print(t1)
print(t1[1])

#t[1]='NF' -> not avl

t2 =('nigga', 'gangsta', (1, 2, 3), ['A', 'B', ('jay-z', 'russ')])
print(t2,type(t2))

l = []
n = ()
m = (1)
w = (1,)
print(type(l), '---', type(n), '---', type(m), '---', type(w))

a = {'A', 'B', 'C', 'D', 'A', 'b', 1, 2}
print(a)
if 2 in a:
    print('Yes')
if 'HAAAAA' not in a:
    print(':((((')

let = set('topgi')
print(let)

a1 = set("abcdasdf")
print(a1)
a2 = set("feghasdf")
print(a2)
print(a1-a2)
print(a1|a2) #a U b
print(a1&a2) #in a, in b, in both area
print(a1^a2) #in a, in b, not in both area