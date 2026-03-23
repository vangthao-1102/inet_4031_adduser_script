#!/usr/bin/python3

# INET4031
# Vang
# 3/22/26
# 3/22/26

#os = loads Python's built-in operating system module (allows for certain OS scripts to be allowed in the program)
#re = brings in regular expressions. a tool that allows to search, match, or manipulate text using patterns instead to exact characters
#sys = brings in the ability to let the program interact with python interpreter 
import os
import re
import sys

#main body of code begins below
def main():
    #loops through a file 
    for line in sys.stdin:

	#variable represents the automatic search of a character in a file. this takes a look the first string of the file to make sure
	#it is correct. if it is correct, it succeeds which shows us that the file is correct
        match = re.match("^#",line)

        #fields is a variable. this whole thing is just to allow for the file to be split by the symbol : (the file uses that character)
        fields = line.strip().split(':')

	#checks bewtween the two vairables. if one is true, it passes the check and continues. != 5 for fields is based on the file read
        if match or len(fields) != 5:
            continue

	#purpose is to keep track of the file variables. fields is now a list, remember. third line keeps track of first and last name
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #this allows for if there are users in multiple groups. the split allows for better read of that information
        groups = fields[4].split(',')

        #showing that account is being created for specificed user
        print("==> Creating account for %s..." % (username))
	#goes into the command line and automatically updates the adduser to the new user that has been created
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

	#print(cmd) will print out what the cmd variable contains. then os.system() will execute the variable.
        print(cmd)
        os.system(cmd)

        #shows that a password is being set for a certain user
        print("==> Setting the password for %s..." % (username))
        #all this does is automatically setup the password for the user
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

	#os.system will attempt to automatically assign passwords to users
        print(cmd)
        os.system(cmd)

        for group in groups:
	    #if statement looks for if users do not belong to group. if the user does belong to a group, assign accordingly
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
