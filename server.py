
from talon.voice import Context, Str, Word, Key, Rep, press
import socket
import threading


def threaded_scroll(dir):
    size = 1024
    while True:
              try:
                  data = conn.recv(size)
                  # if data:
                      # press('esc')
                      # Str('received received xxxxxx')(None)
                      # Str(str(data))(None)
                  # else:
                      # Str('no data')(None)
                      # raise error('received data')
              except:
                  conn.close()
                  return False

def connect():
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            conn.connect(('127.0.0.1', 9998))
        except ValueError:
            print("connection ")
        thread = threading.Thread(target=threaded_scroll, args=([1]))
        thread.start()
        return conn

    except ValueError:
        print("unable to connect") 

def send(x):
    # string = str(x)
    # string.replace("[","")
    # string.replace("]","")
    # string.replace(",","")
    # string.replace("'","")
    string = bytes(x, encoding= 'utf-8')
    conn.send(string)

def disconnect():
    conn.close()
            
# conn = connect()

# connecte







                    # "down" + numerals: lambda x: send_parsed_number(x , "down",1),
                    # "up" + numerals: lambda x: send_parsed_number(x , "up",1),
                    # "up" : Key('cmd-esc k'),
    # ""+numerals : lambda x: send("number"),

    # "seven" : lambda x: send("number"),
    # "7" : lambda x: send("number"),
    # "three" : lambda x: send("number"),
    # "<dgndictation>": lambda x: send(str(x._words)),
    # "<dgndictation>": lambda x: send(str(x.dgndictation[0])),
    # "<dgndictation>": lambda x: send(str(parse_words(x))),
    # "1" : lambda x: send("number"),
    # "one" : lambda x: send("number"),


                    # "down" : lambda x: send("down"),
                    # "up" : lambda x: send("up"),
