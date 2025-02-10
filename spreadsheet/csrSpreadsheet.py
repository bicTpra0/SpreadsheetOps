from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

import math


class CSRSpreadsheet(BaseSpreadsheet):

    def __init__(self, numRows = 0, numCols = 0):
        # TO BE IMPLEMENTED
        #pass
        self.ValA = []
        self.ColA = []
        self.SumA = [0]
        self.numRows = numRows
        self.numCols = numCols


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        for c in range (0, len(lCells)):
            if lCells[c].row > self.numRows:
                self.numRows = lCells[c].row + 1
            if lCells[c].col > self.numCols:
                self.numCols = lCells[c].col + 1

        for row in range(0, (self.numRows + 1)):
            rowSum = 0
            for col in range(0, (self.numCols + 1)):
                for cell in range(0, len(lCells)):
                    curr = lCells[cell]
                    if curr.row == row:
                        if curr.col == col:
                            self.ValA.append(curr.val)
                            self.ColA.append(curr.col)
                            rowSum += curr.val
            #print(rowSum + self.SumA[-1])
            #self.SumA.append(round((rowSum + self.SumA[-1]), 1))                
            self.SumA.append(float('%.2f'%(rowSum + self.SumA[-1])))
                    #SumA.append(rowSum)
        #print(self.SumA)
        #print(len(self.SumA))

                        
                        

    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        self.numRows += 1
        return True
        
        
        

    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        self.numCols += 1
        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  
        If inserting as first row, specify rowIndex to be 0. 
         If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        if (rowIndex < -1) or (rowIndex > self.numRows):
            return False

        #if row index is -1, all rows are moved +1
        #sumA + 1 entry of val 0 at start
        if rowIndex == -1:
            self.SumA.insert(0, 0)

        #if rowIndex is last row, append last SumA element to SumA
        else:
            if rowIndex == self.numRows:
                self.SumA.append(self.SumA[-1])
        
            else:
            #find the rowIndex of sumA and add another sumA value at rowIndex + 1
                for i in range(len(self.SumA)):
                    if i == rowIndex:
                        iVal = self.SumA[i+1]
                        self.SumA.insert(i+1, iVal) 
        
        self.numRows += 1

        return True



    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        #if less than starting index or more than total cols, return false
        if (colIndex < -1) or (colIndex > self.numCols):
            return False
        
        #add column to start, all colA values are increased by 1
        if colIndex == -1:
            for i in range(len(self.ColA)):
                self.ColA[i] += 1

        
        else:
            #find all columns in ColA that are bigger than colIndex and increase them by 1
            for i in range(len(self.ColA)):
                if self.ColA[i] > colIndex:
                    self.ColA[i] += 1

        #if rowIndex is last row, no changes are made except for numCols being increased by 1        
        self.numCols += 1
        return True



    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        if (rowIndex < -1) or (rowIndex >= self.numRows):
            return False

        if (colIndex < -1) or (colIndex >= self.numCols):
            return False
        
        theseRows = self.getRows()

        valIndex = 0
        ci = self.ColA[:]
        vi = self.ValA[:]
        ind = 0
        for i in range(len(theseRows)):
            #if row index is already listed as a row with a value and colindex is in colA,
            if theseRows[i] == rowIndex and self.ColA[i] == colIndex:
                # get the valueindex of the value to update.
                valIndex = i + 1
                self.ValA[valIndex - 1] = value
                break
            else:
                #if rowindex in these rows, row has a value already, but colindex is not in colA, need to add a value and column element and update sumA
                if theseRows[i] == rowIndex and self.ColA[i] != colIndex:
                    self.ColA.insert(i, colIndex)
                    self.ValA.insert(i, value)
                    try:
                        rowVal = self.SumA[i+3]
                        for v in range(len(self.SumA[i+3:])):
                            if self.SumA[v] == rowVal:
                                self.SumA[v] = value+rowVal
                        self.SumA.insert(i+3, (value+rowVal))
                        break
                    except IndexError:
                        rowVal = self.SumA[-1]
                        self.SumA.insert(-1, value+rowVal)
                        break
                    
                else:
                    #if row isn't in theserows
                    #need to add a value to valA at appropriate index, and value at colA at appropriate index
                    if theseRows[i] > rowIndex:
                        
                        #add a row to theseRows before first element bigger than rowIndex
                        theseRows.insert(i, rowIndex)
                        self.ColA.insert(i, colIndex)
                        self.ValA.insert(i, value)
                        self.SumA.insert(i+3, value)
                        break
                    else:
                        if theseRows[-1] < rowIndex:
                            ind = len(theseRows)
                            theseRows.append(rowIndex)
                            self.ColA.append(colIndex)
                            self.ValA.append(value)
                            self.SumA.insert(ind, value)
                            break

        tva = self.ValA.copy()
        self.SumA = [0]
        rs = 0      #row sums
        for r in range(self.numRows + 1):
            for row in theseRows:
                if r == row:
                    rs += tva[0]
                    tva.pop(0)
            self.SumA.append(float('%.2f'%(rs)))

        return True



    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        return self.numRows


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        return self.numCols



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        found = []

        if value not in self.ValA:
            return found
        
        valRows = self.getRows()
        nonNoneCells = []

        size = len(valRows)

        for k in range(len(valRows)):
            thisCell = []
            if self.ValA[k] == value:
                thisCell.append(valRows[k])
                thisCell.append(self.ColA[k])
                thisCell.append(self.ValA[k])
                found.append(thisCell)

        return found




    def entries(self) -> [Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """

        cells = []

        rows = self.getRows()
        #print("rows", rows)

        for i in range(len(rows)):
            newCell = Cell(rows[i], self.ColA[i], self.ValA[i])
            #print(newCell)
            cells.append(newCell)

        return cells


    def getRows(self):
        cellRows = []
        rowMaths = []

        for k in range(len(self.SumA)):
            thisSum = self.SumA[k]
            try:
                if thisSum != self.SumA[k+1]:
                    val = float('%.2f'%(self.SumA[k+1] - thisSum))
                    cellRows.append(k)
                    rowMaths.append(val)
            except:
                break

        allCellRows = []
        values = self.ValA.copy()
        rowCopy = cellRows.copy()
        x = 0

        for v in range(len(values)):    
            temp = []
            #if values at index v equals rowmaths index 0
            try:
                if values[v] == rowMaths[0]:
                    allCellRows.append(rowCopy[0])
                    rowMaths.pop(0)
                    rowCopy.pop(0)
                    x += 1
                else:
                    count = 0
                    if rowMaths[0] != None:
                        for i in range(v, len(values)):
                            temp.append(values[i])
                            count += 1
                            tempSum = sum(temp)
                            ftempSum = float('%.2f'%(tempSum))
                            if ftempSum == rowMaths[0]:
                                x += count
                                for num in range(count):
                                    allCellRows.append(rowCopy[0])
                                rowMaths.pop(0)
                                temp = []
                                rowCopy.pop(0)
                                count = 0
                    else:
                        print("row maths is none")
            except IndexError:
                continue
        
        return allCellRows