"""
File: listdictionary.py
A list-based implementation of dictionaries.
"""


def dict_actions(initial_dict, action_response):
    if action_response == "1":
        key = safe_input("Enter the key to add: ", int)
        value = safe_input("Enter the value to add: ", int)
        initial_dict.add(key, value)
        print(f"Added key '{key}' with value '{value}' to the dictionary.")

    elif action_response == "2":
        key = safe_input("Enter the key to remove: ", int)
        if initial_dict.get(key):
            initial_dict.remove(key)
            print(f"Removed key '{key}' from the dictionary.")
        else:
            print(f"Key '{key}' not found in the dictionary.")

    elif action_response == "3":
        key = safe_input("Enter the key to lookup: ", int)
        value = initial_dict.get(key)
        if value:
            print(f"The value for '{key}' is: {value}")
        else:
            print(f"Key '{key}' not found in the dictionary.")

    elif action_response == "4":
        print(f"The dictionary has {len(initial_dict)} elements.")

    elif action_response == "5":
        print(initial_dict)

    elif action_response == "6":
        initial_dict.clear()
        print("Cleared all elements from the dictionary.")

    return initial_dict


class ListDictionary(object):

    def __init__(self):
        """Initializes an empty dictionary."""
        self.items = []

    def __len__(self):
        """Returns the number of items in the dictionary."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the dictionary."""
        return str(self.items)

    def is_empty(self):
        """Returns True if the dictionary is empty, or False otherwise."""
        return len(self.items) == 0

    def add(self, key, value):
        """Adds a key-value pair to the dictionary."""
        for i, (k, v) in enumerate(self.items):
            if k == key:
                self.items[i] = (key, value)
                return
        self.items.append((key, value))

    def remove(self, key):
        """Removes a key-value pair from the dictionary by key."""
        self.items = [(k, v) for k, v in self.items if k != key]

    def get(self, key):
        """Gets the value associated with a key."""
        for k, v in self.items:
            if k == key:
                return v
        return None

    def clear(self):
        """Clears all items from the dictionary."""
        self.items = []
