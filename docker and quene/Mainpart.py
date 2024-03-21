#this is main part of project1
# Write an empty function that its input are two matrices (A and B) and its output is the multiplication of A and B (C = A.B)
import numpy as np
import logging
#basic setting of logging
logging.basicConfig(filename='example1.log', filemode='w',
                        level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
def multiply_matrices(A, B):
    if not isinstance(A, list) or not all(isinstance(row, list) for row in A):
        logging.error( "Value error -1: invalid datatype, A is not a matrix")
        #print( "Value error -1: invalid datatype, A is not a matrix")
        return -1
    if not isinstance(B, list) or not all(isinstance(row, list) for row in B):
        logging.error( "Value error -2: invalid datatype, B is not a matrix")
        #print( "Value error -2: invalid datatype, B is not a matrix")
        return -2
    
    if any(len(row) != len(A[0]) for row in A if isinstance(row, list)):
        logging.error("Value error -3: Inconsistent row lengths in input matrix A")
        #print ("Value error -3: Inconsistent row lengths in input matrix A")
        return -3
    if any(len(row) != len(B[0]) for row in B if isinstance(row, list)):
        logging.error("Value error -4: Inconsistent row lengths in input matrix B")
        #print ("Value error -4: Inconsistent row lengths in input matrix B")
        return -4
    
    if len(A) ==0:
        #print( "Value error -5:martix A is empty matrix")
        logging.error( "Value error -5:martix A is empty matrix")
        return -5
    
    if len(B)==0:
        #print( "Value error -6:martix B is empty matrix")
        logging.error("Value error -6:martix B is empty matrix")
        return -6

    if len(A[0]) != len(B):
        logging.error("Value error -7 : Number of columns in A must be equal to number of rows in B")
        #print("Value error -7 : Number of columns in A must be equal to number of rows in B")
        return -7
    
    #print("this example has correct result:")
    logging.info("this example has correct result:")
    C = [[0 for row in range(len(B[0]))] for col in range(len(A))]
    C = np.dot(A,B)
    return C

#notice that C has A row and B column
'''
#now here are some cases in main parts, 
#you can change them into remark status instead of running them if u want
#example one has correct output
print("test example one:")
E = [ [3,3,7] ,[ 2, 1,8] ]
F = [ [2,4] ,[ 5, 6],[9,10] ]
D =  multiply_matrices(E, F)
print(D)

#example two , error since number of columns in A must be equal to number of rows in B
print("test example two:")
H = [ [3,3,7] ,[ 2, 1,8] ]
I = [ [2,4] ,[ 5, 6],[9,10],[11,12] ]
G =  multiply_matrices(H,I)
print(G)

#example three , error since the input is even not a matrice
print("test example three:")
K = "hap"
L = [ [2,4] ,[ 5, 6],[9,10] ]
J =  multiply_matrices(K,L)
print(J)

#example four , error since the for input, not all column have same number element or not all
print("test example four:")
N = [ [3,3,7] ,[ 2, 1,8] ]
O = [ [2,4] ,[ 5],[9,10],[11,12] ]
M =  multiply_matrices(N,O)
print(M)

#example five error since the matrix is empty matrix
print("test example five:")
Q = []
R = [ [2,4] ,[ 5, 6],[9,10]]
P =  multiply_matrices(Q,R)
print(P)
'''