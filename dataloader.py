import csv

def loadCsv(filename):
	lines = csv.reader(open(filename, "r"))
	dataset = list(lines)
	for i in range(len(dataset)):
		#print(dataset[i])
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset