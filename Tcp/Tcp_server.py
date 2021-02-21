import socket

def main():
    host = '127.0.0.1'
    port = 4000
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    c, address = s.accept()
    print("Connection From:" +str(address))
    
    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print(address, data)
        data = data.upper()
        print("Sending Back To:-"+ address)
        c.send(data.encode('utf-8'))
    c.close()
    
if __name__ ==  "__main__":
    main()
