import csv
import random

# CSV Structure
# ['Title', 'Author', 'Genre', 'Height', 'Publisher', TODO:'Has Read']

# Objective:
#   - Get unique Genre's and display 5 at random.
#       -Funcitons: Gives a random 5 numbers -> [2, 3, 50, 40, 20]
# Mark Books as 'Read'
#   - Learn how to manipulate the csv
# Find Books based on Author or Genre


def master_intro():
    intro = """Welcome to the Magnificent Book Selector! Please select an option below to begin:
1. Find a Book Randomly
2. Generate suggestions based on Genre
3. Exit
"""
    print(intro)
    intro_question = input("Enter a Number: ")
    return intro_question

# Function that selects a random book from the list


def random_book():
    with open('books.csv', newline='') as f:
        reader = csv.reader(f)
        data_list = list(reader)
        print(data_list[0])
        print(random.choice(data_list))

# Function that lets the user to continue or exit the script after selecting a book.


def master_continue_choice():
    continue_choice = input("Would you like to select another book?(Y/N): ")
    if continue_choice.lower() == 'y':
        master_book_selector()
    elif continue_choice.lower() == 'n':
        print('Exiting')
        exit()
    else:
        print('Please select Y or N.')
        master_continue_choice()

# Master function that runs the other functions based off selection


def master_book_selector():
    try:
        intro_results = master_intro()
        if int(intro_results) == 1:
            random_book()
            master_continue_choice()
        elif int(intro_results) == 2:
            # this will be the genre selector perhaps
            print('almost there')
        elif int(intro_results) == 3:
            print('Exiting')
            exit()
        else:
            print('Invalid input, please try again.')
            master_book_selector()
    except ValueError:
        print("Invalid value, please try again.")
        master_book_selector()
    except TypeError:
        print("Invalid type, please try again.")
        master_book_selector()


master_book_selector()
# for b in range(len(data_list)):
# print("Title", data_list[b][0])
# print("Author", data_list[b][1])
# print("Genre", data_list[b][2])
# print("Height", data_list[b][3])
# if data_list[b][4]:
#print("Title", data_list[b][0])

#print("Publisher", data_list[b][4])

# print(data)
