import os
import socket


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def check_open_ports(IP: str, PORT: int, timeout: float) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        ATTEMPT = sock.connect_ex((IP, PORT))

        try:
            SERVICE = socket.getservbyport(PORT)

        except Exception as exp:
            SERVICE = "unknown"

        if ATTEMPT == 0:
            print(f"\t[+] port {PORT} is open || Service :: {SERVICE}")

    except Exception as exp:
        print(f"[:] Error -> {exp} ")

    finally:
        sock.close()


def main() -> None:
    clear()

    IP = str(input("[V] Ip Address to scan: "))
    PORT_RANGE = int(input("[V] Port Range ( < 65535 ) : "))
    timeout = float(input("Set Timeout Limit (e.g 0.5 ) : "))

    for PORT in range(1, PORT_RANGE + 1):
        check_open_ports(IP, PORT, timeout)


main()
