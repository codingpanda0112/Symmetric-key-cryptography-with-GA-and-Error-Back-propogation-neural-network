import cv2
import numpy as np
from time import time
import math

def Get_r_values(width,height,l,image):
    R1,R11=0,0
    R2,R22=0,0
    for i in range(width-1):
        for j in range(height-1):
            a=pow(-1,(i+j))*image[i][j]
            b=pow(-1,(i+j+1))*image[i][j]
            R11=R11+a
            R22=R22+b
            #print(R1
    R1=abs(R11//width*l)
    R2=abs(R22//height*l)
    print('r1:',R1,'r2:',R2)
    return R1, R2


def number_gen(seed,iters,l):
    op=seed
    while iters:
        op=(29*seed+13)%l
        seed=op
        iters-=1
    return op



def createvectors(x,l):
    frags_per_row=len(x[0])//l
    vectors=[]
    for dummyvectors in x:
        for i in range(0,frags_per_row):
            vectors.append(dummyvectors[i*l:(i+1)*l])
    return vectors       

def crossover(vector,x,y,l):
    if x<l and y<l:
        coi=x
    else:
        coi=0
    #coiter=(9*x+8*y)%l
    coiter=(3*x+5*y)%l
    
    for j in range(0,2*coiter,2):
        n1=number_gen(coi,j,l)
        n2=number_gen(coi,j+1,l)
        temp=vector[n1]
        vector[n1]=vector[n2]
        vector[n2]=temp
    return vector
def mutate(vector,x,y,l):
    if x<l and y<l:
        mui=y
    else:
        mui=0
    #muiter=(76*x+93*y)%l
    muiter=(5*x+73*y)%l
    #print("muiter",muiter)

    for j in range(0,muiter):
        n1=number_gen(mui,j,l)
        #print("number",n1)
        vector[n1]=255-vector[n1]
    return vector


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
            #bit_array.append(pixel)
            bit_array.append(int(pixel,2))
        joined_bits.append(bit_array)
    #print(joined_bits)
    return joined_bits

def bit_slice_encrypt(Array):
    rows = Array.shape[0]
    cols = Array.shape[1]
    bin_Array=[]
    for i in range(rows):
        subset=[]
        for j in range(cols):
            subset.append(bin(Array[i,j])[2:].zfill(8))
        bin_Array.append(subset)
    sliced=np.array(slice_Matrix(bin_Array))
    encrpyt_rotated=encrpyt_bit_rotation(sliced)
    bit=join_bit(encrpyt_rotated)
    bit = np.array(bit)
    return bit

def bit_slice_decrypt(Array):
    rows = Array.shape[0]
    cols = Array.shape[1]
    bin_Array=[]
    for i in range(rows):
        subset=[]
        for j in range(cols):
            subset.append(bin(Array[i,j])[2:].zfill(8))
        bin_Array.append(subset)
    sliced=np.array(slice_Matrix(bin_Array))
    decrpyt_rotated=decrpyt_bit_rotation(sliced)
    bit=join_bit(decrpyt_rotated)
    bit = np.array(bit)
    return bit

def Algorithm_encrypt(image):
    bitarray=cv2.imread(image,0)
    bitarray=cv2.resize(bitarray,(256,256))

    width=len(bitarray[0])
    height=len(bitarray)

    fragments=1
    frags_per_row=1

    l=width//fragments
    #print("l",l)

    r1,r2=Get_r_values(width,height,l,bitarray)
    #r1,r2=20,30
    vectors=createvectors(bitarray,l)

    for i in range(0,len(vectors)):
        vectors[i]=crossover(vectors[i],r1,r2,l)
        vectors[i]=mutate(vectors[i],r1,r2,l)
        r1+=1
        r2+=1
    

    crypt=np.zeros((height,width))
    count=0

    for i in range(0,len(crypt)):
        dummy=np.append([],vectors[count*frags_per_row:(count+1)*frags_per_row])
        count+=1
        crypt[i]=dummy
    crypt = crypt.astype(int)
    print("before encrypt rotate",crypt)
    crypt = bit_slice_encrypt(crypt) 
    print("after encrypt rotate=",crypt)
    return crypt


def Algorithm_decrypt(bitarray):
    #bitarray=cv2.imread(image,0)
    #bitarray=cv2.resize(bitarray,(256,256))
    print("befpre decrypt rotate",bitarray)
    bitarray = bit_slice_decrypt(bitarray)
    print("after decrypt rotate=",bitarray)
    

    width=len(bitarray[0])
    height=len(bitarray)

    fragments=1
    frags_per_row=1
    l=width//fragments

    r1,r2=Get_r_values(width,height,l,bitarray)
    vectors=createvectors(bitarray,l)

    for i in range(0,len(vectors)):
        vectors[i]=crossover(vectors[i],r1,r2,l)
        vectors[i]=mutate(vectors[i],r1,r2,l)
        r1+=1
        r2+=1
    
    crypt=np.zeros((height,width))
    count=0

    for i in range(0,len(crypt)):
        dummy=np.append([],vectors[count*frags_per_row:(count+1)*frags_per_row])
        count+=1
        crypt[i]=dummy
    crypt = crypt.astype(int)

    print("bits converted to image=",crypt)
    return crypt

def createImage(filename,byte_array):
    cv2.imwrite(filename,byte_array)
    print("Image created!")




if __name__=="__main__":
    
    #print("1.Encrypt \n2.Decrypt")
    #option=int(input("Enter option"))
    imagename=""
    '''#if option==1:
        t1=time()
        imagename=input("Enter name of image:")
        print("Encrypting image...")
        byte_array=Algorithm_encrypt(imagename)
        print("Creating Encrypted image..")
        output="output_e.jpg"
        createImage(output,byte_array)
        t2=time()
        print("Time taken to encrypt:",t2-t1)
    #if option==2:
        t1=time()
        #image=input("Enter name of image to be decrypted:")
        image="output_e.jpg"
        print("Decrypting image...")
        byte_array=Algorithm_decrypt(image)
        print("Creating Decrypted image..")
        output="output_final.jpg"
        createImage(output,byte_array)
        t2=time()
        print("Time taken to decrypt:",t2-t1)'''
    t1=time()
    imagename=input("Enter name of image:")
    #imagename='test1.jpg'
    print("Encrypting image...")
    byte_array=Algorithm_encrypt(imagename)
    print("Creating Encrypted image..")
    output="output_e.jpg"
    createImage(output,byte_array)
    t2=time()
    print("Time taken to encrypt:",t2-t1)
    t1=time()
    #image=input("Enter name of image to be decrypted:")
    image="output_e.jpg"
    print("Decrypting image...")
    byte_array=Algorithm_decrypt(byte_array)
    print("Creating Decrypted image..")
    output="output_final.jpg"
    createImage(output,byte_array)
    t2=time()
    print("Time taken to decrypt:",t2-t1)


