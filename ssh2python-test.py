from __future__ import print_function

import os
import socket

from ssh2.session import Session

host = 'remote FTP server IP'
username = 'root'
password = 'password'
port = 22

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

session = Session()
session.handshake(sock)
session.userauth_password(username, password)

def command_exec(laa,ftpaccountuser, ftpaccountpassword):
    channel = laa.open_session()
    channel.execute('')
    size, data = channel.read()
    while size > 0:
        print(data.decode())
        channel.write('1\n')
        size, data = channel.read()
        print(data.decode())
        channel.write(ftpaccountuser+'\n')
        size, data = channel.read()
        print(data.decode())
        channel.write(ftpaccountpassword+'\n')
        channel.write('\n')
    channel.close()


def deleteFtpUser(laa,ftpaccountuserdel):
    channel = laa.open_session()
    channel.execute('')
    size, data = channel.read()
    while size > 0:
        print(data.decode())
        channel.write('2\n')
        size, data = channel.read()
        print(data.decode())
        channel.write(ftpaccountuserdel+'\n')
        size, data = channel.read()
        print(data.decode())
    channel.close()

def updateFtpUser(laa,ftpaccountuserupdate, newpassword):
    channel = laa.open_session()
    channel.execute('')
    size, data = channel.read()
    while size > 0:
        print(data.decode())
        channel.write('3\n')
        size, data = channel.read()
        print(data.decode())
        channel.write(ftpaccountuserupdate+'\n')
        size, data = channel.read()
        print(data.decode())
        channel.write(newpassword+'\n')
        size, data = channel.read()
        print(data.decode())
    channel.close()


#updateFtpUser(session,'PutTheUsernameYouWantToUpdateHere','PutTheNewPasswordHere')
#deleteFtpUser(session,'PutTheUsernameYouWantToDeleteHere')

#Here you have to replace with the username and 
# password of the ftp account you want to create
#command_exec(session,'abdelah','abdelah')



