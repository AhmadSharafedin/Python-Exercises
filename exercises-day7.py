import numpy as np
import matplotlib.pyplot as plt

#ex1
a = np.zeros(10, np.int)
print(a)

b = np.ones(10, np.int)
print(b)

f = np.ones(10, np.int) * 5
print(f)

#ex2
c= np.arange(30, 71)
print(c)

#ex3
s = np.arange(30, 71, 2)
print(s)

#ex4
e = np.arange(9).reshape(3, 3)
print(e)

#ex5
rand_num = np.random.normal(0, 1, 1)
print(rand_num[0])

#ex6
s = np.arange(12).reshape(3, 4)
print(s)

#ex7
seven = np.arange(20)
seven[(seven > 8) & (seven < 16)] *= -1
print(seven)

#ex8
eight_x = np.array([1, 8, 3, 5])
eight_y = np.random.randint(0, 11, 4)
eight_z = eight_x * eight_y
print(eight_z)

#ex9
nine = np.arange(6).reshape(2, 3)
print('nine:\n', nine)
print('"nine" array rows: ', nine.shape[0])
print('"nine" array columns: ', nine.shape[1])

#ex10
r = np.arange(27).reshape(3, 3, 3)
print(r)

#ex11
a = np.array([9, -1, 2, 3])
b = np.array([1, -6, 0, 10])
c = np.array([[1, 8, 2, 5], [3, 1, 7, 9]])

print('a - b:', a - b) #answer=[ 8  5  2 -7]
print('a * b:', a * b) #answe=[ 9  6  0 30]
print('a,dot(b):', a.dot(b)) #answer= 45
print('a * 2:', a * 2) #answer =[18 -2  4  6]
print('np.sin(a):', np.sin(a)) #answer=[ 0.41211849 -0.84147098  0.90929743  0.14112001]
print('a < 3:', a < 3) #answer= [False  True  True False]
print('a.sum(): ', a.sum()) #answer= 13
print('a.sum(axis=0):', a.sum(axis=0)) #answer= 13
print('c.sum():', c.sum()) #answer= 36
print('c.sum(axis=0)', c.sum(axis=0)) #answer= [ 4  9  9 14]
print('a.min():', a.min()) #answer= -1
print('a.mean():', a.mean()) #answer= 3.25
print('a average(): ', np.average(a)) #answer= 3.25
print('a median():', np.median(a)) #answer= 2.5
print('a std(): ', np.std(a)) #answer= 3.6314597615834874
print('a var():', np.var(a)) #answer= 13.1875
print('c.cumsum():', c.cumsum()) #answer= [ 1  9 11 16 19 20 27 36]
print("a[1:2] : ", a[1:2]) #answer= [-1]
print("a[2:] : ", a[2:]) #answer= [2 3]
print("c[-1] : ", c[-1]) #answer= [3 1 7 9]

#ex12
x = np.arange(1, 50)
y = [value * 3 for value in x]
plt.plot(x, y)
plt.title('Draw a line .')
plt.ylabel('Y-axis')
plt.xlabel('X-axi')
plt.show()

#ex13
x1 = [10, 20, 30]
x2 = [10, 20, 30]
plt.figure()
plt.plot(x1, [20, 40, 10], label="line1")
plt.plot(x2, [40, 10, 30], label="line2")
plt.title("Tow or more lines on same plot with suitable legends")
plt.legend(loc='upper right')
plt.show()

#ex14
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
plt.show()

#ex15
objects = ('Python', 'Java', 'PHP', 'JavaScript', 'C#', 'C++')
y_pos = np.arange(len(objects))
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(y_pos, popularity, align='center', color=[
        'red', 'black', 'green', 'blue', 'yellow', 'blue'])
plt.xticks(y_pos, objects)
plt.ylabel('Popularity')
plt.title('Languages')
plt.show()