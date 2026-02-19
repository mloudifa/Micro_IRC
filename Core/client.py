class Client:
    def __init__(self,conn,addr):
        self._socket = conn
        self.addr = addr
        self._rec_buf = b''
        self.nick = ''
        self.user = ''
        self.isreg = False