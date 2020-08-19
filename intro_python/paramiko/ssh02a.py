#!/usr/bin/python3
"""Learning about Python SSH | rzfeeser@alta3.com"""

# used to remove warnings from packages
import warnings

import paramiko
import csv
# filter out any warnings with the word Paramiko
warnings.filterwarnings(action="ignore", module=".*paramiko.*")

def readInUsers():
    with open('users.csv', mode='r') as file:
        csvFile = csv.reader(file)
    return csvFile

def main():
    """Our runtime code that calls other functions"""
    # describe the connection data
    users = readInUsers()
    #print(users)
   
    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa") 
    
    # loop across the collection credz
    for user in users:
        ## create a session object
        sshsession = paramiko.SSHClient()

        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ## display our connections
        print("Connecting to... " + user[0] + "@" + user[1])

        ## make a connection
        sshsession.connect(hostname=user[1], username=user[0], pkey=mykey)

        ## touch the file goodnews.everyone in each user's home directory
        sshsession.exec_command("touch /home/" + user[0] + "/goodnews.everyone")

        ## list the contents of each home directory
        sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + user[0])

        ## display output
        print(sessout.read().decode('utf-8'))

        ## close/cleanup SSH connection
        sshsession.close()

    print("Thanks for looping with Alta3!")

main()

