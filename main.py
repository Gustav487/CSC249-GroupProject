# main.py
#
# Group: Smarty Pants
# 7/23/2024
#

""" This program is an info game for helping the
    user understand a few of data structures"""


def main():
    print("Welcome to the Data Structures info game!")

    response = ""

    while response != "0":
        display_main_menu()
        response = input('Enter your choice: ')

        if response == "1":
            from custom_array import Array, array_actions, display_info
            action_response = ""

            display_info()

            # Ask user for an initial length of the array
            capacity = int(input("How many initial elements do you want on the array? "))
            initial_array = Array(capacity)

            # Populate the array
            for item in range(capacity - 1, -1, -1):
                initial_array.insert(0, item)

            # Decided to create the initial array for not confusing the user
            print("An initial array was created.\n")
            print("Go ahead and modify the elements for better understanding. Happy studies!")
            print(f"Here is the initial array: {initial_array}")

            while action_response != "0":
                display_action_menu()
                action_response = safe_input('Enter your choice: ', int)
                structure = array_actions(initial_array, action_response)

        elif response == "2":
            from listbag import ListBag, bag_actions
            action_response = ""

            initial_bag = ListBag()

            while action_response != "0":
                display_action_menu()
                action_response = safe_input('Enter your choice: ', int)
                structure = bag_actions(initial_bag, action_response)

        elif response == "3":
            from liststack import ListStack, stack_actions
            action_response = ""

            initial_stack = ListStack()

            while action_response != "0":
                display_action_menu()
                action_response = safe_input('Enter your choice: ', int)
                structure = stack_actions(initial_stack, action_response)

        elif response == "4":
            from listqueue import ListQueue, queue_actions
            action_response = ""

            initial_queue = ListQueue()

            while action_response != "0":
                display_action_menu()
                action_response = safe_input('Enter your choice: ', int)
                structure = queue_actions(initial_queue, action_response)

        elif response == "5":
            from listdictionary import ListDictionary, dict_actions
            action_response = ""

            initial_dict = ListDictionary()

            while action_response != "0":
                display_dict_action_menu()
                action_response = safe_input('Enter your choice: ', int)
                structure = dict_actions(initial_dict, action_response)

        elif response != "0":
            print("Invalid choice. Try again.\n")

    print("\nThank you for playing the Data Structures info game!")


def safe_input(prompt, expected_type=int):
    while True:
        try:
            return expected_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {expected_type.__name__}.")


def display_main_menu():
    print("\nWhat type of data structure do you want to learn?")
    print("(1) Arrays\n"
          "(2) Bags\n"
          "(3) Stacks\n"
          "(4) Queues\n"
          "(5) Dictionaries\n"
          "(0) Exit")


def display_action_menu():
    print("\nWhat action do you want to perform with the data structure you have chosen?")
    print("(1) Add an element\n"
          "(2) Remove an element\n"
          "(3) Check the structure length\n"
          "(4) Show elements of the structure\n"
          "(5) Clear the structure\n"
          "(6) Search for an element\n"
          "(7) Sort the structure\n"
          "(8) Save the structure to a file\n"
          "(9) Load the structure from a file\n"
          "(0) Go back to the main menu")


def display_dict_action_menu():
    print("\nWhat action do you want to perform with the dictionary?")
    print("(1) Add a key-value pair\n"
          "(2) Remove a key-value pair\n"
          "(3) Lookup a value by key\n"
          "(4) Check the dictionary length\n"
          "(5) Show all key-value pairs\n"
          "(6) Clear the dictionary\n"
          "(0) Go back to the main menu")


if __name__ == '__main__':
    main()
