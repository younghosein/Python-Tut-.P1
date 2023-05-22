def show1():
    print("HELLOOOO...")
show1()
show1()

def show2(name):
    print("HELLOOOO ",name,"...")
show2('developer')
show2('programmer')

def show3(name,age):
    print("HELLOOOO ",name, '->', age)
show3('developer',21)
show3('programmer',29)

def show4(name):
    return 'hello '+ name
print(show4('hosein'))

def show5(name='user'):
    print("HELLOOOO ",name)
show5()
show5('student')

def f(a, L=[]):
    L.append(a)
    return L
for j in  range(5):
    print(f(j))