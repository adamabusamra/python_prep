import csv


def writeToCsv(data):
    with open('./data/data.csv', 'w', newline='') as file:
        fieldnames = ['API', 'Auth', "Category",
                      "Cors", "Description", "HTTPS", "Link"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow(row)
