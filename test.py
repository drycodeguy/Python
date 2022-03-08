#!/usr/bin/python3

import paramiko 
import subprocess 
def ssh_connection(ip,port,user,passwd, command):
    client=paramiko.SSHClient()
    # If you wanted to use ssh keys instead, uncomment the line below
    #client.load_host_keys('/home/user/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,port,username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        pls=ssh_session.recv(1024)
    return pls
IPaddy=""
filename="ip.txt.txt" 
ip="x.x.x.x"
fh=open(filename) 
for line in fh:
    print(line)
    IPaddy=line
fh.close() 
out=ssh_connection(IPaddy,'6969','amos', 'amos24','ls')
#print(f'this is out: {out}')
outtwo=out.decode('utf-8')
output='output.txt'
f = open(output,'a')
f.write(outtwo)
f.close()
