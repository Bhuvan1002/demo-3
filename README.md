Cafe Ordering System – Python Beginner Project
Overview

This is a simple Python program that simulates a cafe ordering system. It allows users to:

View the menu of drinks or snacks.

Place multiple orders.

Calculate the total price dynamically.

Display a final bill.

This project is designed for Python beginners to learn the basics of:

Python functions

Loops and conditional statements

User input

Reading CSV files with pandas

Basic arithmetic operations

Features
Menu Display

User can choose between drinks and snacks.

The program reads the menu from a CSV file (drinks.csv or snacks.csv) and displays it in a clean, numbered format.

Order Multiple Items

Users can order one or more items from the menu.

The menu is shown each time the user wants to order additional items.

Dynamic Total Calculation

Calculates and updates the total price as the user orders more items.

Final Bill

Displays a summary of the orders and the total amount to pay.

CSV File Format

The menu is stored in CSV files (drinks.csv and snacks.csv)


How to Run

Install pandas if not already installed:
pip install pandas

Make sure the CSV files (drinks.csv and snacks.csv) are in the same folder as the Python script.

Run the Python script:

python main.py

Code Structure

welcome_message()

Displays a welcome message and the selected menu.

Reads the menu from a CSV file.

order(menu)

Takes user orders in a loop.

Updates the total price for multiple items.

Prints a running total and final bill.

main block

Runs the program by calling welcome_message() and order() functions.

Learning Outcomes

By completing this project, beginners will learn:

Reading and processing CSV files using pandas.

Using loops and conditional statements to handle user input.

Working with functions to organize code.

Managing running totals and simple arithmetic in Python.

Handling basic errors such as invalid menu selection.

Future Improvements

Add itemized receipt with all ordered items and quantities.

Allow users to remove items or edit quantities.

Save order history to a file.

Add more categories like desserts or combos.

Conclusion

This simple project is perfect for beginners who want to practice Python basics in a fun and interactive way. It combines user input, data processing, and loops to create a small, real-world application.
