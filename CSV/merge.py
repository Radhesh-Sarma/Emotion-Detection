import csv

reader = csv.reader(open("SadProcessed.csv"))
reader1 = csv.reader(open("NotSadProcessed.csv"))

f = open("combined.csv", "w")
writer = csv.writer(f)

j = 0
for row in reader:
    if j==0:
    	writer.writerow(["Sad?"] + row)
    else:
	writer.writerow([1] + row)
    j += 1
    

i = 0
for row in reader1:
    if i!=0:
    	writer.writerow([0] + row)
    i += 1

f.close()
