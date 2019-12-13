import csv

with open ("myFile.csv","w+") as csvfile:
    writer=csv.writer(csvfile)
    i=0
    while i<100:
        writer.writerow("1")
        i+=1



with open ("myFile.csv","r+") as csvfile:
    reader=csv.reader(csvfile)
    i=0
    for row in reader:
        print()

    writer=csv.writer(csvfile)
    writer.writerow({i})