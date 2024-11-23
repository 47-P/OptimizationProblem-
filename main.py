import sys # Importing sys to use argv for getting command-line arguments
import time 
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Cellular Automaton Simulation")
    
    # Input file argument
    parser.add_argument('-i', '--input', type=str, required=True,
                        help="Path to the input file containing the starting cellular matrix")
    
    # Output file argument
    parser.add_argument('-o', '--output', type=str, required=True,
                        help="Path to the output file for storing the final cellular matrix")
    
    # Processes argument
    parser.add_argument('-p', '--processes', type=int, default=1,
                        help="Number of processes to spawn (default: 1)")
    
    args = parser.parse_args()
    
    # Validate input file path
    if not os.path.isfile(args.input):
        raise FileNotFoundError(f"Input file '{args.input}' does not exist.")
    
    # Validate output directory
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        raise FileNotFoundError(f"Output directory '{output_dir}' does not exist.")
    
    # Validate processes
    if args.processes <= 0:
        raise ValueError("The number of processes must be a positive integer greater than 0.")
    
    return args

# Function to check if the index is within the matrix
def is_in_range(row, column):
    matrix_row = 6
    matrix_column = 6

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

def main():

    args = parse_arguments()
    input_path = args.input
    output_path = args.output
    processes = args.processes

    start_time = time.time()
    matrix = []
    matrix1 = []

    # Reading the file and then appending it to a matrix
    with open(input_path, 'r') as file:
        for line in file:
            row = []
            for char in line.strip():
                row.append(char)
            matrix.append(row)
            matrix1 = [row.copy() for row in matrix]



    len_matrix = len(matrix)

    for i in range(99):

        for row in range(0, len_matrix):

            for column in range(0, len_matrix):

                cell = matrix[row][column]

                # Initializing the seven variables that we will need to use for counting the neighbours values
                healthy_o = weakened_o = healthy_x = weakened_x = dead = 0        
                        
                for neighbour_row in range(row - 1, row + 2):

                    for neighbour_column in range(column - 1 , column + 2):

                        if neighbour_row == row and neighbour_column == column: # Skipping the element itself to only count the neighbours 
                                continue
                        
                        elif is_in_range(neighbour_row, neighbour_column): # Checking if the index is in the range

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
                        matrix1[row][column] = '.'
                    
                    elif is_less_ten(total):
                        matrix1[row][column] = 'o'

                    else:
                        matrix1[row][column] = 'O'
                
                elif cell == 'o':
                    if less_or_equal_zero(total):
                        matrix1[row][column] = '.'

                    elif greater_or_equal_eight(total):
                        matrix1[row][column] = 'O'

                    else:
                        matrix1[row][column] = 'o'

                elif cell == '.':
                    if is_prime(total):
                        matrix1[row][column] = 'o'

                    elif abs_value_is_prime(total):
                        matrix1[row][column] = 'x'

                    else:
                        matrix1[row][column] = '.'
                
                elif cell == 'x':
                    if greater_or_equal_one(total):
                        matrix1[row][column] = '.'

                    elif less_or_equal_neg_eight(total):
                        matrix1[row][column] = 'X'
                    
                    else:
                        matrix1[row][column] = 'x'

                elif cell == 'X':
                    if abs_is_power_two(total):
                        matrix1[row][column] = '.'

                    elif greater_neg_ten(total):
                        matrix1[row][column] = 'x'

                    else:
                        matrix1[row][column] = 'X'

        matrix, matrix1 = matrix1, matrix

    for row in matrix:
        print("".join(row))

    with open(output_path, 'w') as file:
        for row in matrix:
            file.write("".join(row) + '\n')

    print(time.time() - start_time)


if __name__ == "__main__":
    main()