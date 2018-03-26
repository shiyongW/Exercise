Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> id(1)
1658023392
>>> abs(-1)
1
>>> sqrt(8)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    sqrt(8)
NameError: name 'sqrt' is not defined
>>> import math as mm
>>> mm.sqrt(8)
2.8284271247461903
>>> mm.sqrt(9)
3.0
>>> a=list((2,3,4,5,6))
>>> a
[2, 3, 4, 5, 6]
>>> help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __reduce__(...)
 |      helper for pickle
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop

>>> range(1,10)
range(1, 10)
>>> range(1,10,2)
range(1, 10, 2)
>>> list(range(1,20,2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> list(range(1.1,9.9,2))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list(range(1.1,9.9,2))
TypeError: 'float' object cannot be interpreted as an integer
>>> list(range(1,1000,10))
[1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 201, 211, 221, 231, 241, 251, 261, 271, 281, 291, 301, 311, 321, 331, 341, 351, 361, 371, 381, 391, 401, 411, 421, 431, 441, 451, 461, 471, 481, 491, 501, 511, 521, 531, 541, 551, 561, 571, 581, 591, 601, 611, 621, 631, 641, 651, 661, 671, 681, 691, 701, 711, 721, 731, 741, 751, 761, 771, 781, 791, 801, 811, 821, 831, 841, 851, 861, 871, 881, 891, 901, 911, 921, 931, 941, 951, 961, 971, 981, 991]
>>> list(range(0,100,10))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> list('wangshiyong')
['w', 'a', 'n', 'g', 's', 'h', 'i', 'y', 'o', 'n', 'g']
>>> list({'a':3,'b':2,'c':4,'d':9})
['a', 'b', 'c', 'd']
>>> list({'a':3,'b':2,'c':4,'d':9}.items())
[('a', 3), ('b', 2), ('c', 4), ('d', 9)]
>>> x=list(range(10))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> import random
>>> random.shuffle(x)
>>> x
[5, 8, 1, 0, 4, 9, 6, 2, 7, 3]
>>> random.shuffle(x)
>>> x
[0, 2, 7, 8, 6, 5, 9, 1, 3, 4]
>>> x[4]
6
>>> x[-3]
1
>>> x[0]
0
>>> x[1]
2
>>> del x
>>> 
>>> x
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x=range(3)
>>> x
range(0, 3)
>>> x=list(range(3))
>>> x
[0, 1, 2]
>>> del[1]
SyntaxError: can't delete literal
>>> del x[1]
>>> x
[0, 2]
>>> x[1]
2
>>> del x
>>> x={'a':1,'b':5,'c':3}
>>> x
{'a': 1, 'b': 5, 'c': 3}
>>> del x[1]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    del x[1]
KeyError: 1
>>> del x['a']
>>> x
{'b': 5, 'c': 3}
>>> x['a']
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x['a']
KeyError: 'a'
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x=(1,2,3)
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> x[0]
1
>>> x[0]=2
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    x[0]=2
TypeError: 'tuple' object does not support item assignment
>>> gc.collect()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    gc.collect()
NameError: name 'gc' is not defined
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x=[11,4,8,32,42,22]
>>> y=x.append('ff')
>>> y
>>> print(y)
None
>>> x
[11, 4, 8, 32, 42, 22, 'ff']
>>> 
>>> y
>>> del y
>>> del x[-1]
>>> x
[11, 4, 8, 32, 42, 22]
>>> x.insert()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    x.insert()
TypeError: insert() takes exactly 2 arguments (0 given)
>>> x.insert(2,'a')
>>> x
[11, 4, 'a', 8, 32, 42, 22]
>>> x.insert(-2,'b')
>>> x
[11, 4, 'a', 8, 32, 'b', 42, 22]
>>> y=['c','d','e']
>>> x.extend(y)
>>> x
[11, 4, 'a', 8, 32, 'b', 42, 22, 'c', 'd', 'e']
>>> 
