import socket

def main():
    host = '127.0.0.1'
    port = 3000
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    print("Server Started!")
    while True:
        data, adrs = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Client1: " + data + '\n Address:-' + str(adrs))
        data = data.upper()
        print('Sending Back To:- Client2')
        s.sendto(data.encode('utf-8'),adrs)
    s.close()
    
if __name__ == '__main__':
    main()
