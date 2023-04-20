#import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

#open csv file and create dataframe
with open("Video_Games_Sales_as_at_22_Dec_2016.csv","r") as file:
    csv_reader = csv.reader(file)
    header_row = next(csv_reader)
    dataframe = pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")

    #this function shows nintendos popularity over the years based on global sales
    def YoRvsNintendo():
        #set up variables
        years = dataframe["Year_of_Release"].unique()
        years.sort()
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        GlobalSales = []

        #iterate through each individual year and find the total global sales for each year
        for year in years:
            tempdf = dataframe[(dataframe["Year_of_Release"] == year) & (dataframe["Publisher"] == "Nintendo")]
            tempSum = tempdf["Global_Sales"].sum()
            GlobalSales.append(tempSum)     

        #display bar chart
        ax.bar(years,GlobalSales)
        plt.show()
    

    #this function will show how different publishers compare in NA
    def publisherNA(region):
        #init variables and arrays
        publishers = (dataframe["Publisher"].unique())
        dataArr = []
        Top10 = []
        others = 0
        labels = ['Nintendo','Microsoft','Ubisoft','Activision','Take-Two Interacrive','Atari','Sony Entertainment','bethesda','Sega','EA','other']

        #similar to iterating through the years in the first function
        #iterate through each publisher and find their total global sales since 1980
        for publisher in publishers:
            tempdf = dataframe[dataframe["Publisher"] == publisher]
            tempSum = tempdf[region].sum()
            dataArr.append(tempSum)
            
        #sorted in reverse order so i can find the highest rather than the lowest
        dataArr.sort(reverse = True)

        #iterate through dataArr to gather the top 10 highest selling publishers
        for i in range (0,10):
            Top10.append(dataArr[i])

        #gather the sales on all other publishers and populate the others array
        for i in range(10,len(dataArr)):
            others += dataArr[i]

        #append to the end so i can use the data value in my pie chart
        Top10.append(others)
        
        plt.style.use('_mpl-gallery-nogrid')

        #set up styling
        colors = plt.get_cmap('turbo')(np.linspace(0.2, 0.7, len(Top10)))

        # plot
        fig, ax = plt.subplots()

        #create the piechart
        piechart = ax.pie(Top10, colors=colors, labels=labels, labeldistance=0.75, radius=10, center=(4, 4),wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
        
        plt.show()  



publisherNA("NA_Sales")
YoRvsNintendo()
