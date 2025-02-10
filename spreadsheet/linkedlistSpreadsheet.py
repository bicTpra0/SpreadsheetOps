from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell

#python3 spreadsheetFilebased.py linkedlist sampleData.txt sampleCommands.in sample.exp

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class Node:
    def __init__(self, Cell):
        self.cell = Cell
        self.row = Cell.row
        self.col = Cell.col
        self.val = Cell.val
        self.next = None
        self.prev = None

    def get_cell(self):
        return self.cell

    def get_row(self):
        return self.row
    
    def get_col(self):
        return self.col
    
    def get_val(self):
        return self.val

    def get_next(self):
        return self.next

    def set_row(self, row):
        self.row = row
    
    def set_col(self, col):
        self.col = col

    def set_next(self, next):
        self.next = next
    
    def set_prev(self, prev):
        self.prev = prev


class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self, rows = 0, cols = 0):

        self.head = None    
        self.tail = None    
        self.length = 0
        self.rows = rows
        self.cols = cols


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """        

        for c in range (0, len(lCells)):
            newNode = Node(lCells[c])

            if not self.head:
                self.head = newNode
                self.tail = newNode
                self.rows = newNode.row + 1
                self.cols = newNode.col + 1

            else:
                newNode.set_next(self.head)
                self.head.set_prev(newNode)
                self.head = newNode
                if newNode.row > self.rows:
                    self.rows = newNode.row + 1
                if newNode.col > self.cols:
                    self.cols = newNode.col + 1


            self.length += 1

        #print(self.length)
        #print("rows = " + str(self.rows))


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """

        if self.head == None:
            return False
        
        #print(self.rows)

        rows = self.rowNum()
        rows += 1
        self.rows = rows
        #print(self.rows)
        return True




    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        if self.head == None:
            return False
        
        cols = self.colNum()
        cols += 1
        self.cols = cols
        #print(self.cols)
        return True
        
        


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  
            If inserting as first row, specify rowIndex to be 0.  
            If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        #get total number of rows in spreadsheet
        numRows = self.rowNum()
        #if the rowindex is greater than the number of rows or less than -1
        if rowIndex >= numRows or rowIndex < -1:
            return False        # invalid index
        
        #the current node is the head of the list
        curr_node = self.tail
        #for all nodes for the length of the list
        for i in range(self.length):
            while curr_node.prev != None:
                if curr_node.get_row() > rowIndex:
                    #get the current node's cell
                    currCell = curr_node.get_cell()
                    #print(currCell)
                    #the current node's cell's row is incremented by one
                    currCell.row = currCell.row + 1
                    #update the node's row to be the cell's row
                    curr_node.set_row(currCell.row)
                    #continue for all nodes
                curr_node = curr_node.prev
                
        
        #do the same for the head node because for some reason it isn't being included in the loop
        curr_node = self.head
        if curr_node.get_row() > rowIndex:
                    #get the current node's cell
            currCell = curr_node.get_cell()
                    #print(currCell)
                    #the current node's cell's row is incremented by one
            currCell.row = currCell.row + 1
                    #update the node's row to be the cell's row
            curr_node.set_row(currCell.row)
        
        #add 1 to the row count
        self.rows += 1

        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """
        #get total number of columns in spreadsheet
        numCols = self.colNum()
        
        #if the colindex is greater than the number of columns or less than -1
        if colIndex >= numCols or colIndex < -1:
            # invalid index
            return False        
        
        #the current node is the head of the list
        curr_node = self.tail
        #for all nodes for the length of the list
        for i in range(self.length): 
            while curr_node.prev != None:
                if curr_node.get_col() > colIndex:
                        #get the current node's cell
                    currCell = curr_node.get_cell()
                        #the current node's cell's column is incremented by one
                    currCell.col = currCell.col + 1
                        #update the node's col to be the cell's col
                    curr_node.set_col(currCell.col)
                    #continue for all nodes
                curr_node = curr_node.prev
        
        #do the same for the head node because for some reason it isn't being included in the loop
        curr_node = self.head
        #print(curr_node.cell)
        if curr_node.get_col() > colIndex:
                        #get the current node's cell
            currCell = curr_node.get_cell()
                        #the current node's cell's column is incremented by one
            currCell.col = currCell.col + 1
                        #update the node's col to be the cell's col
            curr_node.set_col(currCell.col)
        
        #add 1 to the column count
        self.cols += 1
        return True
    


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """
        #if row index is greater than or equal to total rows
        if (rowIndex >= self.rows): 
            #invalid index
            return False
        
        #if colindex is greater than or equal to total cols    
        if (colIndex >= self.cols):
            #invalid index
            return False

        #set current node to start of list
        curr_node = self.head

        #for all nodes in the length of list
        for i in range(self.length):
            #if current node's row is same as row index
            if curr_node.get_row() == rowIndex:
                #if current node's col is same as col index
                if curr_node.get_col() == colIndex:
                    #get the cell of current node
                    curr_cell = curr_node.get_cell()
                    #print(curr_cell)
                    #change the cell's value to update value
                    curr_cell.val = value
                    return True
                #get next node
                #curr_node = curr_node.next
            curr_node = curr_node.next
                
        #if rowIndex and col index aren't already values of cells in list
        #and are also within range of rows and columns
        #create a new cell with given values
        newCell = Cell(rowIndex, colIndex, value)

        #create a new node with the cell as value
        newNode = Node(newCell)
        #print(newCell)

        #add pointer from new node to head node
        newNode.set_next(self.head)
        #change the head node to have pointer to new node at head
        self.head.set_prev(newNode)
        #change head node to be the new node
        self.head = newNode

        self.length += 1

        return True
        


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        ttlRows = self.rows

        return ttlRows



    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        ttlCols = self.cols
        return ttlCols



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        cellLists = []

        curr_node = self.head
        for i in range(self.length):
            if curr_node.get_val() == value:
                cells = list()
                cells.append(curr_node.get_row())
                cells.append(curr_node.get_col())
                cellLists.append(cells)
            curr_node = curr_node.get_next()
        
        return cellLists

        



    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        valueCells = []

        if self.length == 0:
            return []

        curr_node = self.head
        
        while curr_node != None:
            if curr_node.get_val() != None:
                cell = curr_node.get_cell()
                valueCells.append(cell)

            curr_node = curr_node.get_next()
        
        l = len(valueCells)
        
        for i in range(l):
            minindex = i
            minCell = valueCells[minindex]
            for j in range(i+1, l):
                if valueCells[j].row < minCell.row:
                    minindex = j
                    minCell = valueCells[minindex]
                if valueCells[i].row == valueCells[j].row:
                    if valueCells[j].col < valueCells[i].col:
                        minindex = j
                        minCell = valueCells[minindex]
            if minindex != i:
                valueCells[minindex] = valueCells[i]
                valueCells[i] = minCell
        
        return valueCells
