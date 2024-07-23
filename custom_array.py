"""
File: custom_array.py
An Array is a restricted list whose clients can use
only [], len, iter, str, insert, remove, clear and clone.
To instantiate, use
<variable> = array(<default capacity>, <optional fill value>)
The fill value is None by default.
"""


def display_info(action_response="9"):
    if action_response == "9":
        print("\nCool! Array is the most famous type of collection.\n\n"
              "Here are some important information:\n"
              "1.	Array represents a sequence of items that can be accessed or replaced at given index positions.\n"
              "2.	Each element of an array is called an item. You can access each item by providing its index.\n"
              "3.	Every array is created with a reasonable default size at program start-up. When the array cannot \n"
              "hold more data, create a new, larger array and transfer the data items from the old array. When the \n"
              "array seems to be wasting memory, decrease its length in a similar manner.\n")

    elif action_response == "1":
        print("\nIn the case of insertion:\n" 
              "1. Check for available space before attempting an insertion and increase the physical size of the \n"
              "array, if necessary, as described earlier.\n"
              "2. Shift the items from the logical end of the array to the target index position down by one. (This \n"
              "process opens a hole for the new item at the target index)\n"
              "3. Assign the new item to the target index position.\n"
              "4. Increment the logical size by one\n")

    elif action_response == "2":
        print("\nIn the case of removing:\n"
              "1. Shift the items from the one following the target index position to the logical end of the array \n" 
              "up by one. This process closes the hole left by the removed item at the target index.\n"
              "2. Decrement the logical size by one"
              "3. Decrease the physical size of the array, if necessary.\n")


def array_actions(initial_array, action_response):
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

    if action_response == "6":
        value = safe_input("Enter the value to search: ", int)
        index = initial_array.search(value)
        if index != -1:
            print(f"Value {value} found at index {index}.")
        else:
            print(f"Value {value} not found in the array.")

    if action_response == "7":
        initial_array.bubble_sort()
        print(f"Sorted array: {initial_array}")

    if action_response == "8":
        filename = safe_input("Enter the filename to save the array: ", int)
        initial_array.save(filename)
        print(f"Array saved to {filename}.")
    elif action_response == "9":
        filename = safe_input("Enter the filename to load the array from: ", int)
        try:
            initial_array = Array.load(filename)
            print(f"Array loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found.")

    return initial_dict


class Array(object):
    """Represents an array."""
    def __init__(self, capacity, fillValue=None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = list()
        self.logicalSize = 0
        # Track the capacity and fill value for adjustments later
        self.capacity = capacity  # default capacity of the array
        self.fillValue = fillValue
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)

    def __getitem__(self, index):
        """Subscript operator for access at index.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self.size():
            raise IndexError("Array index out of bounds")
        return self.items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self.size():
            raise IndexError("Array index out of bounds")
        self.items[index] = newItem

    def size(self):
        """-> The number of items in the array."""
        return self.logicalSize

    def __grow(self):
        """Increases the physical size of the array if necessary."""
        # Double the physical size if no more room for items
        # and add the fillValue to the new cells in the underlying list
        for count in range(len(self)):
            self.items.append(self.fillValue)

    def __shrink(self):
        """Decreases the physical size of the array if necessary."""
        # Shrink the size by half but not below the default capacity
        # and remove those garbage cells from the underlying list
        newSize = max(self.capacity, len(self) // 2)
        for count in range(len(self) - newSize):
            self.items.pop()

    def insert(self, index, newItem):
        """Inserts item at index in the array."""
        if index < 0:
            index = 0
        elif index > self.logicalSize:
            index = self.logicalSize

        if self.logicalSize == self.capacity:
            self.__grow()

        for i in range(self.logicalSize, index, -1):
            self.items[i] = self.items[i - 1]

        self.items[index] = newItem
        self.logicalSize += 1

    def remove(self, index):
        """Removes and returns item at index in the array."""
        try:
            for i in range(index, self.logicalSize - 1):
                self.items[i] = self.items[i + 1]
                self.items[i + 1] = self.fillValue
            self.logicalSize -= 1
        except IndexError:
            print("Array index out of bounds")

        if self.logicalSize < (len(self.items) * 0.25) and len(self.items) >= self.capacity * 2:
            self.__shrink()

    def clear(self):
        """Removes all data items and resets the array to default."""
        self.items = [self.fillValue] * self.capacity
        self.logicalSize = 0

    def clone(self):
        """Creates and returns a clone of this Array object."""
        clonedArray = Array(self.capacity, self.fillValue)
        clonedArray.items = self.items
        clonedArray.logicalSize = self.logicalSize
        return clonedArray

    def search(self, value):
        """Searches for a value and returns its index, or -1 if not found."""
        for index, element in enumerate(self._data):
            if element == value:
                return index
        return -1

    def save(self, filename):
        """Saves the array to a file."""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load(filename):
        """Loads an array from a file."""
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def bubble_sort(self):
        """Sorts the array using bubble sort algorithm."""
        for passnum in range(len(self._data) - 1, 0, -1):
            for i in range(passnum):
                if self._data[i] > self._data[i + 1]:
                    temp = self._data[i]
                    self._data[i] = self._data[i + 1]
                    self._data[i + 1] = temp


def main():
    """Test code for modified Array class."""
    a = Array(5)
    print("Initial array:", a)
    for item in range(4):
        a.insert(0, item)
    print("Insert 3, 2, 1, 0:", a)
    a.insert(1, 77)
    print("Insert 77 at index 1:", a)
    a.insert(2, 88)
    print("Insert 88 at index 2:", a)
    a.insert(15, 10)
    print("Insert 10 at index 15:", a)
    a.insert(-1, 66)
    print("Insert 66 at index -1:", a)
    a.remove(3)
    print("Remove item at index 3:", a)
    for count in range(5):
        a.remove(0)
        print("Remove item at index 0:", a)
    b = a.clone()
    print("clone created:", b)
    b.clear()
    print("clone cleared:", b)


if __name__ == "__main__":
    main()
