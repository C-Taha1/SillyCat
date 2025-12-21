import requests
import sys
import os
import time


def clear():
	os.system("clear")

def typewritter(string: str , delay: float) -> None:
	for char in string:
		sys.stdout.write(char)
		time.sleep(delay)
		sys.stdout.flush()


def art():
	art = r""" 

  ___  _            _                  ___          _         ___               
 |   \(_)_ _ ___ __| |_ ___ _ _ _  _  | _ )_ _ _  _| |_ ___  | __|__ _ _ __ ___ 
 | |) | | '_/ -_) _|  _/ _ \ '_| || | | _ \ '_| || |  _/ -_) | _/ _ \ '_/ _/ -_)
 |___/|_|_| \___\__|\__\___/_|  \_, | |___/_|  \_,_|\__\___| |_|\___/_| \__\___|
                                |__/                                            

"""

	typewritter(art , 0.002)

# intresting status codes:

CODES = [ 200 , 500 ]

def brute(url: str , word: str , delay: int) -> None:

	try:
		time.sleep(delay)

		REQ = requests.get(f"{url}/{word}" , allow_redirects=False)

		if REQ.status_code in CODES:
			print(f"[{REQ.status_code}] -- {url}/{word}")

	except Exception as exp:
		print(f"error : {exp}")


def openList(wordlist: str) -> None:

	with open(wordlist , 'r') as wl:
		CONTENT = wl.read().split()

	return CONTENT

def main():

	clear()
	art()

	base_url = str(input("[x] Enter URL ( start with http/https )  : "))
	wordlist = str(input("[x] Path To wordlist : "))
	delay  =   float(input("[x] Set Delay ( helps with rate limiting and stuff ) : "))

	if wordlist == "":
		print("No wordlist provided , using the default wordlist...")
		words = openList("wordlists/small.txt")

	else:
		words = openList(wordlist)

	typewritter("\nBruteForcing has Started...\n" , 0.009)

	for word in words:
		brute(base_url , word , delay)

main()



