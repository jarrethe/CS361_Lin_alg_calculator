import os
import numpy

if __name__ == '__main__':
    temp = 1
    while (temp == 1):
        # check if the file is empty every 1 second
        if os.stat("det.txt").st_size != 0:
            # the file is not empty, read the file into an array
            matrix = []
            with open("det.txt", "r") as file:
                for line in file:
                    for word in line.split():
                        matrix.append(int(word))
            # convert to a numpy 2d array
            dim = int(pow(len(matrix), 0.5))
            npmatrix = [[0 for _ in range(dim)] for _ in range(dim)]
            counter = 0
            row = 0
            for i in range(0, len(matrix)):
                if counter == dim:
                    counter = 0
                    row += 1
                npmatrix[row][counter] = matrix[i]
                counter += 1
            # calculate determinant
            det = numpy.linalg.det(npmatrix)
            det = round(det, 3)
            # write to det.txt
            with open("detanswer.txt", "w") as file:
                file.write(str(det))
            