import csv

#parse csv using dictionary key

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # next(csv_reader) #used to skip the line in csv

    with open('new_names2.csv', 'w') as new_file:

        fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)


