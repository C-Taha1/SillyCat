import sys
import time
import socket 
import os

REPLY_SIZE = 4096 # for bigger banner handling

def clear():
    os.system("clear")

def typewritter(word: str , delay: float) -> None:
    for char in word:
        sys.stdout.write(char)
        time.sleep(delay)
        sys.stdout.flush()


def grab( ip: str , port: int , timeout: float) -> None:

    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sock.settimeout(timeout)
    GET_REQUEST = f"GET / HTTP/1.1\r\nHost: {ip}\r\nConnection: close\r\n\r\n".encode()


    try:
        SERVICE = socket.getservbyport(port)

    except Exception as exp:
        SERVICE = "unknown"

    try:
        CONN_ATTEMPT = sock.connect_ex((ip , port))


        if CONN_ATTEMPT == 0:

            typewritter(f"\n\033[1;32m[x] Connection Established with {ip}:{port}\033[1;0m\n" , 0.05)
        
            if SERVICE == "http":
                sock.send(GET_REQUEST)
                data = sock.recv(REPLY_SIZE).decode(errors='ignore')
                print(f"[ {ip} : {port} ]\t said: \n\n{data}\n")

            elif SERVICE == "ssh" or SERVICE == "unknown":

                sock.send("Hello Server".encode()) # to nullify server connecting and not responding
                data = sock.recv(REPLY_SIZE).decode(errors='ignore')
                print(f"[ {ip} : {port} ]\tsaid:\n\n{data}\n")


        else:
            print("[closed] the port is closed or network unreachable??\n")


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
    port = int(input("[x] port number ( < 0 < 65535 ) : "))
    timeout = float(input("[x] set a timeout : "))

    grab(host , port , timeout)


main()
