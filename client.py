import socket
import csv
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.53.156.180', 8080))
f = open("myfile.txt","r")
va=f.read()

client.send(va.encode("utf-8"))
from_server = client.recv(4096)

client.close()
print (from_server)
exit(0)