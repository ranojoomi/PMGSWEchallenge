import sys
import pandas as pd
import csv
import os

def get_headers(arguments):

    headers = []
    for file in arguments:
        # check that file is csv, if not skip
        if len(file) < 4 or file[-4:] != '.csv':
            continue

        try:
            with open(file, 'r') as file_reader:
                csv_reader = csv.reader(file_reader)

                # check every element in header line only
                for head in csv_reader:
                    for col in head:
                        if col not in headers:
                            headers.append(col)
                    break
        except FileNotFoundError:
            continue

    return headers

def main(in_files, out_file):

    n = len(in_files)

    # check that we have at least one csv file
    if n < 2:
        sys.stderr.write("Make sure csv files are included\n")
        return 1

    # the chucksize we will buffer into
    size = 1024 * 1024

    headers = get_headers(in_files)
    put_head = True
    
    # iterate through files in command line
    for file in in_files:

        # check that file is csv, if not skip
        if len(file) < 4 or file[-4:] != '.csv':
            continue

        # obtain name of file not including the directory
        index = file.rfind('/')
        file_name = file if index < 0 else file[index + 1:]

        # try opening file, if failure, skip and move on
        try:
            # read from file in chucks
            with pd.read_csv(file, chunksize=size) as reader:
                for chunk in reader:

                    # add new filename column to df
                    chunk['filename'] = file_name

                    # create df with headers so all unique columns are included
                    df_main = pd.DataFrame(columns=headers)

                    # append current chunk to main df
                    df_main = pd.concat([df_main, chunk])

                    # write chunk to stdout 
                    if put_head:
                        df_main.to_csv(out_file, index=False, mode='w', header=put_head, lineterminator='\n')
                    else:
                        df_main.to_csv(out_file, index=False, mode='a', header=put_head, lineterminator='\n')

                    put_head = False

        except FileNotFoundError:
            continue

    return 0

if __name__ == '__main__':
    main()