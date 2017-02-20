import time

class time_counter:

	'''
	This class give us the time wasted in a process.
	It takes the time creation as reference,
	and return the time wasted.

	'''
    
	def __init__(self,start):
		self.start = time.mktime(start)
		(self.sd,self.sh,self.sm,self.ss) = start[2:6]
		#print(start[2:6])

	def wasted(self,current):
		#print(current[3:6])
		(self.cd,self.ch,self.cm,self.cs) = current[2:6]
		self.total_d = self.cd - self.sd
		self.total_h = self.ch - self.sh
		self.total_m = self.cm - self.sm
		self.total_s = self.cs - self.ss

		print("%d:%d:%d:%d" % (self.total_d,self.total_h,self.total_m,self.total_s))

#t0 = time.localtime()
#t = time_counter(t0)
#time.sleep(5)

#t.wasted(time.localtime())

