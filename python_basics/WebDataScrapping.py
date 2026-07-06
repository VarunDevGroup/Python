import socket
import re

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(("data.pr4e.org", 80))

cmd = "GET /intro-short.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n"
mysocket.send(cmd.encode())

response = b''

while True:
    data = mysocket.recv(512)
    if not data:
        break
    response += data

mysocket.close()

text = response.decode()

headerVal={}

for line in text.splitlines():
    if line.startswith("Content-Type:"):
        headerVal["Content-Type"]=line.split(":")[1].strip()
    elif line.startswith("Content-Length:"):
        headerVal["Content-Length"]=line.split(":")[1].strip()
    elif line.startswith("ETag:"):
        headerVal["ETag"]=line.split(":")[1].strip()

print(headerVal)