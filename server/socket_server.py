# utf-8
from gevent import monkey
monkey.patch_all()
import gevent
import socket
from config import my_port
from config import my_host
from config import max_c


def handle_request(_con, _addr, _sleep):
    while True:
        mystr = _con.recv(1024)
        # _con.recv is a non-blocking method, return control to the main routine if no msg
        _sleep(0)
        # Return control to the main routine manually
        if not mystr:
            break
        print(mystr)
    _con.close()
    print("Connection Closed : %s \n" % str(_addr))


def server(_host, _port, _max_c):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # create a socket object
    s.bind((_host, _port))
    # bind our socket object to a certain port on this host

    s.listen(_max_c)
    # start listening to the socket, maximum con= max_c

    print('Serving HTTP on port: %s \n' % str(_port))

    while True:
        con, addr = s.accept()
        # my_socket.accept() is a non-blocking method
        # if no new connection accepted, return control back to the co-routine
        print("Tcp Connection Established")
        print("Client Address:" + str(addr) + "\n")
        gevent.spawn(handle_request, con, addr, gevent.sleep)
        # Schedule and start a co-routine
    s.cloce()
    # s.close() will never be executed

server(my_host, my_port, max_c)






