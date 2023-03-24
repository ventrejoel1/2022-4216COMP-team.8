import csv

def importCSVfile(FileName):
    with open(filename,"r") as file:
        csv_reader = csv.reader(file)
        header_row = next(csv_reader)
        print(header_row)

