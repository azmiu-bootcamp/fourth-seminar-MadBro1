import csv
with open('data.csv',encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row[5] == "Juventus" and row[8] == "Right":
            print(row[2])
