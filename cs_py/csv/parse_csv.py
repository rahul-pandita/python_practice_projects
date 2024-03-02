import csv

with open("names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # skip over first line in an iterable using generator
    # next(csv_reader)

    with open("new_names.csv", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter="\t")
 
        for line in csv_reader:
            csv_writer.writerow(line)