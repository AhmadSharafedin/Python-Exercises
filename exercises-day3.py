#ex1
a = [1, 2, 3, 4, 5]
for item in a:
    print(item)

#ex2
print(sum(a))

#ex3
print(max(a))

#ex4
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
a = list(set(a))
print(a)

#ex5
a = [1, 2, 3, 4, 5]
b = []
if len(a) < 1:
    print('list is empty')
else:
    print('not empty')
if len(b) > 0:
    print('list is empty')
else:
    print('not empty')

if not a:
    print('list is empty')
else:
    print('list not empty')

#ex6
a = 'a string', 1, True, [1, 2]
for item in a:
    print(item)

#ex7
num_set = set([0, 1, 2, 3, 4, 5])
for item in num_set:
    print(item)

#ex8
a = {5, 9, 4, 1}
b = {5, 4, 3}
print(a & b)

#ex9
setx = set(['green', 'blue'])
sety = set(['blue', 'yellow'])
seta = setx | sety
print(seta)
#answer={'blue', 'green', 'yellow'}


#ex10
seta = set([5, 10, 3, 15, 2, 20])
print(len(seta))
#anser = 6

#ex11
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)
#answer= {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#ex12
a = "Hello, World!"
print(a[1])
print(a[2:5])
print(a[-5:-2])
print(len(a))
print(a.lower())
print(a.replace('H', 'J'))

#answer = 
#e
#llo
#orl
#13
#hello, world!
#Jello, World!
