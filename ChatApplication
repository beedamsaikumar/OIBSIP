import socket
import threading

# Server configuration
host = '127.0.0.1'
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

def handle_client(client_socket, addr):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Received from {addr[0]}: {message}")

            # Broadcast received message to all clients except sender
            for c in clients:
                if c != client_socket:
                    c.send(f"From {addr[0]}: {message}".encode('utf-8'))
        except ConnectionResetError:
            break

    # Remove disconnected client
    clients.remove(client_socket)
    client_socket.close()

def accept_connections():
    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f"Connection established with {addr[0]}:{addr[1]}")

        # Create a thread to handle client communication
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

def send_server_message():
    while True:
        message = input("Server: ")  # Take server input
        broadcast_message = f"Server: {message}"
        for c in clients:
            c.send(broadcast_message.encode('utf-8'))

clients = []

server.listen(5)  # Listen for up to 5 clients
print("Waiting for connections...")

# Start threads for accepting connections and sending server messages
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()

send_server_message_thread = threading.Thread(target=send_server_message)
send_server_message_thread.start()

