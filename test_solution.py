import unittest
import solution
import solution_for_testing
import csv
import os

class TestSolution(unittest.TestCase):

    # setting up file lists for testing
    files = ['fixtures/clothing.csv', 'fixtures/accessories.csv', 'fixtures/household_cleaners.csv']
    files_diff_col = ['fixtures/clothing.csv', 'fixtures/accessories.csv', 'fixtures/household_cleaners.csv', 'fixtures/random.csv']
    files_one_missing = ['fixtures/clothing.csv', 'fixtures/accessories.csv', 'fixtures/household_cleaners.csv', 
        'fixtures/fileNotFound.csv']

    # output tet file
    out_file = 'combined_test.csv'

    def get_out_file(self):
        return self.out_file

    # testing with no command line arguments
    def test_no_file(self):
        self.assertEqual(1, solution.main())
    
    # testing the get_headers helper function
    def test_get_header(self):
        output = solution.get_headers(self.files_diff_col)
        self.assertEqual(4, len(output))
        self.assertEqual('email_hash', output[0])
        self.assertEqual('category', output[1])
        self.assertEqual('name', output[2])
        self.assertEqual('age', output[3])
    
    # testing get_header correctly ignores files that do not exist
    def test_get_header_wrongFile(self):
        output = solution.get_headers(self.files_one_missing)
        self.assertEqual(2, len(output))
        self.assertEqual('email_hash', output[0])
        self.assertEqual('category', output[1])

    # testing combining csv with same columns
    def test_same_cols(self):
        num_rows = 0
        num_cols = 0
        num_rows_combined = 0
        num_cols_combined = 0
        all_rows = []

        for file in self.files:
            header = True
            with open(file, 'r') as open_file:
                csv_reader = csv.reader(open_file)
                for line in csv_reader:
                    num_rows += 1
                    num_cols = len(line)
                    if not header:
                        # adding all non header rows to list
                        all_rows.append(line)
                    
                    header = False 

        solution_for_testing.main(self.files, self.out_file)

        header = True
        with open(self.out_file, 'r') as open_test:
            csv_reader = csv.reader(open_test)
            for i, line in enumerate(csv_reader):
                num_rows_combined += 1
                num_cols_combined = len(line)
                if not header:
                    line.pop()
                    # making sure our data that we have written matches with the original csv files
                    self.assertEqual(all_rows[i-1], line)
                header = False

        # asserting that column and rows sizes are correct (adjusted numbers to account for headers)
        self.assertEqual(num_rows, num_rows_combined + (len(self.files) - 1))
        self.assertEqual(num_cols, num_cols_combined - 1)

    # test for combining csv files with different columns
    def test_with_diff_columns(self):
        num_rows = 0
        num_rows_combined = 0
        num_cols_combined = 0

        headers = solution.get_headers(self.files_diff_col)

        for file in self.files_diff_col:
            with open(file, 'r') as open_file:
                csv_reader = csv.reader(open_file)
                for line in csv_reader:
                    num_rows += 1

        solution_for_testing.main(self.files_diff_col, self.out_file)

        with open(self.out_file, 'r') as open_test:
            csv_reader = csv.reader(open_test)
            for line in csv_reader:
                num_rows_combined += 1
                num_cols_combined = len(line)

        # asserting that number of rows and columns is equal to the original csv files
        self.assertEqual(num_rows, num_rows_combined + (len(self.files_diff_col) - 1))
        self.assertEqual(len(headers), num_cols_combined - 1)
        

if __name__ == '__main__':
    try:
        os.remove(TestSolution.get_out_file(TestSolution))
    except FileNotFoundError:
        pass
    unittest.main()