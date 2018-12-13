L = ["0","1","2","3","4","5","6"]
fin_list = ["0","1","2","3","4","5","6"]

for i in range(3):
	d = []
	for f in fin_list:
		for l in L:
			d.append(f + l)
	fin_list += d

D = {}
for f in fin_list:
	D[f] = 0

with open("7_ref.txt", 'r') as f:
	x = f.readline()	
	n = len(x)
	for i in range(n - 2):
		D[x[i:i+2]] += 1
	for i in range(n - 3):
		D[x[i:i+3]] += 1
	for i in range(n - 4):
		D[x[i:i+4]] += 1

for key, value in sorted(D.items(), key=lambda x: len(x[0])):
		print("   {} : {}".format(key,value))
