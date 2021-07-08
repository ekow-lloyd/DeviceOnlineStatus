# a program that monitors the status of my home camera and sends an email when device is offline

import smtplib
import subprocess 

Online = []
Offline = []

def sendMail():
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login("myemail@gmail.com","mypassword")
    smtpObj.sendmail("myemail@gmail.com", "recipientemailt@gmail.com", "Subject:Device State \nHi Lloyd,\nthe following device(s) are Online at time of mail: {}.\nCheers,\nPython".format(Online))
    smtpObj.quit()

sendMail()


def mailFail():
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login("myemail@gmail.com","mypassword")
    smtpObj.sendmail("myemail@gmail.com","myemail@gmail.com","Subject:Alert \nHi there,\nthe following device(s)are offline : {}".format(Offline))
    smtpObj.quit()
mailFail()


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
            print('Sending confirmation mail....')
            sendMail()
        else:
            if outcome != 0:
                Offline.append(IP.rstrip())
                print("Status: Down")
                print('Sending Notification mail')
                mailFail()

print('Exiting Status Check')
print('')





