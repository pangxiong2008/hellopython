import logging
import pdb
logging.basicConfig(level=logging.INFO)
class Student(object):
    __slots__=('name','age')
s=Student()
s.name='123'
s.age=12
v='0'
n=int(v)
logging.info('n=%d' % n)
pdb.set_trace()
def foo():

