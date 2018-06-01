'''Create a class Animal as a base class and define method animal_attribute.
Create another class Tiger which is inheriting 
Animal and access the base class method.'''

class Animal:
    
    def animal_attribute(self):
    
        print('This is animal_attribute function in Animal class')

class Tiger(Animal):
    
    def display_Tiger():
        
        print('This is a Tiger class')
    
t=Tiger()
t.animal_attribute()
