#!/usr/bin/python3
#Amos Struthers

#imports paramiko and the sub process
import paramiko 
import subprocess 
#defines the function ssh_connection and the parameters that will be used, 
#and establishes the ssh connection 
def ssh_connection(ip,port,user,passwd, command):
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,port,username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    #if the ssh is open execute the command given
    if ssh_session.active:
        ssh_session.exec_command(command)
        #allows the output to be kept as the output for the function "ssh_connection"
        pls=ssh_session.recv(1024)
    return pls  
#creates the variable IPaddy wich will be used to call the ip address of the ssh server
#the ip address will be called from a file called "ip.txt"
IPaddy=""
filename="ip.txt" 
ip="x.x.x.x"
fh=open(filename) 
for line in fh:
    IPaddy=line
fh.close() 
#sets variable passwd, and opens a file that contains the server passwd
passwd=""
filename="passwd.txt"
fh=open(filename)
for line in fh:
    passwd=line
#sets variable user, and opens a file that contains the server user
user=""
filename="user.txt"
fh=open(filename)
for line in fh:
    user=line
#this allows user to specify ports if needed, a text file named "port.txt" will be used to get this info 
#comment the next 5 lines (41-45) and uncomment the next line if no special port is needed
#port='22'
port=""
filename="port.txt"
fh=open(filename)
for line in fh:
    port=line
fh.close()
#creates two variables out, and out1. and establishes the SSH connection with the required inputs 
#(ip address file, port, user, password, desired command)
out=ssh_connection(IPaddy,port,user, passwd,'hostname')
out1=ssh_connection(IPaddy,port,user, passwd,'ls -al /var/www')
#calls the variable "outtwo", and "outthree", decodes the binary to utf-8
outtwo=out.decode('utf-8')
outthree=out1.decode('utf-8')
#opens a file to output data into, called 'output.txt'
output='output.txt'
#opens the file "output.txt" and allows it to be ammended
f = open(output,'a')
#prints the results of "out", and "out1" to the text file
f.write(outtwo)
f.write(outthree)
#closes the file
f.close()
