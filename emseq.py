from sys import setrecursionlimit
setrecursionlimit(10000000)

STRING_DICT = {}
insertion_dict = {}
Alphabet = 2
alph_str = ['0','1']
COUNT = 0

class trieNode(object):
	def __init__(self,parent,char,label):
		self.children = {}
		self.parent = parent
		self.inedge = char
		self.label = label # This is the label for keeping track of indices/time-stamp

	def toString(self,i=0):
		print(" "*i + str(self.get_lab()))
		for s in self.children:
			print(" "*i + s + " -> ")
			self.children[s].toString(i+1)

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

	def depth(self):
		m = 0
		for s in self.children:
			m = max(m,self.children[s].depth())
		return 1 + m

	def pref(s1, s2):
		# assumes that s1 is shorter than s2
		return s1 == s2[:len(s1)]

	def exist_pref(s1, s2):
		# assumes that s1 is shorter than s2
		x = ""
		for i in range(len(s1)):
			if s1[i] == s2[i]:
				x += s1[i]
			else:
				break
		return x

	def insert(self,word,lab):
		a = -1
		x = ""
		a = self.get_lab()
		self.set_lab(lab)
		count = 0
		for s in self.children:
			if s[0] == word[0]:
				x = trieNode.exist_pref(s,word)
				if x == s:
					z = self.children[s]
					(a,b) = z.insert(word[len(x):],lab)
					return (a,b+len(x))
				else:
					z = self.children[s]
					a = z.get_lab()
					self.children[x] = trieNode(self,x,lab)
					y = self.children[x]
					y.children[s[len(x):]] = z
					del(self.children[s])
					y.children[word[len(x):]] = trieNode(self,word[len(x):],lab)
					return (a,len(x)+count)
		self.children[word] = trieNode(self,word,lab)
		return (a,1+count)			

	def compress(self):
		d = list(self.children.keys())
		for i in d:
			self.children[i].compress
		d = list(self.children.keys())
		if len(d) == 1 and self.parent != None:
			gang = (self.children)[d[0]].children
			a = self.inedge
			self.inedge = (d[0] + a)
			self.parent.children.pop(a,None)
			self.parent.children[d[0] + a] = self
			self.children = gang




def op(x):
	return str((int(x) + 1) % Alphabet)


s = "0100"
w = ""
a = ""
T = trieNode(None,'',-1)
fin = ""
for i in range(200000):
	if i < 4:
		a = s[i]
	w = a + w
	fin += a
	COUNT = 0
	(k,COUNT) = T.insert(w,i)
	a = op(fin[k+1])
	# if (i%10000 == 0):
	# 	X = T.size()
	# 	T.compress()
	# 	Y = T.size()
	# 	if (X != Y):
	# 		print(i)
	if (i%10000 == 0):
	 	print(i)
	 	print("COUNT -> " + str(COUNT))
	 	



with open("2_ref.txt",'w') as f:
	f.write(fin)
