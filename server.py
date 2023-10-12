import socket
import json
import random
import string

file = open("regs", "r")
lines = file.readlines()
records = {}
  
for line in lines:
    data = json.loads(line.strip())
    records[data["addressOfRecord"]] = data

server_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Connecting to the localhost
ip_address = '127.0.0.1'
port = 5556
server_object.bind((ip_address, port))
server_object.listen()

#Once the client connects to the particular port, the server starts to accept the request.
connection_object, _ = server_object.accept()

connection_object.settimeout(10)

if connection_object:
	# Connected to client successfully
    print("SERVER CONNECTED TO CLIENT")
    
    # sending initial message to the client
    connection_object.send(b"type the message")
    
    # receiving message from the client
    aor = connection_object.recv(1024)
    try:
        while True:
            aor_decoded =  aor.decode('utf-8')
            print("{}: {}".format("CLIENT MESSAGE: ", aor_decoded))
            if records.get(aor_decoded):
                data = json.dumps(records[aor.decode("utf-8")])
                connection_object.send(bytes(data, encoding="utf-8"))
            else:
                connection_object.send(bytes(" ", encoding="utf-8"))

            aor = connection_object.recv(1024)
            connection_object.settimeout(10)
    except socket.timeout as e:
            print(e,': No message received after 10 seconds.Closing the connection...')
            connection_object.close()    












    
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.bind((HOST, PORT))
    #     s.listen()
    #     while True:
    #         conn, addr = s.accept()

    #         with conn:
    #             print(f"Connected by {addr}")
    #             try:
    #                 while True:
    #                     aor = conn.recv(1024)

    #                     if not aor:
    #                         conn.sendall(b"")

    #                     data = json.dumps(records[aor.decode("utf-8")])
    #                     print(data)
    #                     conn.sendall(bytes(data, encoding="utf-8"))
    #             except:
    #                 print('error')
    #                 conn.close()            