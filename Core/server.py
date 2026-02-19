import socket
import selectors
from . import client


class Server:
    def __init__(self,port,password):
        self.passw = password
        self.port = port
        self._s_socket = None
        self._poller = None
        self._clients = []

#initial the server socket:  
    def start(self):
        self._poller = selectors.DefaultSelector()
        self._s_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self._s_socket.bind(("0.0.0.0",self.port))
        self._s_socket.listen()
        self._s_socket.setblocking(False)
        self._poller.register(self._s_socket,selectors.EVENT_READ)
        self.main_loop()
#the main server loop
    def main_loop(self):
        while True: 
            event = self._poller.select() 
            for key,mask in event:
                if key.fileobj == self._s_socket:
                    conn,addr = self._s_socket.accept()
                    self.client_init(conn,addr)
                else:
                    #hand_connection
                    pass
    def client_init(self,conn,addr):
        conn.setblocking(False)
        cl = client.Client(conn,addr)
        self._clients.append(cl)
        self._poller.register(conn,selectors.EVENT_READ,data=cl)
        print(f"new client connected with the addr{addr}")
    
