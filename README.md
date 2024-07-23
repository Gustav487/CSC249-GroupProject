# CSC249-GroupProject

We are the Smarty Pants group. Our project was created with the objective of explaining concepts on some data structures for the user. Therefore, the project uses more than one data structure: Array, Bag, Stack, and Queue. Our program was designed to work as an interactive game, where the user can choose between the data structures available and learn while making operations.

To make the implementation easier, we decided to leverage the code designed during the CSC-249 Data Structure & Algorithms (2024SU.CSC.249.0001) course under the supervision of Professor Ms. Ying Andrews. During the course, the students used the textbook Fundamentals of Python Data Structures 2nd Edition by Kenneth A. Lambert. The code used for the data structures are the following:

array.py file. That code was created during the 4th week of the course, and the array content can be found in Chapter 4 of the textbook.
The file array was renamed to custom_array.py to avoid conflicting with the pre-built-in Python function: array.
listbag.py file. That code was created during the 4th week of the course, and the bag content can be found in Chapters 5 and 6 of the textbook.
liststack.py file. That code was created during the 7th week of the course, and the stack content can be found in Chapter 7 of the textbook.
listqueue.py file. That code was created during the 7th week of the course, and the queue content can be found in Chapter 8 of the textbook.
listdictionary.py file. This file was created to demonstrate a deeper understanding of the concepts presented in the chapters and textbooks.
By following the approach of the software engineering, following are some of the project requirements that supported us while developing the program:

The program must support the following data structures: array, bag, stack, and queue.
The program should allow the user to decide about which data structures to interact with.
The program should allow the user to customize the data structure.
The program should provide the user with relevant information about the chosen data structure.
The program should provide the user with relevant information about the operations while interacting with the program.
The user should be able to decide when starting or finishing the program.
We introduced a new function called safe_input to handle input validation. This function ensures that user inputs are of the expected type and prompts the user again if an invalid input is provided. Standard input calls have been replaced with safe_input across the project files to enhance input handling and avoid runtime errors due to invalid user inputs.

In main.py, we replaced the input call for the main menu choice with safe_input to ensure the choice is an integer. Loops for handling choices related to lists, arrays, and dictionaries now use safe_input for action responses.

In custom_array.py, the input calls in the array_actions function have been replaced with safe_input to handle inputs for adding, removing, searching, and other actions on the array, ensuring they are integers.

In listdictionary.py, the input calls in the dict_actions function have been replaced with safe_input to handle inputs for actions on the dictionary, ensuring proper handling of user inputs.

This ensures that all user interactions requiring input are robust against invalid data, enhancing the stability and user experience of our application.






