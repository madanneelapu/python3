import socket

contacts = {}
f = open("contacts.txt", "r")

lines = f.readlines()
for line in lines:
    parts = line.strip("\n").split(",")
    name = parts[0]
    number = parts[1]

    if name in contacts:
        contacts.get(name).append(number)
    else:
        contacts[name] = [number]

print(contacts)

s = socket.socket()
host = socket.gethostname()
port = 2000
s.bind((host, port))
s.listen(5)

print("server is up and running...")

while True:
    c, addr = s.accept()
    print("Got connection from ", addr)
    search_name = c.recv(1024).decode()
    response = ""
    phnos = contacts.get(search_name,["No contact found",search_name])
    response = ",".join(phnos)
    c.send(response.encode())
    c.close()
