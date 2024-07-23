"""
File: listbag.py
A list-based implementation of bags
"""


def bag_actions(initial_bag, action_response):
    if action_response == "1":
        element = safe_input("What element do you want to add? ", int)
        initial_bag.add(element)

    elif action_response == "2":
        element = safe_input("What element do you want to remove? ", int)
        initial_bag.remove(element)

    elif action_response == "3":
        print(f"The bag has {len(initial_bag)} elements.")
    elif action_response == "4":
        print(initial_bag)
    elif action_response == "5":
        initial_bag.clear()

    return initial_bag


class ListBag(object):

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = list()

        if sourceCollection:
            for item in sourceCollection:
                self.items.append(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if the bag is empty, or False otherwise."""
        return len(self.items) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of self."""
        temp = str(self.items)[1:-1]
        return "{" + temp + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        for item in self.items:
            yield item

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        new_bag = self.items
        for item in other:
            new_bag.append(item)
        return ListBag(new_bag)

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if isinstance(other, ListBag):
            return self.items == other.items
        return False

    def count(self, item):
        """Returns the number of instances of item in self."""
        return self.items.count(item)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items = list()

    def add(self, item):
        """Adds item to self."""
        self.items.append(item)

    def remove(self, item):
        """Remove item from self.
        Raises KeyError if item is not in self."""
        try:
            self.items.remove(item)
        except ValueError:
            return f"{item} is not in bag."


def main():
    lyst = list(range(1, 11))
    print("The list of items added:", lyst)
    b = ListBag(lyst)
    print("The bag's size:", len(b))
    print("The bag's string:", b)
    print("The bag is empty:", b.isEmpty())
    print("4 is in the bag:", 4 in b)
    print("0 is in the bag:", 0 in b)
    b.add(7)
    print("Add 7 in bag")
    print("The bag's string:", b)
    b.remove(10)
    print("Remove 10 from bag")
    print("The bag's string:", b)
    print("How many instances of 7?", b.count(7))
    c = ListBag(b)
    print("c = ListBag(b)")
    print("b == c?", b == c)
    d = ListBag([22, 4])
    print("d = ListBag(22, 4)")
    print("b == d?", b == d)
    e = b + d
    print("e = b + d")
    print("bag e's string:", e)
    c.clear()
    print("c.clear()")
    print("bag c's string:", c)


if __name__ == "__main__":
    main()
