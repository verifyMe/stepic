import socket
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
    conn, addr = s.accept();
    while True:
        data = conn.recv(1024)
        print("Data: " + data.decode('utf-8'))
        if not data:
            break   
        if data.decode('utf-8') == 'close' :
            conn.close()  
            break                
        conn.send(data)
    conn.close()   
