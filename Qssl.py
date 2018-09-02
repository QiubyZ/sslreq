import socket
import ssl
from ssl import PROTOCOL_SSLv23, PROTOCOL_TLS, PROTOCOL_SSLv3, PROTOCOL_TLSv1, PROTOCOL_TLSv1_1, PROTOCOL_TLSv1_2
PATH = "e://TOOLS PYTHON/ca-bundle.crt"
HOSTNAME = "my.telkomsel.com"
PAYLOAD = "GET https://my.telkomsel.com/ HTTP/1.0\r\nHost: my.telkomsel.com\r\n\r\n"
protocol = [PROTOCOL_SSLv23, PROTOCOL_TLS, PROTOCOL_SSLv3, PROTOCOL_TLSv1, PROTOCOL_TLSv1_1, PROTOCOL_TLSv1_2]
def sslreq(H=HOSTNAME, path=PATH, PAYLOAD=PAYLOAD, protocol=None):
    try:
        print "==== [ REQUESTS ] ====="
        context = ssl.create_default_context()
        if protocol is None:
            protocol = PROTOCOL_SSLv23
        context = ssl.SSLContext(protocol)
        context.verify_mode = ssl.CERT_REQUIRED
        context.check_hostname=True
        context.load_verify_locations(path)
        conn = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname=H)
        print "Proxy: ", H
        conn.connect((H,443))
        print "Versi SSL: ", protocol
        details = conn.getpeercert()
        print '====== [SERTIFIKAT] ===== '
        print details
        print "============================"
        print "SEND PAYLOAD"
        print "============================"
        pay = PAYLOAD
        print repr(pay)
        c = conn.sendall(pay)
        print "========= [RECEIVED] ========"
        cert = conn.recv(1024).split(b"\r\n")
        print cert
    except:
        print "Gagal tersambung"
        print "Versi SSL: ", protocol

for i in protocol:
    sslreq(protocol=i)
