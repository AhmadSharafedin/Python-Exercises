'''
#ex1
a=5
b= 10
if a>b:
    print (a)
else:
    print (b)
    
#ex2
a=int(input('enter a number:'))
for x in range (10):
    x+=1
    z=a * x
    print (a ,'*', x ,'=', z)
    
#ex3
n=5;
for a in range(n):
    for c in range(a):
        print ('* ', end="")
    print('')

for a in range(n,0,-1):
    for c in range(a):
        print('* ', end="")
    print('')
    
#ex4
letters = ['x', 'y', 'z', 'a', 'c']
for i in letters:
    if i == 'a':
        continue
    elif i=='c':
        break
    print(i)
    
#ex5
for x in range(12,25,3):
    print(x)
    
#ex6
i = 1
while i < 6:
    print (i)
    if i ==3:
        break
    i += 1
   
#ex7
a = int(input('enter a number: '))
x = 0
for i in range(a+1):
    x+=i
print (x)
  

#ex8
a=int(input('enter a number: '))
if (a%2)==0:
    print('number', a, 'is even')
else:
    print('number',a,'is odd')


#ex9
for a in range(9):
    c=0
    for b in range(8-a):
        print(" ",end=" ")
    for b in range(a+1):
        c+=1
        if c>9:
            break
        print(c,end=" ")
    for d in range(a):
        c-=1
        if c<1:
            break
        print(c,end=" ")      
    print()
for a in range(8):
    c=0
    for b in range(a+1):
        print(" ",end=" ")
    for b in range(8-a):
        c+=1
        if c>9:
            break
        print(c,end=" ")
    for b in range(8-(a+1)):
        c-=1
        if c<1:
            break
        print(c,end=" ")      
    print()
    
#ex10
while True:
    try:
        a = input("enter an integer number: ")
        a = int(a)
        break
    except ValueError:
        print("There may or may not have been an exception")
print(a) 

#ex11
try:
    a=3
    if a<4:
        b = a/(a-3)
    print('Value of b=',b)
except(ZeroDivisionError, NameError):
    print('\nError Occured and Handled')

'''









