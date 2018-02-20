import socket




while True:
    search_name = input("Please enter name ['end' to stop]:")
    if "end" == search_name:
        print("Thank you.")
        break

    s = socket.socket()
    host = socket.gethostname()
    port = 2000
    s.connect((host, port))
    s.send(search_name.encode())
    print(s.recv(1024).decode())
    s.close()