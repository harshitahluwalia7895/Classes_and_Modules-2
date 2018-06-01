class Cop:
	def __init__(self):
		self.name='testCop'
		self.age=30
		self.workexp=4
		self.desig='testCop'

	def addDetails(self,name,age,workexp,desig):
		self.name=name
		self.age=age
		self.workexp=workexp
		self.desig=desig

	def Display(self):
		print("Cop Details:")
		print("Name: ",self.name)
		print("Age: ",self.age)
		print("Work Experience: ",self.workexp)
		print("Designation: ",self.desig)


class Mission(Cop):
	basicObjective='prevent crime'
	def add_mission_details(self):
		print("Mission details: ")
		print(self.basicObjective)

m1=Mission()
name=input("Enter name of cop: ")
age=int(input("Enter age of cop: "))
workexp=int(input("Enter work experience: "))
desig=input("Enter designation: ")
m1.addDetails(name,age,workexp,desig)

m1.Display()
m1. add_mission_details()

