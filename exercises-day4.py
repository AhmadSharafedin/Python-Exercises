#ex1
o=lambda x =1,y=2,z=3:x+y+z 
print(o()) #answer = 6 
print(o(10)) #answer = 15
print(o(10,20)) #answer = 33

#ex2


def multi(*num):
    m = 1 
    for n in num:
        m = m * n
    print("multi:",m)

multi(2,3,4)
multi(2,3,4,5)

#ex3
print((lambda a,b: a* b)(5,6))

#ex4
filtered = list(filter(lambda x: x < 0 , range (-5,5)))
print(filtered)

#ex5
x = lambda a, b, c : a + b + c 
print(x(5, 6, 2))
#answer = 13

#ex6
x=("Joey", "Monica", "Ross")
y=("Chandler", "Pheobe")
z=("David", "Rachel", "Courtney") 
result = list(zip(x, y, z)) 
print(result)

#ex7
coin=('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC') 
d = dict(zip(coin, code))
print(d)
#answer = [('Joey', 'Chandler', 'David'),
# ('Monica', 'Pheobe', 'Rachel')]
#{'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}

#ex8
def fun(variable):
    letters=['a','e','o','u']
    if (variable in letters):
        return True
    else:
        return False
sequence=['g','j','e','j','k','o','p','r']
filtered=list(filter(fun,sequence))
print (filtered)
#answer = ['e', 'o']

#ex9
x=list(map(int,input("Enter a multiple value: ").split()))
print("list of student:",x)
#answer = Enter a multiple value: 2 5
#list of student: [2, 5]

#ex10
def newfunc(a):
    return a*a
x = list(map(newfunc,(1,2,3,4)))
print(x)
#answer = [1, 4, 9, 16]

#ex11
def func(a,b):
    return a+b
a = list(map(func,[2,4,5],[1,2,3,4]))
print(a)
#answer = [3, 6, 8]

#ex12
c = map(lambda x:x+x,filter(lambda x: (x>=3),(1,2,3,4)))
print(list(c))
#answer = [6, 8]

#ex13
c = filter(lambda x:(x>=3),map(lambda x:x+x,(1,2,3,4)))
print(list(c))
#answer = [4, 6, 8]

#ex14

import functools
list = [7,2,-2,3,1,0,9]
print (functools.reduce(lambda x,z: x if x < z else z, list))




#ex15
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
result = tuple(zip(numbers, letters))
print(result)



























