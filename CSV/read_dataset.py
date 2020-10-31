import csv
import numpy as np

dataset = csv.reader(open("combined.csv"))

a = []
b = []

i = 0
for row in dataset:
	if i!=0:
		a.append(row[2:])
		b.append(row[0])
	i += 1

data_inputs = np.array(a)

data_outputs = np.array(b)

