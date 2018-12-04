from sys import setrecursionlimit
setrecursionlimit(10000000)

class trieNode(object):
	def __init__(self,boo,parent,char,label):
		self.children = {}
		self.wordFin = boo
		self.parent = parent
		self.inedge = char
		self.label = label

	def traverse_up(self):
		return (self.parent, self.inedge)

	def set_fin(self,boo):
		self.wordFin = boo

	def set_lab(self,lab):
		self.label = lab

	def get_lab(self):
		return self.label

	def size(self):
		if len(self.children) == 0:
			return 1
		else:
			s = 0
			for c in self.children:
				s += self.children[c].size()
			return 1 + s

	def insert(self,word,lab):
		a = -1
		if not(word[0] in self.children):
			if len(word) == 1:
				self.children[word] = trieNode(True,self,word,lab)
			else:
				self.children[word[0]] = trieNode(False,self,word[0],lab)
				x = self.children[word[0]]
				x.insert(word[1:],lab)
		else:
			if len(word) == 1:
				x = self.children[word[0]]
				a = x.get_lab()
				x.set_fin(True)
				x.set_lab(lab)
			else:
				x = self.children[word[0]]
				a = x.get_lab()
				x.set_lab(lab)
				b = x.insert(word[1:],lab)
				if (b != -1):
					a = b
		return a

def op(x):
	if x == '1':
		return '0'
	else:
		return '1'


s = "0100110101"
w = ""
a = ""
T = trieNode(False,None,'',0)
fin = ""

for i in range(2000):
	if i < 10:
		a = s[i]
	w = a + w
	k = T.insert(w,i)
	fin += a
	a = op(fin[k+1])
	if (i%100 == 0):
		print(i)
		print(T.size())

with open("emseq-binary.txt",'w') as f:
	f.write(fin)