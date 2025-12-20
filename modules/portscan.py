import socket 
import os

def clear():
    os.system("clear")


def scan( ip: str , port: int , timeout: int):
    
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sock.settimeout(timeout)
    
    try:

        ATTEMPT = sock.connect_ex(( ip , port ))

        try:

            SERVICE = socket.getservbyport(port)

        except Exception as exp:
            SERVICE = "Unknown"

        if ATTEMPT == 0:
            print("\t[+] port " , port , "is open\t[service] " , SERVICE)


    except Exception as exp:
        print(f"error : {exp}")

    finally:
        sock.close()

def art():
    art = r"""

  ___         _   ___                    _           
 | _ \___ _ _| |_/ __| __ __ _ _ _  _ _ (_)_ _  __ _ 
 |  _/ _ \ '_|  _\__ \/ _/ _` | ' \| ' \| | ' \/ _` |
 |_| \___/_|  \__|___/\__\__,_|_||_|_||_|_|_||_\__, |
                                               |___/

"""

    import sys , time

    for word in art:
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.002)

def main():
    clear()
    art()

    ip = str(input("[x] Ip To scan : "))
    port = int(input("[x] set the port range ( 1 -- 65535 ) : "))
    timeout = float(input("[x] Set a timeout ( in seconds ) : "))
    
    print("\nScaning Started\n")

    for p in range(1 , port):
        scan(ip , p , timeout)


main()        
