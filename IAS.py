
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


string=Text_input()
ct=Text_ascii(string)
print(ct)