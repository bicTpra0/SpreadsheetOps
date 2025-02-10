# SpreadsheetOps

UNI ASSIGNMENT for Algorithms and Analysis
Submitted by JP and VN

Spreadsheet commands with various data structures and algorithms with various input data/scenarios.
Data generation, command generation, and output comparison.

Given files:
  - spreadsheetFilebased.py
  - spreadsheet/cell.py
  - spreadsheet/baseSpreadsheet.py

Files completed:
  - spreadsheet/arraySpreadsheet.py
  - spreadsheet/linkedlistSpreadsheet.py
  - spreadsheet/csrSpreadsheet.py
  - generation/generate_data.py
  - generation/generate_commands.py


to run the test with csr, type (in Linux, use ‘python3’, on Pycharm’s terminal, use ‘python’):
  ```
  python3 spreadsheetFilebased.py csr sampleData.txt sampleCommands.in sample.out
  ```

Then compare sample.out with the provided sample.exp. In Linux, use the diff command:
  ```
  diff sample.out sample.exp
  ```

If nothing is returned then the test is successful. 
If something is returned after running diff then the two files are not the same and the implementation is incorrect.
