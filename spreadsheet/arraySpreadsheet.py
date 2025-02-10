from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ArraySpreadsheet(BaseSpreadsheet):
    '''
    This class holds all the methods (functions) that are required to be implemented to read and write to a spreadsheet
    based on a 2D array data structure. The class inherits from the BaseSpreadsheet class which reads in the data 
    from the input file and stores it in a list of tuples.
    '''

    def __init__(self):
        self.data = []
        
    # Task A - Implementing the ArraySpreadsheet Class
    def buildSpreadsheet(self, lCells: [Cell]):
        """
        The purpose of this function is to build a spreadsheet from a list of tuples of (row, column, value).
        The function will first find the maximum row and column values in the list of tuples. 
        It creates the max by looping over each row or column and then getting the maximum value, then adding one because
        of the zero-indexing. That is, 1 is added to the maximum row and column values to account for the fact that the array is zero-indexed.

        This function refers to the lCells list where cell refers to an element in lCells 
        and cell.row refers to the row of the element. The same applies to cell.col and cell.val.

        @param lCells: list of cells to be stored
        """

        # Find the maximum row and column values
        max_row = max(cell.row for cell in lCells) + 1
        max_col = max(cell.col for cell in lCells) + 1

        # Creating a 2D array of 'None' values.
        self.data = [[None for i in range(max_col)] for i in range(max_row)]

        # Populate the 2D array with cell values from the lCells list
        for cell in lCells:
            self.data[cell.row][cell.col] = cell.val

    def appendRow(self) -> bool:
        """
        The purpose of this module is to append a new row to the bottom of the spreadsheet.
        The function will first find the number of columns in the first row of the spreadsheet using the len function. 
        It will then loop over each element in new row and create a new row of None values.

        @return True if operation was successful, or False if not.
        """

        try:
            # Get the number of columns in the first row of the spreadsheet
            num_columns = len(self.data[0])
            # Create a new row of None values
            new_row = [None for i in range(num_columns)]
            # Append the new row to the spreadsheet
            self.data.append(new_row)
            return True
        except Exception as e:
            print(f"Error calling appendRow(): {e}")
            return False

    def appendCol(self) -> bool:
        """
        The purpose of this method is to append a new column to the right end of the spreadsheet.
        This method works by looping over each row in the spreadsheet and appending a new value of None values.
        That is, at the end of each row a None value is added, so by the end there is a new column of None values.

        @return True if operation was successful, or False if not.
        """

        try:
            # Append a new column to the spreadsheet
            for row in self.data:
                row.append(None)
            return True
        except Exception as e:
            #print(f"Error calling appendCol(): {e}")
            return False

    def insertRow(self, rowIndex: int) -> bool:
        """
        The purpose of this method is to insert a new row (can be between any existing rows) into the spreadsheet.
        This function allows the user to enter a row in-between an existing row (positive index number) or at the beginning of the spreadsheet (marked as -1).

        This method first checks if the RowIndex is <-1 or > the number of rows in the spreadsheet. If so, it returns false.
        If the RowIndex is valid, the function will take the first row and count the number of columns in the row. This is assigned to 'num_columns'.
        It then creates a new row of 'None' values. This is assigned to 'new_row'.

        If the rowIndex is -1 then insert new row at the beginning of the spreadsheet.
        If the rowIndex is >= 0 then insert new row after (below) the existing row.

        @param rowIndex Index of the existing row that will be after the newly inserted row. If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1. <-- double check with lecturer
        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        # Check if the rowIndex is valid, 
        # i.e. check that rowIndex is not less than -1 or greater than the number of rows plus an additional row in the spreadsheet
        #if rowIndex < -1 or rowIndex > len(self.data)+1: Double check with lecturer which instructions are correct. 
        if rowIndex < -1 or rowIndex > len(self.data):
            return False

        try:
            # Get the number of columns in the first row of the spreadsheet
            num_columns = len(self.data[0])
            
            # Create a new row of zeros eith elements to the length of the number of columns
            new_row = [None for i in range(num_columns)]

            # if rowIndex is >0 then insert new row after (to the right of) the existing row
            if rowIndex >= 0:
                rowInsert = rowIndex +1
                self.data.insert(rowInsert, new_row)

            # if rowIndex is -1 then insert new row at the beginning of the spreadsheet
            else:
                self.data.insert(0, new_row)
            return True
        
        except Exception as e:
            #print(f"Error calling insertRow({rowIndex}): {e}")
            return False

    def insertCol(self, colIndex: int) -> bool:
        """
        This method inserts a new column (can be between any existing columns) into the spreadsheet.
        This method first checks if the colIndex is <-1 or > the number of columns in the spreadsheet. If so, it returns false.
        If the colIndex is valid, the function will take the first row and count the number of columns in the row. This is assigned to 'num_columns'.
        It then creates a new row of 'None' values. This is assigned to 'new_row'.

        If the colIndex is -1 then insert new column at the beginning of the spreadsheet.
        If the colIndex is >= 0 then insert new column after (to the right of) the existing column.

        @param colIndex Index of the existing column that will be after the newly inserted row.  
        If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1. return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """

        if colIndex < -1 or colIndex > len(self.data[0]):
            return False

        try:
            # if colIndex is 0 or more then insert new column of None values after.
            if colIndex >= 0:
                colInsert = colIndex +1
                for row in self.data:
                    row.insert(colInsert, None)
                return True
            # Otherwise insert new column of None values at the beginning of the spreadsheet
            else:
                for row in self.data:
                    row.insert(0, None)
            return True
        
        except Exception as e:
            #print(f"Error calling insertCol({colIndex}): {e}")
            return False

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        This method updates the cell with the input/argument value. 
        It first tries to apply a new value to a row and column index combination. If this is successful, it returns True.
        If the row and column index combination is not valid, it returns False.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.
        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        try:
            self.data[rowIndex][colIndex] = value
            return True
        
        except Exception as e:
            #print(f"Error calling update({rowIndex}, {colIndex}, {value}): {e}")
            return False

    def rowNum(self) -> int:
        """
        This method returns the number of rows in the spreadsheet. It does this by looking at the length of the 2D array.

        @return Number of rows the spreadsheet has.
        """

        # Return the number of rows
        return len(self.data)

    def colNum(self)->int:
        """
        This method returns the number of columns in the data. It does this by looking at the length of the first row in the 2D array (i.e. column length).

        @return Number of column the spreadsheet has.
        """

        # Return the number of columns
        return len(self.data[0])

    def find(self, value: float) -> [(int, int)]:
        """
        This method finds and returns a list of cells that contain the value 'value'.

        It does this by iterating over each row index and row value in the 2D array, then
        within each row it iterates over each column index and column value in the row.
        If the value in the cell matches the input value, it appends the row and column index to the list 'found_cells'.

        @param value value to search for.
        @return List of cells (row, col) that contains the input value.
	    """

        found_cells = []

        for rowIndex, row in enumerate(self.data):
            for colIndex, cell_value in enumerate(row):
                if cell_value == value:
                    found_cells.append((rowIndex, colIndex))

        return found_cells

    def entries(self) -> [Cell]:
        """
        This method returns a list of cells that have values (i.e., all non None cells).
        Similar to the find method, it iterates over each row index and row value in the 2D array, then
        within each row it iterates over each column index and column value in the row.
        If the value in the cell is not None, it appends the row and column index to the list 'found_cells'.

        @return A list of cells that have values (i.e., all non None cells).
        """

        non_empty_cells = []

        for rowIndex, row in enumerate(self.data):
            for colIndex, cell_value in enumerate(row):
                if cell_value is not None:
                    non_empty_cells.append(Cell(rowIndex, colIndex, cell_value))

        return non_empty_cells
