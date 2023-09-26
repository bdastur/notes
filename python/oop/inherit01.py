#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person():
    def __init__(self, fname, lname, id="Random") -> None:
        self.fname = fname
        self.lname = lname
        self.id = id

    def printName(self):
        print("%s, %s [%s]" % (self.fname, self.lname, self.id))

class Student(Person):
    pass

class Employee(Person):
    def __init__(self, lname, fname, age=35):
        super().__init__(lname, fname)
        self.fname = lname
        self.lname = fname
        self.age = age
    
    def printName(self):
        print("Employee %s, %s, %s" % (self.fname, self.lname, self.age))

def main():
    person = Person("Behzad", "Dastur")
    person.printName()
    Student("John", "Doe").printName()
    Employee("Joe", "Stan").printName()

if __name__ == '__main__':
    main()