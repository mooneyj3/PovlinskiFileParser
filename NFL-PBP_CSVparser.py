##
# This is a simple file parser to convert the spreadsheets from Bryan Povlinski to a format I need
# https://www.spreadsheetsports.com/free-tools/2013-nfl-play-play-data-excel/
##

import csv
import os

# on macbook:  /Users/J-moneyham/NFLData
src_dir = input('Source Directory: ')
if not (os.path.isdir(src_dir)):
    print('source directory not found')
    exit()

# on macbook:  /Users/J-moneyham/NFLData/output
dest_dir = input('Destination Directory: ')
if not (os.path.isdir(dest_dir)):
    print('destination directory not found')
    exit()

## File names follow this format:
# 2013 NFL Play-by-Play Data.csv

start_year = 2013
end_year = 2016
in_filetail = " NFL Play-by-Play Data.csv"
out_filetail = " NFL PbP Data Processed.csv"

curr_yr = start_year
while (curr_yr <= end_year):
    in_filename = str(curr_yr) + in_filetail
    out_filename = str(curr_yr) + out_filetail

    in_path = os.path.join(src_dir, in_filename)
    out_path = os.path.join(dest_dir, out_filename)

    if not (os.path.isfile(in_path)):
        print('Could not find: ' + in_filename)
        curr_yr += 1
        continue

    if (os.path.isfile(out_path)):
        print(str(curr_yr) + ' has existing output file, no processing done for this year.')
        curr_yr += 1
        continue



    curr_yr += 1






