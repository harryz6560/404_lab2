import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHost: "+ host.encode('utf-8') + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(request)
    s.shutdown(socket.SHUT_WR)
    result = s.recv(BYTES_TO_READ)
    
    # print the messages
    while(len(result) > 0):
        print(result)
        result = s.recv(BYTES_TO_READ)

    s.close()

if __name__ == "__main__":
    # get('www.google.com', 80)
    get("localhost", 8001)
