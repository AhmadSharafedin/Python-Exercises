from functools import reduce

class Person:
    def __init__(self,name,address):
        self._name = name
        self._address = address
    def __del__(self):
        print('I have been deleted')
    def getName(self):
        return self._name
        
    def setName(self, name):
        self._name = name
    
    def getAddress(self):
        return self._address
    
    def setAddress(self, address):
        self._address = address
    
'''        
p = Person('Ahmad','Amman')
print(p.getName())
p.setName('Hosam')
print(p.getName())
print(p.getAddress())
p.setAddress('Zarqa')
print(p.getAddress())
'''

class Employee(Person):
    def __init__(self, number:int,name , address, salary:float, jobTitle:str, loans:list):
        super().__init__(name, address)
        self.number = number
        self.__salary = salary
        self.__jobTitle = jobTitle
        self.__loans = loans
        
    def __del__(self):
        print ('I have been deleted')    
        
    def getSalary (self):
        return self.__salary
    
    def setSalary (self, salary):
        self.__salary = salary
        
    def getJobTitle (self):
        return self.__jobTitle
    
    def setJobTitle (self, jobTitle):
        self.__jobTitle = jobTitle
        
    def getTotalLoans (self):
        return sum(self.__loans)
    
    def getLoans (self):
        return self.__loans
    
    def setLoans (self, loans):
        self.__loans = loans

    def getMaxLon (self):
        if len(self.__loans) < 1:
            return None
        return max(self.__loans)

    def getMinLon (self):
        if len(self.__loans) < 1:
            return None
        return min(self.__loans)   
    
    def printInfo(self):
        print (f'''
Employee Number: {self.number}
Employee Name: {self._name}
Employee Address: {self._address}
Employee Salary: {self.__salary}
Employee Job Title: {self.__jobTitle}
Employee Loans: {self.__loans}
               ''')
        
        
'''    
e = Employee(5, 350.5, 'Programmer', [15,50,30,20,45])
print(e.getSalary())
e.setSalary(450.25)
print(e.getSalary())
print(e.getJobTitle())
e.setJobTitle('Operation Manager')
print(e.getJobTitle())
print(e.getTotalLoans())    
print(e.getLoans())  
e.setLoans([300,542,1434,7655,633])        
print(e.getLoans())
print(e.getMaxLon())
print(e.getMinLon())    
'''

class Student(Person):
    def __init__(self, number:int,name, address, subject:str, marks:dict):
        super().__init__(name, address)
        self.number = number
        self.__subject = subject
        self.__marks = marks
        
    def __del__(self):
        print ('I have been deleted')    
        
    def getSubject (self):
        return self.__subject
    
    def setSubject (self, subject):
        self.__subject = subject
    
    def getMarks (self):
        return self.__marks
    
    def setMarks (self, marks):
        self.__marks = marks
        
    def getAverage (self):
        return (sum(self.__marks.values())/len(self.__marks.values()))
   
    def getAMarks (self):
        return list(filter(lambda a: a>90 , self.__marks.values()))
    
    def printInfo(self):
        print (f'''
Student Number: {self.number}
Student Name: {self._name}
Student Address: {self._address}
Subject: {self.__subject}
Marks: {self.__marks}
               ''')
    
    

'''
s = Student(54, 'English',{'History':95,'Arabic':80})
print(s.getSubject())
s.setSubject('Maths')
print(s.getSubject())
print(s.getMarks())
s.setMarks({'Maths':85,'Scince':99,'Computer':92})
print(s.getMarks())
print(s.getAverage())    
print(s.getAMarks())      
'''    
    
employee1 = Employee(1000, 'Ahmad Yazan', 'Amman, Jordan', 500, 'HR Consultant', [434, 200, 1020])
employee2 = Employee(2000, 'Hala Rana', 'Aqaba, Jordan', 750, 'Department Manager', [150, 3000, 250])
employee3 = Employee(3000, 'Mariam Ali', 'Mafraq, Jordan', 600, 'HR S Consultant', [304, 1000, 250, 3000, 5000, 235])
employee4 = Employee(4000, 'Yasmeen Mohammad', 'Karak, Jordan', 865, 'Director', [])

student1 = Student(20191000, 'Khalid Ali', 'Irbid, Jordan', 'History', {
    'English': 80,
    'Arabic': 90,
    'Art': 95,
    'Management': 75
})
student2 = Student(20182000, 'Reem Hani', 'Zarqa, Jordan', 'Software Eng', {
    'English': 80,
    'Arabic': 90,
    'Management': 75,
    'Calculus': 85,
    'OS': 73,
    'Programming': 90
})
student3 = Student(20161001, 'Nawras Abdulllah', 'Amman, Jordan', 'Arts', {
    'English': 83,
    'Arabic': 92,
    'Art': 90,
    'Management': 70
})
student4 = Student(20172030, 'Amal Raed', 'Tafelah, Jordan', 'Computer Eng', {
    'English': 83,
    'Arabic': 92,
    'Management': 70,
    'Calculus': 80,
    'OS': 79,
    'Programming': 91
})
        
        
#ex1
EmployeesList=[employee1,employee2,employee3,employee4]

#ex2
StudentsList=[student1,student2,student3,student4]

#ex3
print (len(EmployeesList))

#ex4
print(len(StudentsList))

#ex5
for employee in EmployeesList:
    employee.printInfo()
    print ('Employee Total Loans is: ',employee.getTotalLoans())
    
#ex6
for student in StudentsList:
    student.printInfo()
    print ('Student Average Marks is: ',student.getAverage())

#ex7
highest_Avg=0
for student in StudentsList:
    if highest_Avg < student.getAverage():
        highest_Avg=student.getAverage()
print('The highest average is: ',highest_Avg)

#ex8
employee_has_loans = list(filter(lambda e: e.getMinLon(), EmployeesList))
min_employee_loan = min(list(map(lambda e: e.getMinLon(), employee_has_loans)))
print ('Employee min Loans is: ', min_employee_loan)

#ex9
max_employee_loan = max(list(map(lambda e: e.getMaxLon(), employee_has_loans)))
print ('Employee max Loans is: ', max_employee_loan)

#ex10
sum_loans=0
for employee in EmployeesList:
    print (f'''
{employee.getName()} : {employee.getLoans()}
Total loans is: {employee.getTotalLoans()}
           ''')
sum_loans=sum_loans+employee.getTotalLoans()
print('the total loans for all employees is :',sum_loans)

#ex11
print(list(map(lambda e: {e.number:e.getLoans()},EmployeesList)))
        
#ex12
for employee in employee_has_loans:
    max_loan=reduce(lambda a,b :a if a > b else b ,employee.getLoans())
    min_loan=reduce(lambda a,b : a if a < b else b ,employee.getLoans())
    print(employee.getName(),' the max and min loans are : ',max_loan, ', ',min_loan)
    
#ex13
students_HasA = list(filter(lambda s: len(s.getAMarks())>0, StudentsList))
for student in students_HasA:
    print(f'''
Name: {student.getName()}
Subject: {student.getSubject()}
Marks: {student.getMarks()}
''')
        
#ex14
max_salary=0
for employee in EmployeesList:
    if(employee.getSalary()>max_salary):
        max_salary=employee.getSalary()
print('the max employee salary is: ',max_salary)

        
#ex15
employees_salaries = list(map(lambda a: a.getSalary(), EmployeesList))
min_salary = min(employees_salaries)
print('Minimum Employee Salary is : ', min_salary)    


#ex16
Total_salary=0
for employee in EmployeesList:
    Total_salary=Total_salary+employee.getSalary()
print('the total salaries is: ',Total_salary)

#ex17
for employee in EmployeesList:
    del employee
for student in StudentsList:
    del student     
        
        
        
        
        
        
        
        
        
        
        
        
        

