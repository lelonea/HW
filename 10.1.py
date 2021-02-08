import csv
path = '/home/ydavidouski/Desktop/exel.csv'
with open(path) as obj:
    age_1_12 = 0
    age_13_18 = 0
    age_19_25 = 0
    age_26_40 = 0
    age_40 = 0
    reader = csv.DictReader(obj)
    for row in reader:
        if int(row['age']) <= 12 and int(row['age']) > 1:
            age_1_12 += 1
        if int(row['age']) <= 18 and int(row['age']) > 12:
            age_13_18 += 1
        if int(row['age']) <= 25 and int(row['age']) > 18:
            age_19_25 += 1
        if int(row['age']) <= 40 and int(row['age']) > 25:
            age_26_40 += 1
        if int(row['age']) > 40:
            age_40 += 1

print(age_1_12)
print(age_13_18)
print(age_19_25)
print(age_26_40)
print(age_40)
