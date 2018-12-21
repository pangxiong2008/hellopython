
a=100 
if a>100:
        print(a)
else:
        print(-a)

s='i \'m  \"ok"'
print (s)


print('''line1
line2
line3'''
)

def is_odd(n):
        return n%2==1
number=list(filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15]))
print(number)
def f(x):
        return x*x
number2=list(map (f,[1,2,3,4]))
print(number2)
        
class Student(object):
        def __init__(self, name, score):
                self.name=name
                self.score=score
bat=Student('123',15)
bat.name

def print_score(std):
        print('%s:%s' % (std.name,std.score))


print_score(bat)
class Teacher(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender=gender
    
teah=Teacher('hh','123456')
print(teah.get_gender())
class Animal(object):
        def run(self):
                print('Animal is running...')
        def run_twice(animal):
            animal.run()
class Dog(Animal):
        def run(self):
                print ('Dog is running...')
class Cat(Animal):
        def run(self):
                print ('Cat is running...')
dog=Dog()
dog.run_twice()
cat=Cat()
def run_twice2(animal):
        animal.run()

run_twice2(Animal())
type(dog)
def set_age(self,age):
        self.age=age
class StudentTest(object):
        @property
        def score(self):
                return self._score
        @score.setter
        def score(self,value):
                self._score=value
s=StudentTest()
s.score=60
s.score

from enum import Enum,unique
@unique
class Weekday(Enum):
        Sun=0
        Mon=1

day1=Weekday.Mon
print()
        




