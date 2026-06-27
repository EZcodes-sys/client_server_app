import socket, time

HOST, PORT = "127.0.0.1", 9000
commands = ["HELLO", "PING", "TIME", "STATUS", "INVALID", "QUIT"]

print(f"CLIENT ▶ Connecting to {HOST}:{PORT} ...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("CLIENT ▶ Connected successfully.\n")
    for cmd in commands:
        print(f"  CLIENT ▶ Sending: '{cmd}'")
        s.sendall(cmd.encode("utf-8"))
        response = s.recv(1024).decode("utf-8")
        print(f"  CLIENT ◀ Received: '{response}'\n")
        time.sleep(0.2)
print("CLIENT ▶ Session complete. Connection closed.")