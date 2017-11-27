import random
import datetime


class Family:
	def __init__(self,array):
		self.num = len(array)
		self.f = array

	def getArray(self):
		return self.f
	def getNum(self):
		return self.num

	def shuffle(self):
		random.shuffle(self.f)


		
			
		
	def getPeople(self,n):
		if n < self.num + 1 :
			foo2 = self.f
			return foo2[n]



def trueShuffle(fam1):
		foo = fam1.getArray()
		old = foo[:]


		i=0
		n = fam1.num
		while (i<n): 
			if old[i] == fam1.getPeople(i) :
				i=-1
				fam1.shuffle()
				
			i=i+1


def getSantas():
	f = open('data/mail', 'r')
	i=0
	A=[]
	for line in f:
		arr = line.split('	')
		A.append(arr[0])
		i=i+1	
	f.close()
	return A

def main(year):
	
	A = getSantas()
	random.shuffle(A)
	Fam = Family(A[:])	
	old = Family(Fam.getArray()) # Not the old ! 
	trueShuffle(Fam)
	n = Fam.getNum()
	for i in range(0,n):
		Santa = A[i]
		Gifte = Fam.getPeople(i)
		f = open('People/'+str(Santa)+str(year)+'.txt','w')
		g = open('ASCII','r')
		f.write('*************************************************************************\n')
		f.write('Salut ' + Santa +',\n')
		f.write('J\'ai l\'immense plaisir de t\'annoncer que, cette annee, tu devras offrir un superbe cadeau a '+str(Gifte)+'.\n')
		f.write('*************************************************************************\n\n\n')
		ascii = g.read()
		f.write(ascii)
		f.close()
		g.close()

now = datetime.datetime.now()
main(now.year)












