"""
File: liststack.py
A list-based implementation of stacks.
"""


def stack_actions(initial_stack, action_response):
    if action_response == "1":
        element = safe_input("What element do you want to add? ", int)
        initial_stack.push(element)

    elif action_response == "2":
        initial_stack.pop()

    elif action_response == "3":
        print(f"The stack has {len(initial_stack)} elements.")
    elif action_response == "4":
        print(initial_stack)
    elif action_response == "5":
        initial_stack.clear()

    return initial_stack


class ListStack(object):
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
        """Returns True if the stack is empty, or False otherwise."""
        return len(self.items) == 0

    def __len__(self):
        """Returns the number of items in the stack."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the stack."""
        temp = str(self.items)[1:-1]
        return "{" + temp + "}"

    def __iter__(self):
        """Supports iteration over a view of the stack."""
        for item in self.items:
            yield item

    def __add__(self, other):
        """Returns a new stack containing the contents
        of self and other."""
        new_stack = self.items
        for item in other:
            new_stack.append(item)
        return ListStack(new_stack)

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if isinstance(other, ListStack):
            return self.items == other.items
        return False

    def peek(self):
        """Returns the item at top of the stack.
        Raises IndexError if stack is empty."""
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.items[len(self.items) - 1]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items = list()

    def push(self, item):
        """Inserts item at the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item at top of the stack.
        Raises IndexError if stack is empty."""
        if self.isEmpty():
            raise IndexError("Stack is empty")
        old_item = self.items[len(self.items) - 1]
        self.items.pop()
        return old_item


def main():
    lyst = [8, 2, 4, 7, 6, 1]
    print("The list of items added is:", lyst)
    b = ListStack(lyst)
    print("The stack's size:", len(b))
    print("The stack's string:", b)
    print()

    print("Pop")
    print("Item popped:", b.pop())
    print("The stack's string:", b)
    print()
    print("c = ListStack(b)")

    print("Push 5")
    b.push(5)
    print("The stack's string:", b)
    print()
    print("Item at top:", b.peek())
    print("The stack's string:", b)
    print()

    print("Push 3")
    b.push(3)
    print("The stack's string:", b)
    print()
    print("Item at top:", b.peek())
    print("The stack's string:", b)
    print()

    print("Pop")
    print("Item popped:", b.pop())
    print("The stack's string:", b)
    print()
    print("c = ListStack(b)")

    c = ListStack(b)
    print("b == c?", b == c)
    print()

    print("d = ListStack([1, 2, 3, 4, 5, 6])")
    d = ListStack([1, 2, 3, 4, 5, 6])
    print("b == d?", b == d)
    print()

    print("e = b + d")
    e = b + d
    print("Stack e's string:", e)
    print("Is e empty?", e.isEmpty())
    print()

    e.clear()
    print("Clear e")
    print("Is e empty?", e.isEmpty())
    print("Stack e's string:", e)


if __name__ == "__main__":
    main()
