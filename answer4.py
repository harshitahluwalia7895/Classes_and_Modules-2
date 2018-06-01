class Shape:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def Area(self):
		self.area=self.length*self.breadth
		print("Area: ",self.area)

class Rectangle(Shape):
        pass
	

class Square(Shape):
        pass
	
chh='y'

while chh=='y':
	ch=input("Enter 1 for rectangle or 2 for Square:")

	if ch=='1':
		l=float(input("Enter length: "))
		b=float(input("Enter breadth: "))
		r1=Rectangle(l,b)
		r1.Area()

	elif ch=='2':
		s=float(input("Enter side: "))
		s1=Square(s,s)
		s1.Area()
	
	chh=input("Do you want to create more shapes??? y//n: ")




