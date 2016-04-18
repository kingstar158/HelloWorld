#_*_coding:utf-8_*_
#__func__python中此类型函数的学习和理解

class Student(object):
	"""test for student class"""
	def __init__(self, name):
		self.name = name
        ##__str__() 返回用户看到的字符串 
	def __str__(self):
		return 'Student object (name:%s)' %self.name
	
        #__repr__() 返回开发者看到的字符串
	__repr__ = __str__

'''	
print Student("Marry Jack")
s = Student("Lily")
print s
'''


### __iter__ / __getitem__

class Fib(object):
        """test for functon"""

        def __init__(self):
                self.a, self.b = 0,1

        #__iter__() 使得类成员能够像列表一样被访问
        def __iter__(self):
                return self

        def next(self):
                self.a, self.b = self.b, self.a + self.b
                if (self.a > 100):
                        raise StopIteration()
                return self.a
        #__getitem__() 建立类实例的索引下标符
        '''
        def __getitem__(self, n):
                a,b = 1,1
                for x in range(n):
                        a,b = b, a + b
                return a
        '''
        def __getitem__(self, n):
                if isinstance(n, int):
                        a,b=1,1
                        for x in range(n):
                                a,b = b, a+b
                        return a
                if isinstance(n, slice):
                        start = n.start
                        stop = n.stop
                        a,b = 1,1
                        L = []
                        for x in range(stop):
                                if x >= start:
                                        L.append(a)
                                a,b = b,a+b
                        return L
        
        
'''
for n in Fib():
        print n

f = Fib()
print f[0]
print f[5]
print f[0:10]
'''

### __getattr__ / __setattr__

class Persion(object):
        def __init__(self):
                self.name = "Hary"

        def __getattr__(self, attr):
                if attr == 'age':
                        return 25
                raise AttributeError("\'Persion\' object has no attribute \'%s\'"%attr)



p = Persion()
print p.name
print p.age
print p.score
