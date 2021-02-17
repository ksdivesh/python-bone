import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)


    with open('names2.csv', 'w') as csv_file2:
        fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(csv_file2, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()

        for line in csv_reader:
            print(line)
            csv_writer.writerow(line)







# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     for line in csv_reader:
#         print(line.first_name)


    # print(csv_reader)