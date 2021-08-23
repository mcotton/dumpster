# socket_echo_server.py
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('157.230.222.187', 5999)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

data = ''
message = ''

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data += str(connection.recv(1024), "utf-8")
            #print('received {!r}'.format(data))

            if data.find('\n') > -1:
                message = data
                data = ''

                print(message)

    except KeyboardInterrupt:
        connection.close()
        sys.exit()

    finally:
        # Clean up the connection
        connection.close()
