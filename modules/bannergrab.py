import sys
import time
import socket 
import os

def clear():
    os.system("clear")

def typewritter(word: str , delay: float) -> None:
    for char in word:
        sys.stdout.write(char)
        time.sleep(delay)
        sys.stdout.flush()


def grab( ip: str , port: int , timeout: float) -> None:

    REPLY_SIZE = 1024
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        CONN_ATTEMPT = sock.connect_ex((ip , port))

        if CONN_ATTEMPT == 0:
            typewritter(f"\n\033[1;32m[x] Connection Established with {ip}:{port}\033[1;0m\n" , 0.05)
        
            data = sock.recv(REPLY_SIZE).decode(errors='ignore')

            print(f"[ {ip}:{port} ] said:\n{data}")


    except Exception as exp:
        print(f"error : {exp}")

    
    finally:
        sock.close()


def art():
    art = r""" 

  ___                          ___          _    _           
 | _ ) __ _ _ _  _ _  ___ _ _ / __|_ _ __ _| |__(_)_ _  __ _ 
 | _ \/ _` | ' \| ' \/ -_) '_| (_ | '_/ _` | '_ \ | ' \/ _` |
 |___/\__,_|_||_|_||_\___|_|  \___|_| \__,_|_.__/_|_||_\__, |
                                                       |___/ 

"""


    typewritter(art , 0.002)


def main():

    clear()
    art()
    
    host = str(input("[x] host  ip : "))
    port = int(input("[x] port number : "))
    timeout = float(input("[x] set a timeout : "))

    grab(host , port , timeout)


main()
