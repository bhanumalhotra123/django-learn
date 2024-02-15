from socket import *

def createServer():
    # Create a socket object using the IPv4 address family and TCP protocol
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        # Bind the socket to the localhost address and port 9000
        serversocket.bind(('localhost', 9000))
        # Set the maximum number of queued connections to 5
        serversocket.listen(5)

        # Continuously accept incoming connections
        while(1):
            # Accept a connection request and return a new socket object and the address of the client
            (clientsocket, address) = serversocket.accept()

            # Receive data from the client (up to 5000 bytes) and decode it as UTF-8
            rd = clientsocket.recv(5000).decode()

            # Split the received data into separate lines
            pieces = rd.split("\n")

            # If there are lines in the received data, print the first line
            if len(pieces) > 0:
                print(pieces[0])

            # Construct the HTTP response
            data = "HTTP/1.1 200 OK\r\n"  # Status line
            data += "Content-Type: text/html; charset=utf-8\r\n"  # Content type header
            data += "\r\n"  # Blank line indicating the end of headers
            data += "<html><body>Hello World</body></html>\r\n\r\n"  # HTML body

            # Send the response back to the client after encoding it as UTF-8
            clientsocket.sendall(data.encode())

            # Shutdown the socket for writing
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        # Handle keyboard interrupt by printing a message
        print("\nShutting down...\n")
    except Exception as exc:
        # Handle any other exceptions by printing the error message
        print("Error:\n")
        print(exc)

    # Close the server socket
    serversocket.close()

# Print a message indicating the URL to access the server
print('Access http://localhost:9000')
# Call the createServer function to start the server
createServer()

