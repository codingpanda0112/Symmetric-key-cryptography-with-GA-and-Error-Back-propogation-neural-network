import random

def Text_input():
	String=input("Enter the  Plain-text:")
	String=String+'\r'+'\n'
	return String

def file_upload(filename):
	string=''
	file = open(filename, "r")
	for line in file:
		for char in line:
			string+=char
	string=string+'\r'+'\n'
	return string		

def Text_ascii(String):
	
	Acii_Array=[]
	convertText=''

	for c in String:
		ascii_value= str(ord(c))

		if len(ascii_value)<3:
			pdded_Text='0'*(3-len(ascii_value))+ascii_value
		else:
			pdded_Text=ascii_value
		
		convertText=convertText+' '+pdded_Text
	return convertText.lstrip()
def Ascii_binary(ascii_array):
	bin_array=[]
	
	for digit in ascii_array:
		#print(bin(ord(digit))[2:].zfill(8))
		bin_array.append(bin(ord(digit))[2:].zfill(8))

	return bin_array

def Ascii_binary_func(String):
	
	ascii_array=[]
	bin_array=[]
	print(String)
	for  i in  range(len(String)):
		ascii_array.append(ord(String[i]))
		bin_array.append(bin(ascii_array[i])[2:].zfill(8))
		
	return ascii_array,bin_array
def split_chunks(array, chunksize,skip_tail=False):
    formated_list = []
    if chunksize <= len(array):
        formated_list.extend([array[:chunksize]])
        formated_list.extend(split_chunks(array[chunksize:], chunksize, skip_tail))
    elif not skip_tail and array:
        formated_list.extend([array])
    return formated_list

def String_Split(bin_array):
	joined=''.join(bin_array)
	print(joined,'Length',len(joined))

	mid=len(joined)//2
	Str1=""
	Str2=""
	String1=[]
	String2=[]
	print(mid)

	for i in range(0,mid):
		#print(bin_array[i])
		Str1+=joined[i]
				
	for j in range(mid,len(joined)):
		Str2+=joined[j]
	String1=split_chunks(Str1,8)
	String2=split_chunks(Str2,8)

	print ('String1=',String1)
	print ('String2=',String2)

	return String1,String2

def Crossover(String1,String2):
	
	indpb = 0.5
	temp = String1
	size = min(len(String1), len(String2))
	for i in range(size):
		for j in range(len(String1[i])):
			if random.random() < indpb:
				#print random.random()
				String1[i] = list(String1[i])
				String2[i] = list(String2[i])
				String1[i][j], String2[i][j] = String2[i][j], String1[i][j]
				String1[i]=''.join(map(str, String1[i]))
				String2[i]=''.join(map(str, String2[i]))
				
	return String1,String2

def mutation(String1,rate):
	number=rate*len(string1)*8
	count=0
	#print('length of string',len(String1))
	while(count<number):
<<<<<<< HEAD
		j=random.randrange(0,len(String1))
		k=random.randrange(0,8)
		if(String1[j][k]==1):
			String1[j][k]=0
		elif (String1[j][k]==0):
			String1[j][k]=1
=======
		#print(count)
		j=random.randrange(0,len(String1))
		#print(j)
		k=random.randrange(0,8)
		#print(k)
		#print('String before mutation=',String1[j])
		if(String1[j][k]=='1'):
			String1[j] = list(String1[j])
			String1[j][k] = 0
			String1[j]=''.join(map(str, String1[j]))
			#print('String after mutation =',String1[j])
		elif (String1[j][k]=='0'):
			String1[j] = list(String1[j])
			String1[j][k] = 1
			String1[j]=''.join(map(str, String1[j]))
			#print('String after mutation =',String1[j])
>>>>>>> 0ac9b0c6324bd5720a2ec608a1dee7dfe7d2d657
		count+=1

	return String1

def combine(String1,String2):
	str1=''.join(String1)
	str2=''.join(String2)
	Str=str1+str2
	combinedlist=split_chunks(Str,8)

	return  combinedlist


#string=Text_input()
string=file_upload("file.txt")
ct=Text_ascii(string)
print(ct)
bin_array=Ascii_binary(ct)
print(bin_array)
#a,b=Ascii_binary_func(string)
#print(a)
#print(b)
string1,string2=String_Split(bin_array)
String1,String2=Crossover(string1,string2)
print( "String1=",String1)
print( "String2=",String2)
combinedlist=combine(String1,String2)
print("combined list=",combinedlist)
string=mutation(combinedlist,30)

mutated_string= mutation(combinedlist,0.20)
print("mutated string")
print(mutated_string)


'''
print("String1")
print(string1)
print("String2")
print(string2)
print("=======================")
print("After Crossover")
String1,String2=Crossover(string1,string2)
print("String1")
print(String1)
print("String2")
print(String2)
print("combined list")
combinedlist=combine(String1,String2)
print(combinedlist)
string=mutation(combinedlist,30)'''

