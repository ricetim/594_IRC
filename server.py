import socket



class irc_server():
    
    def __init_(self, host_addr, host_port):
        # self.host_addr = host_addr
        # self.port = host_port
        self.host_addr = '127.0.0.1'
        self.port = 99999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(), self.host_port))
        s.listen(5)
        
        while True:
            client_socket, client_address = s.accept()
            print(f"Connection from {client_address} has been established.")
            
    def start(self, host_addr, host_port):
        # self.host_addr = host_addr
        # self.port = host_port
        self.host_addr = '127.0.0.1'
        self.host_port = 55555
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(), self.host_port))
        s.listen(5)
        
        while True:
            client_socket, client_address = s.accept()
            print(f"Connection from {client_address} has been established.")
            client_socket.send(bytes("Hey there!!!","utf-8"))
            msg = client_socket.recv(256)
            print(msg)
            # client_socket.close()


def main():
    server = irc_server()
    server.start('127.0.0.1', 55355)
    
if __name__ == "__main__":
    main()
