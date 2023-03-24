import csv

def importCSVfile(fileName):
    global file
    with open(fileName,"r") as file:
        csv_reader = csv.reader(file)

importCSVfile("Video_Games_Sales_as_at_22_Dec_2016.csv")

selectedheaders = []

def displayData(file,):


