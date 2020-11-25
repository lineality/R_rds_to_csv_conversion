# (User) Problem
# We know / We have: rds file
# We need / We don't have: csv file
#
# Solution (Product)
#
# https://pypi.org/project/rpy2/
#
# 1.

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

#import rpy2.robjects as robjects

# import pandas as pd
# import pyreadr
import os

# core code to run an r script in python
# https://stackoverflow.com/questions/24544190/calling-r-script-from-python-using-rpy2#24544362
"""
import rpy2.robjects as robjects
r = robjects.r
r['source']('convert.r')
"""

# writes the temporary R scrip
def write_script(doc_name):

    # create file: readme_text
    readme_text = f'df <- readRDS("{doc_name}.rds")\nwrite.csv(df, "{doc_name}.csv")'

    # create, write-to, & save .txt file
    file_to_create1 = open("convert.r", "w")
    file_to_create1.write(readme_text)
    file_to_create1.close()

    pass


# # function to convert to .csv
# def convert(filename):
#     # take the file name as input
#     input_rds = filename

#     # Read the R-database file into an Ordered Dictionary
#     result = pyreadr.read_r(input_rds)

#     # put the data into a pandas dataframe
#     df = result[None]

#     # output the csv
#     df.to_csv(f"{input_rds[:-4]}.csv")

#     r = robjects.r
#     r['source']('convert.r')


progress_counter = 0
print("progress Counter:")

# iterate through all .rds files in directory
the_path = "."
for filename in os.listdir(the_path):

    # check to that it is a .rds
    if filename[-4:] == ".rds":

        doc_name = filename[:-4]

        # write the R script
        write_script(doc_name)

        # run the R script
        # whcih converts the .rds to .csv!
        import subprocess
        retcode = subprocess.call(['/usr/bin/Rscript','convert.r'])

    # show progress:
    progress_counter += 1
    print(progress_counter)


# Yay!!
print("All Done!!")

