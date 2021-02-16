import fileinput

def writeToFile(order):
	for num in range(0, len(order)):
		print(order[str(num)], end="")

order = {}
for line in fileinput.input():
	if line.startswith('::endmodel'):
		writeToFile(order)
		print(line)
		order.clear()
	elif line.startswith('occurs'):
		k = line.rfind(",")
		num = line[k+1:][:-2]
		if num in order:
			order[num] += line
		else:
			order[num] = line
	else:
		print(line, end="")