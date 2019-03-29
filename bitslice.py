import numpy as np
import math

def rotate_Matrix_90(Matrix): 
    N=len(Matrix)
    for x in range(0, int(N/2)): 

        for y in range(x, N-x-1):
            # store current cell in temp variable 
            temp = Matrix[x][y]  
            Matrix[x][y] = Matrix[y][N-1-x] 
            Matrix[y][N-1-x] = Matrix[N-1-x][N-1-y] 
            Matrix[N-1-x][N-1-y] = Matrix[N-1-y][x] 
            Matrix[N-1-y][x] = temp 
    return Matrix
  
# Function to print the Matrix 
def printMatrix(Matrix): 
    N = len(Matrix[0]) 
    for i in range(N): 
        print(Matrix[i]) 

def reshape(Matrix):
    n=int(math.sqrt(len(Matrix)))
    Matrix = np.array( Matrix ).reshape((n,n))    
    return Matrix

def rotate_Matrix_180(Matrix):
    #90_rotate=[]
    rotate=rotate_Matrix_90(Matrix)
    rotate=rotate_Matrix_90(rotate)
    return rotate

def rotate_Matrix_270(Matrix):
    rotate=rotate_Matrix_90(Matrix)
    rotate=rotate_Matrix_90(rotate)
    rotate=rotate_Matrix_90(rotate)
    return rotate

def slice_Matrix(Matrix):
    slice1=[]
    slice2=[]
    slice3=[]
    slice4=[]
    slice5=[]
    slice6=[]
    slice7=[]
    slice8=[]
    Slice=[]

    n=int(math.sqrt(len(Matrix)))
    for row in Matrix:
        for item in row:
            slice1.append(item[0])
            slice2.append(item[1])
            slice3.append(item[2])
            slice4.append(item[3])
            slice5.append(item[4])
            slice6.append(item[5])
            slice7.append(item[6])
            slice8.append(item[7])

    slice1=reshape(slice1)
    Slice.append(slice1)
    slice2=reshape(slice2)
    Slice.append(slice2)
    slice3=reshape(slice3)
    Slice.append(slice3)
    slice4=reshape(slice4)
    Slice.append(slice4)
    slice5=reshape(slice5)
    Slice.append(slice5)
    slice6=reshape(slice6)
    Slice.append(slice6)
    slice7=reshape(slice7)
    Slice.append(slice7)
    slice8=reshape(slice8)
    Slice.append(slice8)
    return Slice
def bit_rotation(Matrix):
    lenght=len(Matrix)

    for i in range(lenght):
        if i in [0,3,6]:
            rotate90=rotate_Matrix_90(Matrix[i])
            Matrix[i]=rotate90
        elif i in [1,4,7]:
            rotate180=rotate_Matrix_180(Matrix[i])
            Matrix[i]=rotate180
        elif i in [2,5]:
            rotate270=rotate_Matrix_270(Matrix[i])
            Matrix[i]=rotate270
    return Matrix
def join_bit(Matrix):
    bitarray=[]
    Matrix_f=[]
    n=pow(len(Matrix[0]),2)

    for i in range(len(Matrix)):
        Matrix[i]=Matrix[i].reshape(1,n)
        Matrix_f.append(Matrix[i][0])
    for item in Matrix_f:
        print(item)


    for i in range(0,len(Matrix_f[0])):
        Str=''
        for j in range(len(Matrix_f)):
            #print("matrix[i][j",Matrix_f[j][i])
            Str+=str(Matrix_f[j][i])
        print(Str)
        bitarray.append(int(Str,2))
    print(bitarray)
    return bitarray

            
# Driver code 
Array = [[1, 2, 3, 4], 
          [5, 6, 7, 8],  
          [9, 10, 11, 12],  
          [13, 14, 15, 16]] 
#rotate_Matrix(Matrix) 
#printMatrix(Matrix) 

#Array=[[160,172],
#        [184,196]]
bin_Array=[]

for row in Array:
    subset=[]
    for element in row:
        print(element)
        subset.append(bin(element)[2:])
        #print(subset)
    bin_Array.append(subset)

print(bin_Array)

sliced=slice_Matrix(bin_Array)

for slices in sliced:
    print(slices)
print("=====================")

rotated=bit_rotation(sliced)
for slices in rotated:
    print(slices)
bit=join_bit(rotated)
