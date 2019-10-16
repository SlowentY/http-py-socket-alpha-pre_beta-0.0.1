import socket
import threading
from htmls import *

URLS = {
    '/': index,
    '/blog': blog
}

def gen_response(req):
    parsed = req.split(' ')
    s = ''
    i = 200
    print(req)
    if parsed[0] != 'GET':
        s = 'HTTP/1.1 405 Method not allowed\n\n <h1>405</h1><p>Vy sdelali kakoito ban! :-(</p>'
        i = 405
    elif parsed[1] not in URLS:
        s = 'HTTP/1.1 404 Not found\n\n <h1>404</h1><p>Dumayu tut oboidetsya bez slov. |-)</p>'
        i = 404
    else:
        s = 'HTTP/1.1 200 OK\n\n' + URLS[parsed[1]]()

    return s
    

def serverThread(sock, addr, html):
    try:
        print(addr)
        data = sock.recv(1024)
        print(type(data))
        response = gen_response(data.decode('utf-8'))
        print(response)
        sock.send(response.encode())
        sock.close()
    except:
        sock.close();
        print("error");


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 80))
sock.listen(10);
threads = []
i = 0
f = open("html\index.html")
s = f.read()
f.close()

while True:
    client, addr = sock.accept()
    t1 = threading.Thread(target=serverThread, args=(client, addr, s))
    threads.append(t1)
    threads[i].start()
    i = i + 1
