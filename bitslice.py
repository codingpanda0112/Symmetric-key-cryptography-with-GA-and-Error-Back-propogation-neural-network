import numpy as np
import math
def rotate_matrix(Matrix): 
    N = len(Matrix[0]) 
    for i in range(N // 2): 
        for j in range(i, N - i - 1): 
            temp = Matrix[i][j] 
            Matrix[i][j] = Matrix[N - 1 - j][i] 
            Matrix[N - 1 - j][i] = Matrix[N - 1 - i][N - 1 - j] 
            Matrix[N - 1 - i][N - 1 - j] = Matrix[j][N - 1 - i] 
            Matrix[j][N - 1 - i] = temp 
  
# Function to print the matrix 
def printMatrix(Matrix): 
    N = len(Matrix[0]) 
    for i in range(N): 
        print(Matrix[i]) 

def reshape(matrix):
    n=int(math.sqrt(len(matrix)))
    matrix = np.array( matrix ).reshape((n,n))    
    return matrix


def slice_matrix(matrix):
    slice1=[]
    slice2=[]
    slice3=[]
    slice4=[]
    slice5=[]
    slice6=[]
    slice7=[]
    slice8=[]

    n=int(math.sqrt(len(matrix)))
    s = [[0 for j in range(n) ] for i in range(n)] 
    for i in range(0,n):
        for j in range(0,n):
            for k in range(len(matrix)):
                s[i][j][k]=

    slices=[[],[],[],[],[],]
    for row in matrix:
        for item in row:
            slice1.append(item[0])
            slice2.append(item[1])
            slice3.append(item[2])
            slice4.append(item[3])
    slice1=reshape(slice1)
    slice2=reshape(slice2)
    slice3=reshape(slice3)
    print(slice1)
    print(slice2)
    print
            
# Driver code 
Matrix = [[1, 2, 3, 4], 
          [5, 6, 7, 8],  
          [9, 10, 11, 12],  
          [13, 14, 15, 16]] 
#rotate_matrix(Matrix) 
#printMatrix(Matrix) 

Array=[[160,172],
        [184,196]]
bin_Array=[]

for row in Array:
    subset=[]
    for element in row:
        print(element)
        subset.append(bin(element)[2:])
        #print(subset)
    bin_Array.append(subset)

print(bin_Array)

slice_matrix(bin_Array)

