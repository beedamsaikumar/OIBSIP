import socket
import threading

# Client configuration
host = '127.0.0.1'
port = 5555

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except ConnectionResetError:
            break

def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Create threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

send_thread = threading.Thread(target=send_messages, args=(client_socket,))
send_thread.start()
