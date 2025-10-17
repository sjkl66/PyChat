import socket
import threading
import json

server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen()

clients: dict[str, socket.socket] = {}

def handle_client(client: socket.socket) -> None:
    client_data = {}
    response = client.recv(2048).decode()
    response = json.loads(response)
    res_type = response.get("type", None)
    if not res_type:
        return
    if res_type == 'username':
        client_data["username"] = response.get("username")

running = True
while running:
    client, addr = server.accept()
    