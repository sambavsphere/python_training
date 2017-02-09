'''
mul() -> tow int -> multi
int str -> str*int
str1,str2 -> None



'''


class operations:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def mul(self):
		if isinstance(self.a,str) and isinstance(self.b,str):
			return None
		try:
			return self.a*self.b
		except Exception as err:
			return err