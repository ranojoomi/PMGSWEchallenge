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

    # testing 
    def test_same_cols(self):
        num_rows = 0
        num_cols = 0
        num_rows_combined = 0
        num_cols_combined = 0

        for file in self.files:
            with open(file, 'r') as open_file:
                csv_reader = csv.reader(open_file)
                for line in csv_reader:
                    num_rows += 1
                    num_cols = len(line)

        solution_for_testing.main(self.files, self.out_file)

        with open(self.out_file, 'r') as open_test:
            csv_reader = csv.reader(open_test)
            for line in csv_reader:
                num_rows_combined += 1
                num_cols_combined = len(line)

        self.assertEqual(num_rows, num_rows_combined + (len(self.files) - 1))
        self.assertEqual(num_cols, num_cols_combined - 1)

    
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

        self.assertEqual(num_rows, num_rows_combined + (len(self.files_diff_col) - 1))
        self.assertEqual(len(headers), num_cols_combined - 1)
        

if __name__ == '__main__':
    try:
        os.remove(TestSolution.get_out_file(TestSolution))
    except FileNotFoundError:
        pass
    unittest.main()