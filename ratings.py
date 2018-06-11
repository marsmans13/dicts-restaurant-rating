"""Restaurant rating lister."""
import sys

file_name = sys.argv[1]
restaurant_info = {}

for line in open(file_name):
    line = line.rstrip().split(":")
    restaurant_info[line[0]] = line[1]


def get_user_input():
    print("If you would like to see all restaurants, type 1.")
    print("If you would like to add a restaurant and its rating, type 2.")
    print("If you want to quit, type 3.")
    return input()


user_input = get_user_input()

while user_input != "3":

    if user_input == "1":
        for key in sorted(restaurant_info):
            print(key, "is rated at", restaurant_info[key] + ".")

    elif user_input == "2":

        new_restaurant = input("Please give us a restaurant name: ")
        new_rating = input("Please give us a rating from 1-5: ")

        while new_rating not in "12345":
            print("Please enter a number between 1 and 5.")
            new_rating = input()

        print("\n")

        restaurant_info[new_restaurant] = new_rating

    user_input = get_user_input()
