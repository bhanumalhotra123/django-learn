import urllib.request  # Importing the urllib library for handling URLs

# urllib.request module abstracts the network communication, allowing you to work at a higher level of abstraction than dealing with sockets directly.
# Opening a connection to the specified URL using HTTP
fhand = urllib.request.urlopen('http://127.0.0.1:9000/bhanu.txt')

# Iterating through each line of the response from the server
for line in fhand:
    # Decoding each line from bytes to a string and removing any leading/trailing whitespace
    print(line.decode().strip())  # Printing the decoded line

