import socket
import sys


def pars_accept(conn, addr):
    data = b""
    while not b"\n\r" in data:
        text = conn.recv(1024)
        if not text:
            break
        else:
            data += text
        if not data:
            return

    data = data.decode("utf-8")
    if len(data.split(" ")) < 3:
    	return
    data = data.split("\n\r")[0]
    type, address, query = data.split(" ", 2)

    index_file = open('C:\\Users\\amdin\Desktop\web\DZ1\webProgramming\index.html')
    about_file = open('C:\\Users\\amdin\Desktop\web\DZ1\webProgramming\\about\\aboutme.html')

    if type == "GET" and (address == "/index.html" or address == "/"):
        send(conn, typ="text/html; charset=utf-8", data=index_file.read())
    elif type == "GET" and address == "/about/aboutme.html":
        send(conn, typ="text/html; charset=utf-8", data=about_file.read())        
    else:
        send(conn, "404 Not Found", data="Не найдено")
        return

    index_file.close()
    about_file.close()

    # answer = """<!DOCTYPE html>"""
    # answer += """<html><head><title>Aboutme</title></head><body><h1>"""
    # answer += "C:\\Users\\amdin\Desktop\web\DZ1\webProgramming"
    # answer += "\\about\\aboutme.html" if (address == "/about/aboutme.html") else "\\index.html"
    # answer += """</h1></body></html>"""
    # return answer

def send(conn, status="200 OK", typ="text/plain; charset=utf-8", data=""):
    data = data.encode("utf-8")
    conn.send(b"HTTP/1.1 " +  status.encode("utf-8") + b"\r\n")
    conn.send(b"Server: simplehttp\r\n")
    conn.send(b"Connection: close\r\n")
    conn.send(b"Content-Type: " + typ.encode("utf-8") + b"\r\n")
    conn.send(b"Content-Length: " + bytes(len(data)) + b"\r\n")
    conn.send(b"\r\n")
    conn.send(data)

def main():
    sock = socket.socket()
    sock.bind(('', 8000))
    sock.listen(1)

    try:
        while True:
            conn, addr = sock.accept()
            print(addr[0])
            try:
            	pars_accept(conn, addr)
            except:
            	send(conn, "404 Not Found", data="Не найдено")
            finally:
            	conn.close()
    finally:
        sock.close()

if __name__ == "__main__":
    main()