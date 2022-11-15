# CSV Combiner

This repo is my solution for the CSV Combiner take-home technical assessment. The main solution is located in the file `solution.py` which takes in multiple csv files and combines them into the file specified by `stdout`. 

`solution_for_testing.py` is an almost identical file but instead takes in the file names as a list and outputs to the file given in the argument. This was done to make unit testing easier.

Finally, `test_solution.py` contains all the unit tests for the solution. The test file can be run by itself to test the program or the `solution.py` can be run directly to test with custom csv files

##  Assumptions

* A couple of assumptions were made when writing this script. One was that it was assumed that if the user did not input any csv files in the command line, that the program would exit and print a message to `stderr` reminding the user to enter csv files

* Another assumption was regarding files that do not exist and other file types except for csv files, in this case it was assumed that these files are considered invalid and the script has been written to simply skip over these files and instead process the next file. All given valid files would be processed and combined as required.

* A third assumption was that the given csv file in `stdout` would be either an empty file, or that anything that was already in the file would be overwritten. This makes it so the combined file will only include the given csv files in the command line combined together.

* A final assumption was one regarding different columns. When combining csv files that do not share columns, it was assumed that when a row is added to the combined csv file that does not contain certain columns, that the entry in the combined csv file for that row will just be empty. So the combined csv file contains all unique columns from all csv files and for rows that do not contain any data, it simply leaves it blank.

Thank you for the opportunity and I hope you enjoy reviewing my work!