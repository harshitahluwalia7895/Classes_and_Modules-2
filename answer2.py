'''Q2.What will be the output of following code.
   Answer2= It will show error at Line Number 14 and 15 because there is no parentheses in the print statement.
   ---->The correct code is mention Below and its Output is
	 A B 
	 A B					
'''

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())

