import logging
import socket
import sys

def retrieve_url(url):
 
    target_host = url[7:]  # removing http:// from the string
    target_port = 80  # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, target_port))

    request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
    client.send(request.encode())

    response = client.recv(8196)
    http_response = repr(response)


    return (response)

if __name__ == "__main__":
    sys.stdout.buffer.write(retrieve_url(sys.argv[1])) # pylint: disable=no-member
