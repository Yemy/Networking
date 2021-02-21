import socket

def main():
    host = '127.0.0.1'
    port = 3001
    
    server = ('127.0.0.1', 3000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    message = input("Me:")
    while message != quit:
        s.sendto(message.encode('utf-8'), server)
        data, adrs = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('Server:' + data + '\nAddress:-' + str(adrs))
        message = input("Me:")
    s.close()
    
if __name__ == '__main__':
    main()