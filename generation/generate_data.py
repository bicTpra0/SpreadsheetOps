# -------------------------------------------------------------------
# Generate Random Data
# -------------------------------------------------------------------

# Task B: Generate data to test run time of different data structures
# This script generates random data for three columns of different lengths
# and outputs as a text file.

# The data generated is floats only and in 3 different sizes:
# Small: <=1000 rows
# Medium: <=10000 rows
# Large: >10000 rows

# To run script: python generate_data.py <input_size> <min row & column range> <max row & column range> <output file name>

# To run small v medium v large data set: 
# python generate_data.py 1000 0 100 data_small.txt
# python generate_data.py 5000 0 100 data_medium.txt
# python generate_data.py 10000 0 100 data_large.txt

# -------------------------------------------------------------------
import sys
import numpy as np

# Generate random data for the input size
def generate_data(input_size, min_range, max_range):
    '''
    In Task B, we need to generate data for 3 different sizes: small, medium and large.
    The generated data will be used to test the speed of operations for each data structure: array, linked list and csr.

    The purpose of this function is to generate random data for the input size.
    The row and column values are integers and the values are floats.

    @param input_size: the number of rows to generate
    @param min_range: the minimum range of the row and column values
    @param max_range: the maximum range of the row and column values
    '''

    # Check if the inputs are integers.
    try:
        input_size = int(input_size)
        min_range = int(min_range)
        max_range = int(max_range)
    # If not, print error message and exit.
    except ValueError:
        print('Input size must be an integer')
        sys.exit(1)

    # create 3 columns of data, each of size "input_size". Column 1 and 2 are integers and column 3 is floats, rounded to 1 decimal place.
    # Col1 = row, Col2 = column, Col3 = value
    col1 = np.random.randint(low=min_range, high=max_range, size=input_size).astype(int)
    col2 = np.random.randint(low=min_range, high=max_range, size=input_size).astype(int)
    col3 = np.random.uniform(low=-10.0, high=10.0, size=input_size).round(1)
    
    # Create an empty list to store the data
    data = []

    # Append the data to the list, by interating through each element in each column
    for i in range(input_size):
        data.append([col1[i], col2[i], col3[i]])

    return data

if __name__ == '__main__':

    # Check that the correct number of arguments are passed in
    try:
        input_size = sys.argv[1]
        min_range = sys.argv[2]
        min_range = sys.argv[3]
        file_name = sys.argv[4]
        
        # Input the first 3 arguments into the generate_data function
        data = generate_data(sys.argv[1],sys.argv[2],sys.argv[3])

    # If not, print error message and exit.
    except IndexError:
        print('python generate_data.py <input_size> <min row & column range> <max row & column range> <output file name>')
        sys.exit(1)

    # Save all rows and columns from data into a text file called the file name in argument 4.
    with open(file_name, 'w') as f:
        for row in data:
            for col in row:
                f.write(str(col) + ' ')
            f.write('\n')

