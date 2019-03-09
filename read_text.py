f = open("file.txt", "r")
string =""
for x in f:
	print(x)
	for ch in x:
		string+=ch
		print(ch)
print "string=",string
print "*****************************" 

for ch in string:
	print(ord(ch)) 

f = open("file.txt", "r")
print(f.readline()) 
print(f.readline())
