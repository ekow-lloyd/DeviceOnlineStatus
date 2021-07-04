# a program that monitors the status of my home camera and sends an email when device is offline

import smtplib
import subprocess 

while True:
    result = subprocess.run(['ping', '-c', '3','-n', '192.168.0.136'],stdout=subprocess.PIPE). # the ping command and IP address of my camera

    outcome = result.returncode

    if outcome == 0:  # a return code of '0' means succesful ping, then this block of code sends a success report
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        test= smtpObj.ehlo()      # establish a test connection, response 250 means succesful connection.
        encrypt = smtpObj.starttls()
        signIn = smtpObj.login('myemail@gmail.com','Pa55wordWith5')
        sendMsg = smtpObj.sendmail("myemail@gmail", "recipientemail@gmail.com", "Subject: Status : Online \nHi there, Your device is online and running.\nKind Regards")
        {}
        signOut = smtpObj.quit()

        print("\n Success!! \n")
        
        print(signOut)
        print()
        quit()
        
    else:  # if the return code was anything other than '0', means a failure and device is down, so an alert email is sent
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        test = smtpObj.ehlo()
        encrypt = smtpObj.starttls()
        signIn = smtpObj.login('myemail@gmail.com','Pa55wordwith"5"') # credentials to log in to email-account
        sendMsg = smtpObj.sendmail("myemail@gmail", "recipientemail@gmail.com", "Subject: Alert!! \nHi there, Device is Offline.\nKind Regards")
        {}
        signOut = smtpObj.quit()

        print('\n Failed!! \n')
        print(signOut)





