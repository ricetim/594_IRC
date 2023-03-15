import socket

class irc_client():
    
    def start(self, name):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), 55555))



def main():
    # name = input("Please enter your name: ")
    client = irc_client()
    client.start('tim')

if __name__ == "__main__":
    main()
