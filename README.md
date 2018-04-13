SUDOKU SOLVER: Backtracking Algorithm Using Python
--------------
INPUT: A 2D array of 9 1D arrays, each of which have 9 elements. Each element represented a number on the board, with 0 acting as placeholders for an unsolved number.

OUTPUT: A solved, formatted sudoku puzzle.

EXAMPLE (Python 2.7, "solver2.7"):

```
Welcome! Input a Sudoku grid following the format given in the readme.md file >>> [[5,1,7,6,0,0,0,3,4],
[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],
[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]

Below is the solved Sudoku puzzle:

 5  1  7 | 6  9  8 | 2  3  4 |
 2  8  9 | 1  3  4 | 7  5  6 |
 3  4  6 | 2  7  5 | 8  9  1 |
______________________________
 6  7  2 | 8  4  9 | 3  1  5 |	
 1  3  8 | 5  2  6 | 9  4  7 |	
 9  5  4 | 7  1  3 | 6  8  2 |
______________________________
 4  9  5 | 3  6  2 | 1  7  8 |	
 7  2  3 | 4  8  1 | 5  6  9 |	
 8  6  1 | 9  5  7 | 4  2  3 |
 ```
