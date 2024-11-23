import sys # Importing sys to use argv for getting command-line arguments
import time 
path = sys.argv[1] 

start_time = time.time()
matrix = []
matrix1 = []

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

def abs_value_is_prime(num):
    return is_prime(abs(num))

def greater_or_equal_one(num):
    return num >= 1

def less_or_equal_neg_eight(num):
    return num <= -8

def abs_is_power_two(num):
    return is_power_of_two(abs(num))

def greater_neg_ten(num):
    return num > -10


# Reading the file and then appending it to a matrix
with open(path, 'r') as file:
    for line in file:
        row = []
        for char in line.strip():
            row.append(char)
        matrix.append(row)
        matrix1.append(row)



len_matrix = len(matrix)

for i in range(100):
    
    for row in range(0, len_matrix):

        for column in range(0, len_matrix):

            cell = matrix[row][column]
            cell_step = matrix1[row][column]

            # Initializing the seven variables that we will need to use for counting the neighbours values
            healthy_o = 0
            weakened_o = 0

            healthy_x = 0
            weakened_x = 0

            dead = 0       
            total = 0   
                    
            for neighbour_row in range(row - 1, row + 2):

                for neighbour_column in range(column - 1 , column + 2):

                    if neighbour_row == row and neighbour_column == column: # Skipping the element itself to only count the neighbours 
                            continue
                    
                    elif is_in_range(matrix, neighbour_row, neighbour_column): # Checking if the index is in the range

                        neighbour = matrix[neighbour_row][neighbour_column]

                        if neighbour == '.':
                            dead += 1

                        elif neighbour == 'O':
                            healthy_o += 1                    

                        elif neighbour == 'o':
                            weakened_o += 1

                        elif neighbour == 'X':
                            healthy_x += 1

                        elif neighbour == 'x':
                            weakened_x += 1

            total = (2 * healthy_o) + weakened_o - (0 * dead) + (-2 * healthy_x) + (-1 * weakened_x)

            # Defining the rules for determining next step of a cell based on its current state and its neighbours
            if cell == 'O':
                if is_power_of_two(total):
                    cell_step = '.'
                
                elif is_less_ten(total):
                    cell_step = 'o'

                else:
                    cell_step = 'O'
            
            elif cell == 'o':
                if less_or_equal_zero(total):
                    cell_step = '.'

                elif greater_or_equal_eight(total):
                    cell_step = 'O'

                else:
                    cell_step = 'o'

            elif cell == '.':
                if is_prime(total):
                    cell_step = 'o'

                elif abs_value_is_prime(total):
                    cell_step = 'x'

                else:
                    cell_step = '.'
            
            elif cell == 'x':
                if greater_or_equal_one(total):
                    cell_step = '.'

                elif less_or_equal_neg_eight(total):
                    cell_step = 'X'
                
                else:
                    cell_step = 'x'

            elif cell == 'X':
                if abs_is_power_two(total):
                    cell_step = '.'

                elif greater_neg_ten(total):
                    cell_step = 'x'

                else:
                    cell_step = 'X'

    temp = matrix1
    matrix1 = matrix
    matrix = temp        


print(len(matrix))



print(time.time() - start_time)