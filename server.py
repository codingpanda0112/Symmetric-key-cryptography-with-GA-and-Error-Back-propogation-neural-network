import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('10.53.11.189', 8080))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        #print(data)
        if not data: break
        from_client += data.decode("utf-8")
        print (from_client)
        #sending_data = "I am SERVER\n"
        #f = open("test.txt","r")
        #contents = f.read()
        #print(contents)
        #conn.send(str.encode(contents))
    conn.close()
    print ('client disconnected')
    break

