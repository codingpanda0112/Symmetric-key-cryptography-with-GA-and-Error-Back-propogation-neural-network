import pcapkit
import csv

#from cyclic import *
filename=input('Enter the filename :')
extracter=pcapkit.extract(fin=filename,nofile=True,engine='dpkt')
k=1
intermediate_str=''
cipher_text=''
total = ''
for i in extracter.frame:
	
    try:
        
        if i['data']['p']==6:
            #print(i)
            try:
                
                payload=i['data']['data']['data']
                #print("payload=",payload)
                intermediate_str= payload.__str__()
                if intermediate_str!="b''":
                    #print(st)
                    cipher_text=intermediate_str[2:-1]
                    #print("ciphertext obtained from packet",cipher_text)
                    total+=cipher_text
            except:
                pass
    except:
        pass


print("total text=", total)


#file=open('myfile.txt', mode='r')
#String=file.read()
String = total
#print(String)
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
		writer = csv.writer(file, delimiter=',')#, quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for item in bitarray:
			writer.writerow(item)
# call ur cyclic function
#cyclic(int(cipher_text))