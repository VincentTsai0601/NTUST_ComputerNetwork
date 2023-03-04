from socket import *
import datetime


server_Name = str(input('Enter server hostname or IP: '))

server_Port = int(input('Enter server port:'))



#AF_INET is for IPv4 - SOCK_STREAM is for TCP
client_Socket = socket(AF_INET, SOCK_STREAM)
 
client_Socket.connect((server_Name,server_Port)) #Input the severName and severPort to connect the sever_side 


recver = client_Socket.recv(1024).decode('ascii')# connection
print("recvier:"+recver)

sentence_name = "HELO "+str(input("Enter your HELO name:")) +"\r\n"#Name
#heloCommand ="HELO Vincent\r\n"
print("sender:"+sentence_name )
client_Socket.sendall((sentence_name).encode())
recver_name = client_Socket.recv(1024).decode('ascii')
print("recvier:"+ recver_name )

12
print("sender:MAIL FROM: Email")
sentence_MAIL ="MAIL FROM:"+str(input("Enter your MAIL :")) +"\r\n"#sender mail
#heloCommand = "MAIL FROM: <f140299792@gmail.com>>\r\n"
client_Socket.sendall((sentence_MAIL).encode('ascii'))
sender_mail = client_Socket.recv(1024).decode('ascii')
print("recvier:"+ sender_mail )


print("sender:RCPT to:email")
sentence_MAIL = "RCPT TO:"+str(input("Enter your MAIL :")) +"\r\n"#receiver Mail
client_Socket.sendall((sentence_MAIL).encode('ascii'))
recver_mail = client_Socket.recv(1024).decode('ascii')
print("recvier:"+ recver_mail )


print("sender:DATA") #data
data = "DATA\r\n"
client_Socket.sendall(data.encode('ascii'))
Transfer_data = client_Socket.recv(1024).decode('ascii')
print("recvier:"+ Transfer_data )



print("Do you like ketchup?")#messeger
print("How about pickles?")
print(".")
heloCommand = "Do you like ketchup\nHow about pickles?\n.\r\n"
client_Socket.sendall(heloCommand.encode('ascii'))
message = client_Socket.recv(1024).decode('ascii')
print("recvier:"+ message  )


print("QUIT")#leave
heloCommand = "QUIT\r\n"
client_Socket.send(heloCommand.encode('ascii'))
quit = client_Socket.recv(1024).decode('ascii')
print("recvier:"+ quit)





#clientSocket.send("QUIT")

print ('<-- message sent to server' \
      ,client_Socket.getpeername()[0], \
      ":", \
      client_Socket.getpeername()[1], \
      'on', datetime.datetime.now())
numOfCharacters = client_Socket.recv(1024)
print ('--> message recieved from server' ,\
      client_Socket.getpeername()[0], \
      ":", \
      client_Socket.getpeername()[1], \
      'on', datetime.datetime.now())

client_Socket.close()
print ("TCP connection with server is closed")