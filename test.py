L = ["2_ref.txt","3_ref.txt", "4_ref.txt", "5_ref.txt", "6_ref.txt", "7_ref.txt"]

for file_name in L:
	print(file_name)
	with open (file_name, 'r') as f:
		s = f.readline()
		char_nums = {}
		count = 0
		for c in s:
			if c in char_nums:
				char_nums[c] += 1
			else:
				char_nums[c] = 1
			count += 1
			# if count >= 100000: break
	for key, value in sorted(char_nums.items(), key=lambda x: x[0]):
		print("   {} : {}".format(key,value))
