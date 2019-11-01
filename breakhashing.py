import os
import sys
import hashlib




"""
Created By: TheTechHacker
================================
SUBSCRIBE: https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ
"""

if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")
elif sys.platform == "darwin":
    os.system("clear")
else:
    print ("Unknown System Detected")

class hashCracker:
    def __init__(self):
        print ("""
        \033[1;32m
            1)md5
            2)sha1
            3)sha224
            4)sha256
            5)sha384
            6)sha512
        \033[1;m
        """)
        self.hashchoice = input("\033[1;32m Enter Your choice: \033[1;m")
        self.hashed = input("\033[1;32m Enter You're Hash: \033[1;m")
        self.pwd = input("\033[1;32m wordlist: \033[1;m")
        self.cracker = open(self.pwd, "r")

    def md5(self):
        for log in self.cracker:
            log = log.strip()
            hashing = hashlib.md5(log.encode("utf-8")).hexdigest()
            upper_hashing = hashing.upper()
            print ("\033[1;32m Trying: {0} \033[1;m".format(log))

            if self.hashed == hashing or self.hashed == upper_hashing:
                print ("\033[1;34m [+] Hash Cracked: {0}\033[1;m".format(log))
                break

    def sha1(self):
        for log in self.cracker:
            log = log.strip()
            hashing = hashlib.sha1(log.encode("utf-8")).hexdigest()
            uppercase_hashing = hashing.upper()
            print ("\033[1;32mTrying: {0}\033[1;m".format(log))

            if self.hashed == hashing or self.hashed == uppercase_hashing:
                print ("\033[1;34m [+] Hash Cracked: {0}\033[1;m".format(log))
                break

    def sha224(self):
        for log in self.cracker:
            log = log.strip()
            hashing = hashlib.sha224(log.encode("utf-8")).hexdigest()
            uppercase_hashing = hashing.upper()
            print ("\033[1;32m Trying: {0}\033[1;m".format(log))

            if self.hashed == hashing or self.hashed == uppercase_hashing:
                print ("\033[1;34m [+] Hash Cracked: {0}\033[1;m".format(log))
                break

    def sha256(self):
        for log in self.cracker:
            log = log.strip()
            hashing = hashlib.sha256(log.encode("utf-8")).hexdigest()
            uppercase_hashing = hashing.upper()
            print ("\033[1;32m Trying: {0}\033[1;m".format(log))

            if self.hashed == hashing or self.hashed == uppercase_hashing:
                print ("\033[1;34m [+] Hash Cracked: {0}\033[1;m".format(log))
                break

    def sha384(self):
        for log in self.cracker:
            log = log.strip()
            hashing = hashlib.sha384(log.encode("utf-8")).hexdigest()
            uppercase_hashing = hashing.upper()
            print ("\033[1;32m Trying {0}\033[1;m".format(log))

            if self.hashed == hashing or self.hashed == uppercase_hashing:
                print ("\033[1;34m [+] Hash Cracked: {0}\033[1;m".format(log))
                break

    def sha512(self):
        for log in self.cracker:
            log = log.strip()
            hashing = hashlib.sha512(log.encode("utf-8")).hexdigest()
            uppercase_hashing = hashing.upper()
            print ("\033[1;32m Trying {0}\033[1;m".format(log))

            if self.hashed == hashing or self.hashed == uppercase_hashing:
                print ("\033[1;34m [+] Hash Cracked: {0}\033[1;m".format(log))
                break


crack = hashCracker()

if crack.hashchoice == "1":
    crack.md5()
elif crack.hashchoice == "2":
    crack.sha1()
elif crack.hashchoice == "3":
    crack.sha224()
elif crack.hashchoice == "4":
    crack.sha256()
elif crack.hashchoice == "5":
    crack.sha384()
elif crack.hashchoice == "6":
    crack.sha512()
else:
    print ("Select A Valid Option")
