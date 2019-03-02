
def Text_input():
	String=input("Enter the  Plain-text:")
	return String
def Text_ascii(String):
	convertText=' '.join(str(ord(c)) for c in String)
	return convertText


string=Text_input()
ct=Text_ascii(string)
print(ct)