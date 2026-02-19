import sys
from Core import server

def pars_args():
    ac = len(sys.argv)
    if(ac != 3 or not (sys.argv[1].isdigit()) or not (sys.argv[2].isdigit()) or (len(sys.argv[1])!= 4) or (len(sys.argv[2]) != 4)):
        return 0
    return 1

def main():
    if not pars_args():
        print("ERROR")
        return
    PORT = int(sys.argv[1])
    PASS = int(sys.argv[2])
    irc = server.Server(PORT,PASS)
    irc.start()


if __name__ == "__main__":
    main()