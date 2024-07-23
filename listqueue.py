"""
File: listqueue.py
A list-based implementation of queues.
"""


def queue_actions(initial_queue, action_response):
    if action_response == "1":
        element = safe_input("What element do you want to add? ", int)
        initial_queue.add(element)

    elif action_response == "2":
        initial_queue.pop()

    elif action_response == "3":
        print(f"The queue has {len(initial_queue)} elements.")
    elif action_response == "4":
        print(initial_queue)
    elif action_response == "5":
        initial_queue.clear()

    return initial_queue


class ListQueue(object):

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
        """Returns True if the queue is empty, or False otherwise."""
        return len(self.items) == 0

    def __len__(self):
        """Returns the number of items in the queue."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the queue."""
        temp = str(self.items)[1:-1]
        return "{" + temp + "}"

    def __iter__(self):
        """Supports iteration over a view of the queue."""
        for item in self.items:
            yield item

    def __add__(self, other):
        """Returns a new queue containing the contents
        of self and other."""
        new_queue = self.items
        for item in other:
            new_queue.append(item)
        return ListQueue(new_queue)

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if isinstance(other, ListQueue):
            return self.items == other.items
        return False

    def peek(self):
        """Returns the item at the front of the queue.
        Raises IndexError if queue is not empty."""
        if self.isEmpty():
            raise IndexError("Queue is empty")
        return self.items[0]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items = list()

    def add(self, item):
        """Inserts item at the rear of the queue."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item at the front of the
        queue. Raises IndexError if queue is not empty."""
        if self.isEmpty():
            raise IndexError("Queue is empty")

        old_item = self.items[0]
        self.items.pop(0)

        return old_item


def main():
    lyst = [8, 2, 4, 7, 6, 1]
    print("The list of items added is:", lyst)
    b = ListQueue(lyst)
    print("The queue's size:", len(b))
    print("The queue's string:", b)
    print()

    print("Add 5")
    b.add(5)
    print("The queue's string:", b)
    print()
    print("Peek")
    print("Item at front of the queue:", b.peek())
    print("The queue's string:", b)
    print()
    print("Pop")
    print("Item popped:", b.pop())
    print("The queue's string:", b)
    print()
    print("c = ListQueue(b)")
    c = ListQueue(b)
    print("b == c?", b == c)
    print()
    print("d = ListQueue([1, 2, 3, 4, 5, 6])")
    d = ListQueue([1, 2, 3, 4, 5, 6])
    print("b == d?", b == d)
    print()
    print("e = b + d")
    e = b + d
    print("Queue e's string:", e)
    print("Is e empty?", e.isEmpty())
    e.clear()
    print("Clear e")
    print("Is e empty?", e.isEmpty())
    print("The queue's string:", e)


if __name__ == "__main__":
    main()
