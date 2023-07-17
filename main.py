import time
import math


"""Name: display_matrix
   Description: Allows user to see original matrix
   Input: Takes a matrix represented as a 1D array
   Output: Outputs the matrix in matrix form"""

def display_matrix(matrix):
    dim = math.sqrt(len(matrix) / 2)
    counter = 0
    print(' ')
    for i in range(len(matrix)):
        if counter == dim:
            counter = 0
            print(" ")
        if i % 2 == 0:
            print(matrix[i] + " ", end="")
            counter += 1
    print(' ')

"""Name: make_matrix
   Description: Allows user to create a new matrix
   Input: Takes an empty string as an input
   Output: Returns the completed matrix"""

def make_matrix(matrix):
    # get the dimension of matrix the user wants
    dimension = input('What dimension matrix do you want? ')
    dim = int(dimension)
    # create the matrix as a 1-d array
    matrix = ""
    for i in range(1, dim + 1):
        for j in range(1, dim + 1):
            matrix += (input("Value for row " + str(i) +
                       " column " + str(j) + ": ") + " ")
    return matrix


if __name__ == '__main__':
    print('Welcome to the matrix calculator')
    # create the matrix as a 1-d array
    matrix = ""
    matrix = make_matrix(matrix)

    # find out what the user wants to do, initialize loop that will repeat
    # until the user quits
    option = 100
    display_matrix(matrix)
    while (option != 5):

        option = int(input(
            "(1) Calculate determinant\n(2) Row Reduce Matrix \n(3) Print Original Matrix\n(4) Make a new matrix\n(5) Quit\n"))
        # if user wants to calculate determinant, write the matrix in det.txt,
        # read the value written in det.txt afterwards
        if option == 1:
            with open("det.txt", "w") as file:
                file.write(matrix)
            time.sleep(1)
            # read the determinant
            with open("detanswer.txt", "r") as file:
                print("\n" + file.read() + "\n")
            # empty the file
            open("det.txt", "w").close()
            open("detanswer.txt", "w").close()

        # display the rref of the matrix
        if option == 2:
            with open("rref.txt", "w") as file:
                file.write(matrix)
            time.sleep(5)
            # read the determinant
            with open("rrefanswer.txt", "r") as file:
                print("\n" + file.read() + "\n")
            # empty the files
            open("rref.txt", "w").close()
            open("rrefanswer.txt", "w").close()

        # display the original matrix
        if option == 3:
            display_matrix(matrix)

        # create a new matrix
        if option == 4:
            matrix = ""
            matrix = make_matrix(matrix)
            display_matrix(matrix)

        # quit
        if option == 5:
            print("\ncome back soon!")
