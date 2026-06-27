import socket, threading, datetime

HOST, PORT = "127.0.0.1", 9000

def log(msg):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}")

def process_request(req):
    req = req.upper().strip()
    if req == "HELLO":   return "HELLO — Server acknowledges client connection."
    elif req == "TIME":  return f"TIME — Server time: {datetime.datetime.now()}"
    elif req == "PING":  return "PONG — Server is alive and reachable."
    elif req == "STATUS": return "STATUS — Server is running normally on localhost:9000."
    elif req == "QUIT":  return "QUIT — Closing connection. Goodbye!"
    else: return f"UNKNOWN — Command '{req}' not recognised."

def handle_client(conn, addr):
    log(f"Connection accepted from {addr[0]}:{addr[1]}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data: break
            request = data.decode("utf-8").strip()
            log(f"Received: '{request}'")
            response = process_request(request)
            conn.sendall(response.encode("utf-8"))
            log(f"Sent: '{response}'")
            if request.upper() == "QUIT": break
    log(f"Connection with {addr[0]}:{addr[1]} closed")

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind((HOST, PORT))
server_sock.listen(5)
log(f"Listening on {HOST}:{PORT} ...")
while True:
    conn, addr = server_sock.accept()
    threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()