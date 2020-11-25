# Convert rds R database files to csv files (in python)

# Problem(User's): user has an .rds folder, but needs .csv in folder
#                   e.g. https://hanlab.uth.edu/HeRA/download
# solution(product): convert all .rds to a .csv

# instructions:
# 1. Run this line in terminal first:
#    $ pipenv install pyreadr
# 2. $ pipenv shell
# 3. run in the directory with
#    $ python3 rds_to_csv_all_folder.py
#
# all in one:
# pipenv install pyreadr ; pipenv shell ; python3 rds_to_csv_all_folder.py

import pandas as pd
import pyreadr
import os

progress_counter = 0

# function to convert to .csv
def convert(filename):
    # take the file name as input
    input_rds = filename

    # Read the R-database file into an Ordered Dictionary
    result = pyreadr.read_r(input_rds)

    # put the data into a pandas dataframe
    df = result[None]

    # output the csv
    df.to_csv(f"{input_rds[:-4]}.csv")


print("progress Counter:")

# iterate through all .rds files in directory
the_path = "."
for filename in os.listdir(the_path):

    # check to that it is a .rds
    if filename[-4:] == ".rds":

        # convert to csv!
        convert(filename)

    # show progress:
    progress_counter += 1
    print(progress_counter)


# Yay!!
print("All Done!!")
