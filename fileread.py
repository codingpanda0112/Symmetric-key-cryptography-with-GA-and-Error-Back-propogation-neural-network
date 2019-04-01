import csv
import cv2

file=open('myfile.txt', mode='r')
String=file.read()
print(String)
bitarray=[]
for i in range(0,len(String),16):
	bitarray_sub=[]
	for j in range(0,8):
		bitarray_sub.append(String[i+j])
	bitarray_sub.append(String[i+8:i+16])
	bitarray.append(bitarray_sub)

for item in bitarray:
	print(item)
with open('data12.csv', mode='w') as file:
		writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for item in bitarray:
			writer.writerow(item)

array= cv2.imread("test1.jpg",0)
array=cv2.resize(array,(256,256))
cv2.imwrite("test1.jpg",array)