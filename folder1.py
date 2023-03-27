import csv
import pandas as pd

#importing data
with open("Video_Games_Sales_as_at_22_Dec_2016.csv","r") as file:
    csv_reader = csv.reader(file)
    header_row = next(csv_reader)
    dataframe = pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")
    

#define a fuction for the three options and main menu     

    def option1():
        userHeaderRow = []
        #user chooses what columns they would like to view
        print("== Please select the columns you would like to view ==\n")
        print("1.Name")
        print("2.Platform")
        print("3.Year_of_Release")
        print("4.Genre")
        print("5.Publisher")
        print("6.NA_Sales")
        print("7.EU_Sales")
        print("8.JP_Sales")
        print("9.Other_Sales")
        print("10.Global_Sales")
        print("11.Critic_Score")
        print("12.Critic_Count")
        print("13.User_Count\n")
        userColumns = input("Please enter the colums numbers you would like to view with a comma between each one:\n")

        #create a list of integers for the columns
        userColumnsList = userColumns.split(",")
        userColumnsList = list(map(int,userColumnsList))

        #validate the users answers
        for i in range(0,len(userColumnsList)):
            if 0 < userColumnsList[i] < 14:
                i += 1
                validationOption1 = True
            else:
                print("you have entered a value, {}, that is not an option in the menu".format(userColumnsList[i]))
                validationOption1 = False

        if validationOption1:
            userDesiredRows = int(input("please input the amount of rows you would like to view:\n"))
            for i in range(0,len(userColumnsList)):
                userHeaderRow.append(header_row[userColumnsList[i] - 1])

            print("DISPLAYING DATA:\n")
            desiredTable = dataframe.loc[0:userDesiredRows,userHeaderRow]
            print(desiredTable)

        else:
            print("quiting to MAIN MENU...") 

    def option2():
        print("\nyou chose option 2")

    def option3():
        print("\nyou chose option 3")

    def main_menu():
            print("\n === main menu ===")
            print("1. display data")
            print("2. display insights")
            print("3. option 3")
            print("0. quit")

    #create a loop to dispay the menu and read user input
    while True:
            main_menu()
            choice = input("enter your choice:")

            if choice == "1":
                option1()

            elif choice == "2":
                option2()

            elif  choice == "3":
                option3()
        
            elif choice == "0":
                print("Goodbye!")
                break

    #Input validation

            else:
                print("invalid choice, try again") 

