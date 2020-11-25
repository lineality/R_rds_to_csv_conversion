# Convert rds R database files to csv files (in python)

# Problem(User's): user has an .rds file, but needs .csv
#                   e.g. https://hanlab.uth.edu/HeRA/download
# solution(product): convert an .rds to a .csv

# instructions:
# Run this line in terminal first:
# pipenv install pyreadr
# run with $ rds_to_csv.py
# and follow prompt instructions

import pandas as pd
import pyreadr
import os

FLAG = True

while FLAG == True:

    # This shows the user what files are available,
    # for ease of use:
    print("Here are the files in this directory:\n")
    the_path = "."
    files = os.listdir(the_path)
    for name in files:
        print(name)

    # take the file name as input
    input_rds = input("Name of .rds File to Convert to .csv:\n")

    # Read the R-database file into an Ordered Dictionary
    result = pyreadr.read_r(input_rds)

    # put the data into a pandas dataframe
    df = result[None]

    # output the csv
    df.to_csv(f"{input_rds[:-4]}.csv")

    # Yay!!
    print("All Done!!")

    # ask user if they want another conversion
    choice = input("Convert Another file? y/n")
    if (choice == "y") or (choice == "Y"):
        FLAG = True

    elif (choice == "n") or (choice == "N"):
        FLAG = False

    else:
        choice = input("Come again? Convert Another file? y/n\n")

print("Bye!")