from __future__ import print_function
#import datetime
import socket
import sys, time
from socket import *
from tokenize import Double, String
#from turtle import Turtle




BUFSIZE = 1048576



def main():
    
    print(sys.argv)
    print("Iperfer  -c -h <server hostname> -p <server port> -t <time>")
    print("Iperfer  -s -p <listen port>")
    
    if len(sys.argv) < 2:
        Error_messege()
    if sys.argv[1] == "-s":
        servermode()
    elif sys.argv[1] == "-c":
        clientmode()
    else:
        Error_messege()
       
def Error_messege():
    sys.stdout = sys.stderr
    print("Error: missing or additional arguments")
    sys.exit()



def servermode():
    data_volume=0
    start_time =0
    Finish_time  =0
    Time_period  =0
    if (sys.argv[2] == "-p"):
    
        listen_port = eval(sys.argv[3])
        if (1024> listen_port or listen_port >65535):
            print("Error: port number must be in the range 1024 to 65535")
        elif (1024 <= listen_port and listen_port<= 65535):    
            start_time = time.time()
            
            s = socket(AF_INET, SOCK_STREAM)
            s.bind(('', listen_port))
            s.listen(1)
            print ("server is stand by")

            while True:
                conn, (host, Remote_port) = s.accept()
                while True:
                    data = conn.recv(BUFSIZE)
                    data_volume += len(data)
                    if not data:
                        break
                    del data
                
                conn.close()
                Finish_time = time.time() 
                
                print('host_name', host, 'port_number', Remote_port)   
                
                Time_period = Finish_time - start_time 
                print ("received=", data_volume /1024,"KB","rate=",(((data_volume*8) /1024)/1024)/( Time_period ),"Mbps")

        
def clientmode():
    data = 0
    total_bits=0
    if len(sys.argv) < 4:
        Error_messege()
    
    if len(sys.argv) > 4:
        if sys.argv[2] == '-h':
            server_hostname = sys.argv[3]
        if sys.argv[4] == "-p":
            port = eval(sys.argv[5])
        if (1024> port or port >65535):
            print("Error: port number must be in the range 1024 to 65535")
            return
        if sys.argv[6] == '-t':
            count = eval(sys.argv[7])

    
        
        testdata = 'Hello World' * (BUFSIZE-1) + '\n'
        Start_Time = time.time()
        s = socket(AF_INET, SOCK_STREAM)
        t2 = time.time()
        s.connect((server_hostname, port))
        t3 = time.time()
        i = 0
        
        while i < count:
            i = i+1
            s.send(testdata.encode())

        s.shutdown(1) # Send EOF
        
        data = s.recv(BUFSIZE)
       
        Finish_time = time.time()

        print ('sent:=' ,(BUFSIZE*count*0.001),'KB')
        print ("rate:=", (BUFSIZE*count*8*0.001*0.001) / (Finish_time -Start_Time),'Mbps.')


main()