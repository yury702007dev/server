import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
server_socket.bind(('0.0.0.0', 5555))
server_socket.listen(10)

while True:
    client_socket, client_addr = server_socket.accept()
    print(f'Connected with {client_addr}')

    while True:
        data = client_socket.recv(1024)
        if not data:
            print('oops...')
            break
        print(data)
        client_socket.sendall(data)

    client_socket.close()
