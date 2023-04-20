import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy

with open("Video_Games_Sales_as_at_22_Dec_2016.csv","r") as file:
    csv_reader = csv.reader(file)
    header_row = next(csv_reader)
    dataframe = pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")

    EUSales = dataframe ["EU_Sales"].mean()
    NASales = dataframe ["NA_Sales"].mean()
    JPSales = dataframe ["JP_Sales"].mean()
    OtherSales = dataframe ["Other_Sales"].mean()

    print(EUSales)
    
plt.style.use('fivethirtyeight')


slices = [ EUSales, NASales, JPSales, OtherSales ]

labels = [ 'EU Sales', 'NA Sales', 'JP Sales', 'Other Sales' ]

explode = [0, 0, 0, 0]

colors = ['red', 'green', 'yellow', 'blue']

plt.pie(slices, labels=labels, explode =explode, shadow=True, autopct='%1.1f%%', wedgeprops={'edgecolor':'black', 'linewidth': 1 }, colors=colors)

plt.title("Just How Big Are These Markets?")
plt.grid(True)
plt.show()