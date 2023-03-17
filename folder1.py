def option1():
    print("you chose option 1")

def option2():
    print("you chose option 2")

def option3():
    print("you chose option 3")

def main_menu():
        print("\n === main menu ===")
        print("1. option 1")
        print("2. option 2")
        print("3. option 3")
        print("0. quit")

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



else:
     print("invalid choice, try again")