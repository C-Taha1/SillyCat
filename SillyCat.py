import os , sys
import time

# global vars 

universal_path = "modules"
build_tools = ["python3"]

# interface starts here

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def typewritter(word: str , delay: int) -> None:
    for char in word:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def art():
    art = r"""

                                                                /\___/\
                                                                )     (
                                                               =\     /=
                                                                 )   (
                                                                /     \
                                                                )     (
                                                               /       \
                                                               \       /
                                                                \__ __/
                                                                   ))
                                                                  //
                                                                 ((
                                                                 \) 

"""

    typewritter(art , 0.003)



# functionalty starts here

def Listdirectory():
    try:
        return os.listdir(universal_path)

    except Exception as exp:
        print(f"error opening the main directory [ details : {exp}] ")
        return None



def printFiles() -> None:
    files = Listdirectory()

    typewritter("[x] Fecthing Modules...\n" , 0.09)
    time.sleep(1)
    typewritter("[x] All modules loaded...\n" , 0.09)

    for (count , file) in enumerate(files):
        print(f"\tmodule {count + 1} : {file}")
        
        if not file:
            print("0 Modules Found")
            
            return "NO MODULES FOUND"


def runFile(filename:str) -> None:
    directory = universal_path # memo footprint short ( a bit )

    try:
        if filename.endswith(".py"):
            os.system(f"{build_tools[0]} {directory}/{filename}")
        else:
            print(f"cant run {file} [ details : intrepeter/compiler not found ]")

    except Exception as exp:
        print(f"error running the file [ details : {exp} ]")    




def helpMenu():
    typewritter(f"[x] Commands:\n" , 0.09)

    print("\tlist -- print full modules list")
    print("\trun -- run a module")
    print("\tclear -- clear the screen") 
    print("\texit -- exit SillyCat")



def DataLoop():
    data = input("[silly] ")

    return data 



def main():

    clear()
    art()

    run_time  = True

    while run_time:
        data = DataLoop().lower()

        if data == "exit":
            print("have a nice day\n")
            exit()

        elif data == "help":
            helpMenu()

        elif data == "list":
            printFiles()

        elif data == "run":
            filename = str(input('module to load? ( with extension ) : '))
            runFile(filename)

        elif data == "clear":
            clear()   

if __name__ == '__main__':
    main()             