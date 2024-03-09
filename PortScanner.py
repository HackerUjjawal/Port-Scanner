import socket
print("Welcome,")
print("       Develop BY Ujjawal")
target = input("Enter a remote host or Ip to scan: ")
start_port = 1
end_port = 65535

print("Scanning Target:", target)

for port in range(start_port, end_port + 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print("Port", port, "is open")
        sock.close()
    except socket.error:
        pass
