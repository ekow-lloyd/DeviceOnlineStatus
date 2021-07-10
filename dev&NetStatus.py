import smtplib
import subprocess

# a list to store which devicess are online or offline
Online = []
Offline = []

# a function to send mail for online device
# take the log in of email and password to set-up an SMTP connection

def sendMail():
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login("myemail@gmail.com","mypassword")
    smtpObj.sendmail("myemail@gmail.com", "recipientemail@gmail.com", "Subject:Online \nHi Lloyd,\nThe following {} device(s) are currently online : {}.\n\nCheers,\nPythonBlac".format(numOnline,Online))
    smtpObj.quit()

# a function to send mail of offline devices (to avoid complexity i made two function, but one mail could inform of the offline statuses are well)
def mailFail():
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login("myemail@gmail.com","mypassword")
    smtpObj.sendmail("myemail@gmail.com","recipientemail@gmail.com","Subject:Offline \nHi Ekow,\nThe following {} device(s) are currently offline : {}\n\ncheers,\nPythonBlac".format(numOffline,Offline))
    smtpObj.quit()

# a pre-defined list containing the IP addresses of the devices i want to check
# open the text file in read mode and extract the IP addresses, stripping the 'white space' at the end of the file object
# the output of the ping command gets stored in the variable 'Outcome', an Outcome of 0 means successful, so Online list gets appended and same for Offline list if outcome is not 0

with open('pinglist.txt', 'r') as readfile:
    for IP in readfile:
        print('')
        print(IP.rstrip())
        print('Pinging:', IP.rstrip())
        result = subprocess.run(['ping', '-c', '1','-n', IP.strip()],stdout=subprocess.PIPE)
        outcome = result.returncode

        if outcome == 0:
            Online.append(IP.rstrip())
            print("Status: Online")
            print('Updating List for confirmation mail....')
            
        else:
            if outcome != 0:
                Offline.append(IP.rstrip())
                print("Status: Down")
                print('Updating list for Notification mail')

numOnline = len(Online)     
numOffline = len(Offline)           
sendMail()
mailFail()

print('')
print('Exiting Status Check')
print('')
