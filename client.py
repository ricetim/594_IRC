import socket

class irc_client():
    
    def start(self, name):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), 55555))
        
        while True:
            self.user_input(s)
            full_msg = ''
            while True:
                msg = s.recv(8)
                if len(msg) <= 0:
                    break
                full_msg += msg.decode("utf-8")

            if len(full_msg) > 0:
                print(full_msg)

    def user_input(self, socket):
        msg = input('prompt: ')
        print(msg)
        socket.send(bytes(msg,"utf-8"))
        
def main():
    # name = input("Please enter your name: ")
    client = irc_client()
    client.start('tim')

if __name__ == "__main__":
    main()
