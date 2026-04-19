#!/usr/bin/python3
"""Client-server dictionary transfer using JSON serialization."""
import json
import socket


HOST = "127.0.0.1"
PORT = 65432


def start_server():
    """Start a server, receive JSON data, and print the dictionary."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        connection, _ = server_socket.accept()
        with connection:
            chunks = []
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                chunks.append(data)

        received_dict = json.loads(b"".join(chunks).decode("utf-8"))
        print("Received Dictionary from Client:")
        print(received_dict)


def send_data(data):
    """Serialize a dictionary and send it to the server."""
    try:
        payload = json.dumps(data).encode("utf-8")
        with socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            client_socket.sendall(payload)
    except OSError:
        return None
