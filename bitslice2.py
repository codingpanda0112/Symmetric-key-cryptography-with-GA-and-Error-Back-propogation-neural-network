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

def encrpyt_bit_rotation(Matrix):

    for i in range(len(Matrix)):
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

def decrpyt_bit_rotation(Matrix):

    for i in range(len(Matrix)):
        if i in [0,3,6]:
            rotate90=rotate_Matrix_270(Matrix[i])
            Matrix[i]=rotate90
        elif i in [1,4,7]:
            rotate180=rotate_Matrix_180(Matrix[i])
            Matrix[i]=rotate180
        elif i in [2,5]:
            rotate270=rotate_Matrix_90(Matrix[i])
            Matrix[i]=rotate270
    return Matrix

def join_bit(Matrix):
    Matrix = np.array(Matrix)
    no_of_slices = Matrix.shape[0]
    rows_of_each_slice = Matrix.shape[1]
    
    joined_bits=[]
    for i in range(rows_of_each_slice):
        bit_array=[]
        for j in range(rows_of_each_slice):
            pixel = ''
            for slices in range(no_of_slices):
                pixel+=Matrix[slices,i][j]
            bit_array.append(int(pixel,2))
        joined_bits.append(bit_array)
    print(joined_bits)
    return joined_bits


'''Array=[[160,172],
        [184,196]]'''
Array = np.array([[1, 2, 3, 4], 
          [5, 6, 7, 8],  
          [9, 10, 11, 12],  
          [13, 14, 15, 16]])
rows = Array.shape[0]
cols = Array.shape[1]
bin_Array=[]
for i in range(rows):
	subset=[]
	for j in range(cols):
		subset.append(bin(Array[i,j])[2:].zfill(8))
	bin_Array.append(subset)
print(bin_Array)


sliced=np.array(slice_Matrix(bin_Array))
print("after slicing=",sliced)
print("=====================")

encrpyt_rotated=encrpyt_bit_rotation(sliced)
print("encrypted encrpyt_rotated=",encrpyt_rotated)
print("=====================")

print("encrypted bits after joining=")
bit=join_bit(encrpyt_rotated)

decrpyt_rotated=decrpyt_bit_rotation(sliced)
print("decrypted encrpyt_rotated=",decrpyt_rotated)
print("=====================")

print("decrypted bits after joining=")
bit=join_bit(decrpyt_rotated)

