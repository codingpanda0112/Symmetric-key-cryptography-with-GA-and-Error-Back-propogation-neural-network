
def Text_input():
	String=input("Enter the  Plain-text:")
	return String

def Text_ascii(String):
	convertText=''
	for c in String:
		#print(c)
		ascii_value= str(ord(c))
		#print(ascii_value)
		if len(ascii_value)<3:
			pdded_Text='0'*(3-len(ascii_value))+ascii_value

		else:
			pdded_Text=ascii_value
		#print(pdded_Text)
		convertText=convertText+' '+pdded_Text
	return convertText

def Ascii_binary(String):
	
	ascii_array=[]
	bin_array=[]
	print(String)
	for  i in  range(len(String)):
		print(type(i),i)
		print(String[i],'ascii:',ord(String[i]))
		ascii_array.append(ord(String[i]))
		bin_array.append(bin(ascii_array[i])[2:].zfill(8))
		
	return ascii_array,bin_array

string=Text_input()
ct=Text_ascii(string)
#print(ct)
a,b=Ascii_binary(string)
print(a)
print(b)