#import packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

#open csv file and create dataframe
with open("Video_Games_Sales_as_at_22_Dec_2016.csv","r") as file:
    csv_reader = csv.reader(file)
    header_row = next(csv_reader)
    dataframe = pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")

#define the function we will be using to create each chart
def genreXplatform():
     while True:
    
    #initialize variables/lists
        platforms = ["PS2","X360","Wii","PS","DS","PSV","PC","3DS","PSP"]
        platform = ""
        while platform not in platforms:
            
            platform = input("Which platform do you want to view? (PS2, X360, Wii, PS, DS, PSV, PC, 3DS, PSP): ")
            
      
        
        if platform not in platforms:
            print('Invalid platform, please enter a valid platform.')
            continue

        genreDataframe = (dataframe["Genre"].unique())
        topGenres = {}
        for genre in genreDataframe:
            tempDataframe = dataframe[dataframe["Genre"] == genre]
            tempSum = tempDataframe[tempDataframe["Platform"] == platform]["Global_Sales"].sum()
            topGenres[genre] = tempSum
    
        #sort the dictionary by values and extract the top 5 genres
        sortedGenres = sorted(topGenres.items(), key=lambda x: x[1], reverse=True)[:5]
        topGenres = dict(sortedGenres)
        genres = list(topGenres.keys())
        sales = list(topGenres.values())

    #create and style the line graph
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(genres, sales, marker='o', color='orange', linewidth=2)
        ax.set_xlabel('Genre')
        ax.set_ylabel('Global Sales (in millions)')
        ax.set_title('Most Popular Genres on ' + platform)
        ax.tick_params(axis='x', labelrotation=45)
        plt.show()


        #ask if user wants to quit
        while True:
            choice = input("Do you want to view another platform? (y/n): ")
            if choice == "y":
                break
            elif choice == "n":
                return

#call the function
genreXplatform()



