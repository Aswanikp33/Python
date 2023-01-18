import csv
csv_file1=open("students details.csv")
csv_reader=csv.reader(csv_file1)
for line in csv_file1:
    print(line)
