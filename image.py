import base64
import image
import os
import io
#import Image
import numpy as np
from array import array
#with open("hello.jpg", "rb") as imageFile:
'''   str = base64.b64encode(imageFile.read())
    print (str)
with open("img.png", "rb") as image:'''
binary_array=[]
with open("hello.jpg", "rb") as imageFile:
  f = imageFile.read()
  d = bytearray(f)
  b=np.array(d)

  

for c in b :
	print(c)
	binary_array.append(bin(c)[2:])

print(binary_array)
print('size of binary array', len(binary_array))

#image = Image.open(io.BytesIO())
#image.save(savepath)
