import sys # Importing sys to use argv for getting command-line arguments
import time 
path = sys.argv[1] 

matrix = []
martix1 = []

# Function to check if the index is within the matrix
def is_in_range(matrix, row, column):
    matrix_row = len(matrix)
    matrix_column = len(matrix[0])

    return 0 <= row < matrix_row and 0 <= column < matrix_column 

def is_power_of_two(num):
    powers_of_two = [1, 2, 4, 8, 16]
    return num in powers_of_two

def is_prime(num):
    if num > 1:

        for i in range(2, (num//2) + 1):
            if (num % i) == 0:
                return False
        return True
    return False

def is_less_ten(num):
    return num < 10

def less_or_equal_zero(num):
    return num <= 0

def greater_or_equal_eight(num):
    return num >= 8

  
# Reading the file and then appending it to a matrix
with open(path, 'r') as file:
    for line in file:
        row = []
        for char in line.strip():
            row.append(char)
        matrix.append(row)



len_matrix = len(matrix)

for row in range(0, len_matrix):
    
    for column in range(0, len_matrix):

        # Initializing the seven variables that we will need to use next
        healthy_o = 0
        weakened_o = 0

        healthy_x = 0
        weakened_x = 0

        dead = 0       
        total = 0   
                
        for neighbour_row in range(row - 1, row + 2):
            matrix1_row = []
            for neighbour_column in range(column - 1 , column + 2):

                if neighbour_row == row and neighbour_column == column: # Skipping the element itself to only count the neighbours 
                        continue
                  
                if is_in_range(matrix, neighbour_row, neighbour_column): # Checking if the index is in the range

                    if matrix[neighbour_row][neighbour_column] == '.':
                        dead += 1

                    elif matrix[neighbour_row][neighbour_column] == 'O':
                        healthy_o += 1                    

                    elif matrix[neighbour_row][neighbour_column] == 'o':
                        weakened_o += 1

                    elif matrix[neighbour_row][neighbour_column] == 'X':
                        healthy_x += 1

                    elif matrix[neighbour_row][neighbour_column] == 'x':
                        weakened_x += 1

                    total = (2 * healthy_o) + weakened_o - (0 * dead) + (-2 * healthy_x) + (-1 * weakened_x)    

                    