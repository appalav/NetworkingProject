import socks
s = socks.socksocket()
s.set_proxy(socks.SOCKS5, "0.0.0.0", 8000) 
hostname = "www.example.com"
s.connect((hostname, 80))
request = b"GET / HTTP/1.0\r\nHost: " + hostname.encode('utf-8') + b"\r\n\r\n"
s.sendall(request)
response = s.recv(2048)
while response:
    print(response.split(b"\r\n"))
    response = s.recv(2048)
