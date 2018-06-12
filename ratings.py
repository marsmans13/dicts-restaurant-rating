"""Restaurant rating lister."""
import sys
from random import choice

file_name = sys.argv[1]
restaurant_info = {}

for line in open(file_name):
    line = line.rstrip().split(":")
    restaurant_info[line[0]] = line[1]


def get_user_input():
    print("If you would like to see all restaurants, type 1.")
    print("If you would like to add a restaurant and its rating, type 2.")
    print("If you would like to update a restaurant, type 3.")
    print("If you want to quit, type 4.")
    return input()


def test_user_rating(restaurant_name):
        new_rating = input("Please give us a rating from 1-5: ")

        while new_rating not in "12345":
            print("Please enter a number between 1 and 5.")
            new_rating = input()

        restaurant_info[restaurant_name] = new_rating


user_input = get_user_input()

while user_input != "4":

    if user_input == "1":
        for key in sorted(restaurant_info):
            print(key, "is rated at", restaurant_info[key] + ".")

    elif user_input == "2":
        new_restaurant = input("Please give us a restaurant name: ")
        test_user_rating(new_restaurant)

    elif user_input == "3":
        user_random = input("Do you want to update a random restaurant? y/n: ")

        if user_random.lower() == "y":
            random_restaurant = choice(list(restaurant_info.keys()))
            print(random_restaurant, "is rated at",
                  restaurant_info[random_restaurant] + ".")
            test_user_rating(random_restaurant)

        elif user_random.lower() == "n":
            print("These are the restaurants currently rated.")
            for key in restaurant_info:
                print(key)

            user_restaurant = input("Please enter the restaurant you want to rate.")

            while user_restaurant not in restaurant_info:
                print("Please enter a valid restaurant name.")
                user_restaurant = input()

            test_user_rating(user_restaurant)

    user_input = get_user_input()
