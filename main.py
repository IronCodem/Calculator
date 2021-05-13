import math, random
import random

class Calculator:
	def __init__(self):
		self.vars = {"x": None,"y": None,"z": None}
		self.solved = 0
		self.operations = ["*","+","-","/","//","**","%","<",">","<=",">=","==","!=","(",")","()",".","e","="]
		self.var_allowed = ['x','y','z']
		self.history = []
		self.ans = 0
		self.pi = math.pi
	def calculate(self,equation):
		try:
			equation = equation.replace("ans",str(self.ans)).replace(" ","").replace("pi","3.141592653589793238462643").replace("x",str(self.vars["x"])).replace("y",str(self.vars["y"])).replace("^","**")
			if 'zen' not in equation:
				equation.replace("z",str(self.vars["z"])) 
			else:
				pass
			if equation.lower() == 'quit':
				return "bye"
			elif equation.lower() in ["area","circle","circle area"]:
				return self.area
			elif equation.lower() == "clear":
				print("\033[H\033[2J")
				return
			elif equation.lower() == 'help':
				return open("README.md", "r").read()
			elif equation == 'zen':
				zen = exec("import this")
				return zen
			elif equation.lower() in ["sqrt","squareroot","square root"]:
				what = input('sqrt > ')
				self.ans = self.sqrt(what)
				return self.sqrt(what)
			elif equation.lower() in ["abs","absolute","absolute value","absolutevalue"]:
				what = input('abs > ')
				self.ans = self.abs(what)
				return self.abs(what)
			elif equation.lower() in ["showequations","show equations","show"]:
				return self.allEquations
			elif equation.lower() in ["howmany", "solved","how many","how many solved"]:
				return self.howMany
			elif equation.lower() in ["assign","var","variable"]:
				text1 = input("Variable name (x,y,z) > ")
				text2 = input("Value > ").replace("ans",str(self.ans)).replace(" ","")
				self.assign(text1,text2)
			else:
				#for debugging
				#print(equation)
				for char in equation:
					if not (char.isnumeric() or char in self.operations):
						if char == '!=':
							pass
						return Exception("Has to be an equation.")
						
				
				answer = eval(equation)
				self.ans = answer
				self.solved += 1
				self.history.append(f"{self.solved}. {equation} = {answer}")
				return answer
		except Exception as Err:
			print('Invalid equation')
			return Err
	@property
	def allEquations(self) -> list:
		if self.history != []:
			return '\n'.join(list(equation for equation in self.history))
		else:
			return "none yet..."
	
	@property
	def area(self):
		try:
			r = float(input('Enter radius > '))
			a = self.pi * (r**2)
			return a
		except Exception as Err:
			print('Invalid number')
			return Err

	@property
	def howMany(self) -> int:
		return self.solved

	def sqrt(self,num) -> float:
		try:
			num = num.replace("ans",str(self.ans)).replace(" ","").replace("pi","3.141592653589793238462643")
			return math.sqrt(float(num))
		except Exception as Err:
			print('Invalid number')
			return Err

	def abs(self,num) -> float:
		try:
			num = num.replace("ans",str(self.ans)).replace(" ","").replace("pi","3.141592653589793238462643")
			return abs(float(num))
		except Exception as Err:
			print('Invalid number')
			return Err
	def assign(self,var,value):
		try:
			if var.isnumeric:
				self.vars[var] = value
			else:
				print('Value has to be a number')
		except Exception as Err:
			print('Invalid response')
			print(Err)


c = Calculator()
while not False:
	out = c.calculate(input(">>>  "))
	if out == 'bye':
		print('Thanks for using the Python Advanced Calculator!')
		break
	if out != None: print(out)
