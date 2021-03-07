import threading
import socket
import time
from termcolor import colored
import sys

def portscan(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)# 

    try:
        con = s.connect((ip,port))

        print(colored('[+]','green')," ",port)

        con.close()
    except: 
        pass
        #print(colored('[-]','red')," ",port)


try:
    ip = sys.argv[1]
except:
    print('Invalid argument')
    sys.exit(1)


start = time.time()
r = 1;
for x in range(1,10000): 
    t = threading.Thread(target=portscan,kwargs={'port':r}) 
    r += 1     
    t.start()
print(f"Runtime of the program is {time.time() - start}")





