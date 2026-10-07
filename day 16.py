# import socket
# # hostname = socket.gethostname()
# hostname = "www.facebook.com"
# ip = socket.gethostbyname(hostname)
# print("Hostname:", hostname)
# print("IP Address:", ip)

# import socket
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("www.google.com", 80))
# # client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
# client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
# # GET / → Request homepage
# # HTTP/1.1 → Protocol version
# # Host: → Required header
# # \r\n → Line break (important in HTTP)
# # b"" → Sending bytes, not string
# data = client.recv(1024)
# print("Data=",data)
# print("Decoded==========")
# print(data.decode())
# print("Hello\rWorld")

# import os
# ip = input("Enter IP: ")
# response = os.system(f"ping -n 1 {ip}")

# if response == 0:
#     print("Host is alive")
# else:
#     print("Host is unreachable")

# import socket
# target = "192.168.29.71"
# # ports = [21, 22, 23, 80, 443, 3306,5432,5433,8080]
# for port in range(65536):
#     print(f"Scanning port {port}")
#     sock = socket.socket()
#     sock.settimeout(1)
#     result = sock.connect_ex((target, port))
#     if result == 0:
#         print(f"[OPEN] Port {port}")
#     else:
#         pass
#         # print(f"[CLOSED] Port {port}")
#     sock.close()


import socket
common_ports = [21, 22, 23, 25, 53, 80, 110, 143,
                443, 445, 3306, 3389, 8080, 5900, 5432, 5433]

def scan_ports(target, ports):
    open_ports = []
    print(f"\n[*] Scanning {target} ...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # 1 second timeout
        result = s.connect_ex((target, port))
        # service = socket.getservbyport(port, "tcp")
        try:
            service = socket.getservbyport(port, "tcp")
        except Exception as e:
            print(e)
            service = "Unknown Service"
        print(f"[+] Port {port} ({service}) is checked")
        if result == 0:
            try:
                service = socket.getservbyport(port, "tcp")
            except:
                service = "Unknown"
            print(f"[+] Port {port} ({service}) is OPEN")
            open_ports.append((port, service))
        s.close()
    return open_ports


# Target IP (Change to the host you want to test)
target_ip = "192.168.29.71"

# Run the scan
open_ports = scan_ports(target_ip, common_ports)

print("\nScan complete.")
if open_ports:
    print("Open ports found:")
    for port, service in open_ports:
        print(f"- {port} ({service})")
else:
    print("No open ports found.")
