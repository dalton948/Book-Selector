import csv
import random

# CSV Structure
# ['Title', 'Author', 'Genre', 'Height', 'Publisher', TODO:'Has Read']

# Objective:
# Random Book Selection (excluding books already read)
#   - Get unique Genre's and display 5 at random.
#       -Funcitons: Gives a random 5 numbers -> [2, 3, 50, 40, 20]
# Mark Books as 'Read'
#   - Learn how to manipulate the csv
# Find Books based on Author or Genre

intro = """1. Find a Book Randomly
2. Mark a Book as 'Read'
3. Generate suggestions based on Genre
"""
print(intro)
intro_question = input("Enter a Number: ")

# Might be used for the questionaire process


# def questionaire():
# for answer in questions
# print()


# while True:
#     question1 = input("This is the first question: ")
#     if question1 == "" or question1.lower() == "no":
#         print("Exiting")
#         quit()
#     else:
#         break


with open('books.csv', newline='') as f:
    reader = csv.reader(f)
    data_list = list(reader)
    print(data_list[0])
    print(random.choice(data_list))

    # for b in range(len(data_list)):
    # print("Title", data_list[b][0])
    # print("Author", data_list[b][1])
    # print("Genre", data_list[b][2])
    # print("Height", data_list[b][3])
    # if data_list[b][4]:
    #print("Title", data_list[b][0])

    #print("Publisher", data_list[b][4])

    # print(data)
