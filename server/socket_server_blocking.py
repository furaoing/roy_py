# utf-8

import socket
import time
from config import my_port

s = socket.socket()
# create a socket object
host = socket.gethostname()
port = my_port
s.bind((host, port))
# bind our socket object to a certain port on this host

s.listen(5)
# start listening to the socket


class Actor(object):
    """ define our socket actor """
    def __init__(self, _my_socket):
        self.my_socket = _my_socket

    def act(self):
        """
        Can only maintain one connection, p2p socket
        """
        while True:
            con, addr = self.my_socket.accept()
            # my_socket.accept() is a blocking method
            print("new connection: %s" % str(addr))

            while True:
                mystr = con.recv(1024)
                # con.recv() is also a blocking method, will return value none when connect became dead
                if not mystr:
                    break

                print(mystr)
            con.close()
            print("closed connection: %s" % str(addr))
        self.my_socket.close()

my_actor = Actor(s)
my_actor.act()
