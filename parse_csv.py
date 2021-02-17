import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # next(csv_reader) #used to skip the line in csv

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',')

        for line in csv_reader:
            csv_writer.writerow(line)


        # print(line[2])
