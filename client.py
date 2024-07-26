import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("connection is stablished you can start sending data")
    try:
        client_socket.connect(('192.168.29.113', 5555))
        payload = 'hey server'

        try:
            while True:
                client_socket.send(payload.encode('utf-8'))
                data = client_socket.recv(1024)
                if not data:
                    print("Server closed the connection")
                    break
                print("Received from server:", str(data))
                more = input('Want to send more data to the server (y/n)? ')
                if more.lower() == 'y':
                    payload = input("Enter payload: ")
                else:
                    break
        except KeyboardInterrupt:
            print("Exited by user")
        except ConnectionResetError as e:
            print(f"Connection was closed by the server: {e}")
        finally:
            client_socket.close()
    except Exception as e:
        print(f"Failed to connect to the server: {e}")

if __name__ == "__main__":
    main()
