class static(object):
	statice=5
	def varfun(self):
		self.statice+=1
		print(self.statice)


if __name__=='__main__':
	a=static()
	for i in range(3): 
		a.varfun()
		