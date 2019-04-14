import socket

def connect():
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(('127.0.0.1', 9999))
        return conn
    except ValueError:
        print("unable to connect") 

def send(x):
    conn.send(b'(next-line)')
    conn.send(b'(insert "foo bar")')

# conn = onnect()
