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

def subtract_second_row_from_the_first(AbI, firstRowNumber, secondRowNumber, columnnumber):#works
    AbI[firstRowNumber,:] -=AbI[secondRowNumber,:]
    return AbI

def findPivot(AbI, columnn_number):
    number_of_Rows = AbI.shape[0]
    result = columnn_number
    for i in range(columnn_number + 1,number_of_Rows):
        if(abs(AbI[result][columnn_number]) < abs(AbI[i][columnn_number])):
            result = i
    return result


if __name__ == '__main__':
    A = np.array([
        [1.0, -1.0, 3.0],
        [2.0, 1.0, 2.0],
        [-2.0, -2.0, 1.0]])


    AbI =  np.concatenate((A, np.eye(A.shape[0])), axis=1)
    print(AbI)
    number_of_columns = A.shape[1]
    number_of_rows =  A.shape[0]
    print("Counting forward run:")
    for i in range(number_of_columns):
        pivot = findPivot(AbI,i)
        if pivot != i:
            print("~")
            print("change the row ", i, " with row ", pivot)
            change_the_rows(AbI, pivot, i)
            print(AbI)

        for j in range(i + 1, number_of_columns, 1):
            multiplicator = AbI[i][i] / AbI[j][i]
            print("~")
            print("multiply the row ", j, " with ", multiplicator)
            multiply_the_row(AbI,j, multiplicator)
            print(AbI)
            print("~")
            print("subtract the row ", i, " from the row", j)
            subtract_second_row_from_the_first(AbI, j, i, i)
            print(AbI)
    print("the result matrix is")
    print(AbI)
    print("Counting back run:")
    for i in reversed(range(number_of_columns)):
        for j in range(i - 1, -1, -1):
            multiplicator = AbI[i][i] / AbI[j][i]
            print("~")
            print("multiply the row ", j, " with ", multiplicator)
            multiply_the_row(AbI,j, multiplicator)
            print(AbI)
            print("~")
            print("subtract the row ", i, " from the row", j)
            subtract_second_row_from_the_first(AbI, j, i, i)
            print(AbI)
    print("the result matrix is")
    print(AbI)
    print("Transforming diagonal to ones")
    for i in range(number_of_columns):
        multiplicator = 1 / AbI[i][i]
        print("~")
        print("multiply the row ", i, " with ", multiplicator)
        multiply_the_row(AbI, i, multiplicator)
        print(AbI)
    print("the result matrix is")
    A_inv = np.zeros((3,3))
    A_inv[:,:] = AbI[:,number_of_columns:]
    print(A_inv)
    product = np.dot(A_inv, A)
    ones_on_diagonal = np.allclose(product, np.eye(A.shape[0]))
    if ones_on_diagonal:
        print("The product of the inverse matrix and A gives a matrix with ones on the diagonal.")
    else:
        print("The product of the inverse matrix and A does not give a matrix with ones on the diagonal.")