#!/usr/bin/python
#coding=utf-8

class Employee():
    empCount=0;

    def __init__(self,name,salary):

        self.name=name;
        self.salary=salary;
        Employee.empCount+=1;

    def displayCount(self):
        print("Total Employee %d",Employee.empCount);


    def displayEmployee(self):
        print("Name:",self.name,",salary:",self.salary);

    
        
e=Employee("Johannes",8000);
e.displayCount();
e.displayEmployee();

t=Employee("Johannes",8000);
t.displayCount();
