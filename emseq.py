class trieNode(object):
	def __init__(self,boo=False):
		self.children = {}
		self.wordFin = boo

	def addFin(self,char):
		self.children[char] = trieNode(True)

	def add(self,char):
		self.children[char] = trieNode()
