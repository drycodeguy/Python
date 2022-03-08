#!/usr/bin/python3

#amosstruthers

import paramiko
import subprocess


'''
SSH client is used within the definition
output is decoded with .decode before output is returned with y
'''
def ssh_connection(ip,user,passwd, command):
    client=paramiko.SSHClient()
    # If you wanted to use ssh keys instead, uncomment the line below
    #client.load_host_keys('/home/user/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        g=ssh_session.recv(1024)
        y=g.decode()
    return y
'''
This block uses ip.txt and uses the list for the ip variable. The text document has
to be just a list of ips
the username and password for the ssh connection will need to be applied below
also a text file with the list of IPs will need to be accessible, named (ip.txt)
'''
user=''
passs= ''

fh=open('ip.txt')
for line in fh:
    ip=line.strip()
    #print(ip)
    sshout=str(ssh_connection(ip, user, passs,'hostname'))
    #print(sshout)
    sshout1=str(ssh_connection(ip, user, passs,'ls -al /var/www'))
    #print(sshout1)
    #this appends or creates sshout.txt and stores the ip
    #along with the hostname and contents of the /var/www directory
    with open('sshoutput.txt', 'a') as file:
        file.write('The following is:' + ip)
        file.write(' ' + sshout)
        file.write(sshout1)

#closes the document
fh.close()