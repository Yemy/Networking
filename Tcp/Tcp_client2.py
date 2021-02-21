import socket

def main():
    host = '127.0.0.1'
    port = 4001
    
    s = socket.socket()
    s.connect((host, port))
    message = input("Client2:->")
    while message != "quit":
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print("Server: " + data)
        message = input("Client2:->")
    s.close()
    
if __name__ == '__main__':
    main()
    