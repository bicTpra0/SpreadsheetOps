# -------------------------------------------------------------------
# Generate Scenario Commands
# -------------------------------------------------------------------

# Task B: Generate data to test run time of different data structures
# This file generates random commands for the selected scenario 
# The amount of commands generated is equal to the size of the data

# The commands generated are for the scenarios:
# Insert: Insert Row or Inser Column
# Update: Update the value of the row and column indexes
# Find: Find a value in the spreadsheet

# To run to generate random commands or insert v update v find scenario commands: 
# python3 generate_commands.py <datafile> <scenario> <commandOutputFile>
# <datafile> is the name of the file with the cell data
# <scenario> is insert, update, find, or random
# <commandOutputFile> is the location/file to write the generated commands to

# -------------------------------------------------------------------

import sys
import random
import numpy as np


def generate_commands(data_file, scenario):
        #declared variables to initialise later
        size = 0
        sc = ''
        commands = []

        #count the lines of data to determine size and amount of commands to generate
        with open(data_file, 'r') as df:
            size = len(df.readlines())
        df.close()

        #determine size of data and rcsize is initialised based on a percentage of the file size
        #this is done to generate row and column integers based on the potential number of columns rows in varied data sizes
        #only did particular percentages based on the sizes of data we were testing with, didn't go larger than 20,000
        rcsize = 0
        if size <= 500:
            rcsize = 50
        if size <= 1000 and size > 500:
            rcsize = 65
        if size > 1000 and size <= 5000:
            rcsize = size*0.2
        if size > 5000 and size < 10000:
            rcsize = size*0.02
        if size >= 10000 and size < 20000:
            rcsize = size*0.03
        if size > 20000:
            rcsize = size*0.015

        #generate random commands using all available options.
        if scenario == 'random':
            allcmnds = ["AR", "AC", "IR", "IC", "U", "R", "C", "F", "E"]
            onecols = ["AR", "AC", "R", "C", "E"]
            icir = ["IR", "IC"]
            col1 = np.random.choice(allcmnds, size).astype(str)
            
            for k in range(size):
                if col1[k] == 'F':
                    #generate a random float between -10 and 10 to 1 decimal place
                    col2 = np.random.uniform(low = -10.0, high = 10.0, size = size).round(1)
                if col1[k] == "U":
                    #generate a random int beteween -10 and the size. 
                    #+10% for column/row indexes to ensure possibility of being unable to insert
                    col2 = np.random.randint(low = -10, high = rcsize, size=size).astype(int)
                    col3 = np.random.randint(low = -10, high =  rcsize, size=size).astype(int)
                    #generate a random float between -10 and 10 to 1 decimal place
                    col4 = np.random.uniform(low = -10.0, high = 10.0, size = size).round(1)
                if col1[k] in icir:
                    #generate a random int beteween -3 and the size. 
                    #+10% for column/row indexes to ensure possibility of being unable to insert
                    col2 = np.random.randint(low = -10, high = rcsize, size=size).astype(int)
            #append columns to commands
            for d in range(size):
                if col1[d] == 'IR' or col1[d] == 'IC' or col1[d] == 'F':
                    commands.append([col1[d], col2[d]])
                if col1[d] == 'U':
                    commands.append([col1[d], col2[d], col3[d], col4[d]])
                if col1[d] in onecols:
                    commands.append([col1[d]])
            return commands

        #if scenarios = "insert":
        if scenario == 'insert':
            sc = 'I'
            ins = ["IR", "IC"]
            #randomise IR and IC
            col1 = np.random.choice(ins, size).astype(str)
            #generate a random int beteween -10 and the size. 
            #high as 10% of size for column/row indexes to ensure possibility of being unable to insert
            col2 = np.random.randint(low = -10, high = rcsize, size=size).astype(int)
        
        #if scenarios = "update":
            #U with random int, int, float
        if scenario == 'update':
            sc = 'U'
            col1 = sc
            #generate a random int beteween -10 and the size. 
            #+10% for column/row indexes to ensure possibility of being unable to insert
            col2 = np.random.randint(low = -10, high = rcsize, size=size).astype(int)
            col3 = np.random.randint(low = -10, high = rcsize, size=size).astype(int)
            #generate a random float between -10 and 10 to 1 decimal place
            col4 = np.random.uniform(low = -10.0, high = 10.0, size = size).round(1)
        
        #if scenarios = "find":
            #F and random float
        if scenario == 'find':
            sc = 'F'
            col1 = sc
            #generate a random float between -10 and 10 to 1 decimal place
            col2 = np.random.uniform(low = -10.0, high = 10.0, size = size).round(1)
  
        #check for size of data file
            #generate same number of commands as data size        
        for i in range(size):
            #if scenario is update, commands will have 2 extra columns than insert/find
            if sc == 'U':
                commands.append([col1, col2[i], col3[i], col4[i]])
            else:
                #insert
                if sc == 'I':
                    commands.append([col1[i], col2[i]])
                else:
                    #find
                    if sc == 'F':
                        #find col1 always F
                        commands.append([col1, col2[i]])
        
        #return the generated commands
        return commands



if __name__ == '__main__':
    
    #try to use the input, check arguments
    try:
        data_file = sys.argv[1]
        scenario = sys.argv[2]
        cmnd_file = sys.argv[3]

        commands = generate_commands(sys.argv[1], sys.argv[2])
    # error if incorrect input
    except IndexError:
        print("python3 generate_commands.py <datafile> <scenario> <commandOutputFile>")
        sys.exit(1)
    
    #save the commands to a command text file
    with open(cmnd_file, 'w') as f:
        for row in commands:
            for col in row:
                f.write(str(col) + ' ')
            f.write('\n')
    f.close()


    