import csv

with open("names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # skip over first line in an iterable using generator
    next(csv_reader)
 
    for line in csv_reader:
        print(f"Name: {line[0]} {line[1]}")