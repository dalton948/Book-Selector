import csv
import random
import logging

# Objective:
#   - Get unique Genre's and display 5 at random.
#       -Funcitons: Gives a random 5 numbers -> [2, 3, 50, 40, 20]
# Mark Books as 'Read'
#   - Learn how to manipulate the csv
# Find Books based on Author or Genre
header = ['Title', 'Author', 'Genre', 'Height', 'Publisher']
logging.basicConfig(filename='errors.log', level=logging.INFO)

# Function for the intro questions and starting loop.


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
        selected = random.choice(data_list)

        for h in range(len(header)):
            print(f'{header[h].ljust(10)}: {selected[h]}')
        print("")


# Function that lets the user to continue or exit the script after selecting a book.
def master_continue_choice():
    continue_choice = input("Would you like to select another book? (Y/N): ")
    if continue_choice.lower() == 'y':
        master_book_selector()
    elif continue_choice.lower() == 'n':
        logging.info("Exit")
        print("""
        Thank you for choosing the Magnificent Book Selector!
            
        """)
        exit()
    else:
        print('Please select Y or N.')
        master_continue_choice()


# Master function that runs the other functions based off selection
def master_book_selector():
    try:
        logging.info("Choosing")
        intro_results = master_intro()
        if int(intro_results) == 1:
            random_book()
            master_continue_choice()
        elif int(intro_results) == 2:
            # this will be the genre selector perhaps
            print("""
            Feature not implemented yet, please choose another option

            """)
            master_book_selector()
        elif int(intro_results) == 3:
            logging.info("Exit")
            print("""
            Thank you for choosing the Magnificent Book Selector!
            
            """)
            exit()
        else:
            logging.error("invalid value entered: {}".format(intro_results))
            print('Invalid input, please try again.')
            master_book_selector()
    except ValueError:
        logging.error("invalid value entered: {}".format(intro_results))
        print("Invalid value, please try again.")
        master_book_selector()
    except TypeError:
        logging.error("invalid value entered: {}".format(intro_results))
        print("Invalid type, please try again.")
        master_book_selector()


master_book_selector()
