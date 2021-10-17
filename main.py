# from CSVReader import CSVReader
from SmartJunction import SmartJunction


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Build the smart junction by reading the csv file
# The csv file hold data about all lanes in our junction
def run():
    junction = SmartJunction()
    csv_file = input("Please enter csv file: ")
    junction.build_junction(csv_file)
    # "csv_May_files/Evening_weekend_05_2018.csv"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
