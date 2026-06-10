
import socket
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

HOST = "0.0.0.0"
PORT = 2222

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Honeypot listening on port {PORT}...")

while True:
    client, addr = server.accept()
    ip = addr[0]

    print(f"Connection received from {ip}")

    with open("logs/connections.log", "a") as log:
        log.write(f"{datetime.now()} - {ip}\n")

    client.send(b"Access Denied\n")
    client.close()
