import csv
id="1103047"
c=0
with open ("data.csv","w+") as csvfile:
    fieldnames=["Name","ID"]
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name":"Shakhawat", "ID":"1103047"})
    writer.writerow({"Name":"Shakhawat1", "ID":1103048})


with open("data.csv","r+") as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        if row["ID"]==id:
            print(row)
