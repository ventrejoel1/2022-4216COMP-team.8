import csv

#define a fuction for the three options and main menu

def option1():
    print("\nyou chose option 1")

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

        