import socket
import threading
import json

#Variables for holding information about connections
connections = []
total_connections = 0
records = {}

#Client class, new instance created for each connected client
#Each instance has the socket and address that is associated with items
#Along with an assigned ID and a name chosen by the client
class Client(threading.Thread):
    def __init__(self, socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal
    
    def __str__(self):
        return str(self.id) + " " + str(self.address)
    
    #Attempt to get data from client
    #If unable to, assume client has disconnected and remove him from server data
    #If able to and we get data back, print it in the server and send it back to every
    #client aside from the client that has sent it
    #.decode is used to convert the byte data into a printable string
    def run(self):
        #set timeout to 10 seconds
        self.socket.settimeout(10)

        while self.signal:
            try:
                data = self.socket.recv(32)

                #Reset timeout to 10 seconds once we receive the message
                self.socket.settimeout(10)

                data_decoded = str(data.decode("utf-8"));

                print("ID " + str(self.id) + ": " + data_decoded)

                if records.get(data_decoded):
                    record = json.dumps(records[data_decoded])
                    #Send matched record to the client
                    self.socket.sendall(bytes(record, encoding="utf-8"))
                else:
                    #Send back empty line if no record matched 
                    self.socket.sendall(bytes(" ", encoding="utf-8"))
            except socket.timeout as e:
                print(e,f': No message received after 10 seconds.Closing the connection at ID {self.id} {self.address}')
                self.signal = False
                connections.remove(self)
                break
            except:
                print("Client " + str(self.address) + " has disconnected")
                self.signal = False
                connections.remove(self)
                break
           
def loadRecords(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        data = json.loads(line.strip())
        records[data["addressOfRecord"]] = data                        

#Wait for new connections
def newConnections(socket):
    while True:
        sock, address = socket.accept()
        global total_connections
        connections.append(Client(sock, address, total_connections, "Name", True))
        connections[len(connections) - 1].start()
        print("New connection at ID " + str(connections[len(connections) - 1]))
        total_connections += 1

def main():
    #Load records from file
    loadRecords("regs")

    #Get host and port
    host = input("Host: ")
    port = int(input("Port: "))
      

    #Create new server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    print(f"Server listening on {host}:{port}")

    #Create new thread to wait for connections
    newConnectionsThread = threading.Thread(target = newConnections, args = (sock,))
    newConnectionsThread.start()
    
main()