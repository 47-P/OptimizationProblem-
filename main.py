import argparse
import os
from multiprocessing import Pool

# Writing the neccessary funtions for the cell_life rule
def is_in_range(matrix, row, column):
    matrix_row = len(matrix)
    matrix_column = len(matrix[0])

    return 0 <= row < matrix_row and 0 <= column < matrix_column 

def is_power_of_two(num):
    powers_of_two = [1, 2, 4, 8, 16]
    return num in powers_of_two

def is_prime(num):
    return num in [2, 3, 5, 7, 11, 13]

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

# Writing the function that applies the rules to a specific given row
def next_step_row(matrix, row_num):
    
    row = []

    row_len = len(matrix[row_num])

    for column in range(row_len):
        cell = matrix[row_num][column]

        # Initializing the seven variables that we will need to use for counting the neighbours values
        healthy_o = weakened_o = healthy_x = weakened_x = dead = 0        
                
        for neighbour_row in range(row_num - 1, row_num + 2):

            for neighbour_column in range(column - 1 , column + 2):

                if neighbour_row == row_num and neighbour_column == column: # Skipping the element itself to only count the neighbours 
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
                row.append('.')
            
            elif is_less_ten(total):
                row.append('o')

            else:
                row.append('O') 
        
        elif cell == 'o':
            if less_or_equal_zero(total):
                row.append('.') 

            elif greater_or_equal_eight(total):
                row.append('O') 

            else:
                row.append('o')

        elif cell == '.':
            if is_prime(total):
                row.append('o')

            elif abs_value_is_prime(total):
                row.append('x') 

            else:
                row.append('.')
        
        elif cell == 'x':
            if greater_or_equal_one(total):
                row.append('.')

            elif less_or_equal_neg_eight(total):
                row.append('X')
            
            else:
                row.append('x')

        elif cell == 'X':
            if abs_is_power_two(total):
                row.append('.')

            elif greater_neg_ten(total):
                row.append('x')

            else:
                row.append('X')


    return row

def process_row(args):
    matrix, row_index = args
    return next_step_row(matrix, row_index)

# Defining a function to call the row function in order to apply the rules to the entire matrix 
def next_step_matrix(matrix, num_processes):
    rows = len(matrix)
    args = [(matrix, row) for row in range(rows)]

    with Pool(processes=num_processes) as pool:
        result_matrix = pool.map(process_row, args) 

    return result_matrix


# Defining the main function to the program
def main():
    parser = argparse.ArgumentParser(description="Cellular Automaton Simulation")
    
    # Input file argument
    parser.add_argument("-i", "--input", type=str, required=True,
                        help="Path to the input file containing the starting cellular matrix")
    
    # Output file argument
    parser.add_argument("-o", "--output", type=str, required=True,
                        help="Path to the output file for storing the final cellular matrix")
    
    # Processes argument
    parser.add_argument("-p", "--processes", type=int, default=1,
                        help="Number of processes to spawn (default: 1)")
    
    args = parser.parse_args()

    print("Project :: 11853193")

    # Validate input file path
    if not os.path.isfile(args.input):
        raise FileNotFoundError(f"Input file '{args.input}' does not exist.")
    
    # Validate output directory
    if not os.path.isfile(args.output):
        print("No output file")

    if args.processes <= 0:
        raise ValueError("The number of processes must be a positive integer greater than 0.")
    
    matrix = []

    
    with open(args.input, 'r') as file:
        for line in file:
            row = list(line.strip())  
            matrix.append(row)

    # Copying matrix 1 
    matrix1 = [row.copy() for row in matrix]

    # Perform 100 iterations
    for _ in range(100):
        matrix1 = next_step_matrix(matrix, args.processes)
        matrix, matrix1 = matrix1, matrix

    # Write the final matrix to the output file
    output_file = open(args.output, "w")
    output_file.write("\n".join("".join(row) for row in matrix))

    output_file.close()

    
# Defining the entry point to the program
if __name__ == "__main__":
    main()