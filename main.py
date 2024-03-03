import numpy as np


def print_hi(name):
    print(f'Hi, {name}')

#Define ERU
def multiply_the_row(AbI, rowNumber, multiplicator):#works
    AbI[rowNumber,:] *=  multiplicator
    return AbI

def change_the_rows(AbI, firstRowNumber, secondRowNumber):#works
    array_size = (1, AbI.shape[1])
    temp = np.zeros(array_size)
    temp[0,:] = AbI[firstRowNumber,:]
    AbI[firstRowNumber,:] = AbI[secondRowNumber,:]
    AbI[secondRowNumber,:] = temp[:]

    return AbI

def subtract_second_row_from_the_first(AbI, firstRowNumber, secondRowNumber):#works
    AbI[firstRowNumber,:] -=AbI[secondRowNumber,:]
    return AbI


if __name__ == '__main__':
    A = np.array([
        [1.0, -1.0, 3.0],
        [2.0, 1.0, 2.0],
        [-2.0, -2.0, 1.0]])
    # A_inv = np.linalg.inv(A)
    # print(A.shape)

    AbI =  np.concatenate((A, np.eye(A.shape[0])), axis=1)
    print(AbI)


    # product = np.dot(A_inv, A)
    # ones_on_diagonal = np.allclose(product, np.eye(A.shape[0]))
    # print("Inverse of A:")
    # print(A_inv)
    # if ones_on_diagonal:
    #     print("The product of the inverse matrix and A gives a matrix with ones on the diagonal.")
    # else:
    #     print("The product of the inverse matrix and A does not give a matrix with ones on the diagonal.")