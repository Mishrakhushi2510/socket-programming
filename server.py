import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.29.113", 5555))
server_socket.listen(5)

print("Server is running and waiting for connections...")

while True:
    print("Server waiting for connection")
    client_socket, addr = server_socket.accept()
    print("Client connected from ", addr)
    try:
        while True:
            data = client_socket.recv(1024)
            if not data or data.decode('utf-8') == 'END':
                break
            print("Received from client: %s" % data.decode("utf-8"))
            more = input('Want to send data to the client (y/n)? ')
            if more.lower() == 'y':
                payload = input("Enter payload: ")
                client_socket.send(payload.encode('utf-8'))
            else:
                break
    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        client_socket.close()
        print("Client connection closed")

  