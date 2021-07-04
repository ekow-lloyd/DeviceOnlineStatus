# a program that monitors the status of my home camera and sends an email when device is offline

import smtplib
import subprocess 

while True:
    result = subprocess.run(['ping', '-c', '3','-n', '192.168.0.136'],stdout=subprocess.PIPE)

    outcome = result.returncode

    if outcome == 0:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        test= smtpObj.ehlo()      # establish a test connection, response 250 means succesful connection.
        encrypt = smtpObj.starttls()
        signIn = smtpObj.login('ekowlloyd@gmail.com','M@rley-Afeni2020')
        sendMsg = smtpObj.sendmail("ekowlloyd@gmail", "lloyd.stewart@alpro.com", "Subject: Status : Online \nYo stewart, Your device is still online.\nKind Regards")
        {}
        signOut = smtpObj.quit()

        print("\n Success!! \n")

        print(signOut)
        print()
        quit()
        
    else:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        test = smtpObj.ehlo()
        encrypt = smtpObj.starttls()
        signIn = smtpObj.login('myemail@gmail.com','Pa55wordwith"5"') # credentials to log in to email-account
        sendMsg = smtpObj.sendmail("myemail@gmail", "receipeintemail@gmail.com", "Subject: Alert!! \nYo stewart, Device is Offline.\nKind Regards")
        {}
        signOut = smtpObj.quit()

        print('\n Failed!! \n')
        print(signOut)





