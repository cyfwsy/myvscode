import socket
import sys

messages = [
    'This is a message',
    'it will be sent',
    'in parts',
    '這是中文'
]
server_address = ('localhost', 9999)
# Create a TCP/IP socket
socks = [
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM)
]
# Connect the socket to the port where the server is listening
print('connecting to {} port {}'.format(*server_address), file=sys.stderr)
for s in socks:
    s.connect(server_address)
for message in messages:
    outgoing_data = message.encode()
    # Send message on both sockets.
    for s in socks:
        print('{}: sending {!r}'.format(s.getsockname(), outgoing_data), file=sys.stderr)
        s.send(outgoing_data)
    # read response on both sockets
    for s in socks:
        data = s.recv(1024)
        print('{} received {!r}'.format(s.getsockname(), data.decode()), file=sys.stderr)
        if not data:
            print('closing socket', s.getsockname(), file=sys.stderr)
            s.close()
