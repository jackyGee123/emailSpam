import smtplib
import time
import random

from email.Header import Header
from email.mime.text import MIMEText
#Open a file for reading

me = 'Jackygee2013@gmail.com' # change to your email
p_reader = open('Jackygee6509', 'rb') 
cipher = p_reader.read()
recipients = ['jackygee6509@gmail.com'] 


def spamEveryMinute():
    while (True):
        fp = open('message.txt', 'rb')
        msg = MIMEText(fp.read(), 'plain', 'utf-8')
        fp.close()

        thread_number = random.randint(0, 10000)
        msg['Subject'] = Header('Minutely Spam Report (randomizer: ' + str(thread_number) + ')', 'utf-8')
        msg['From'] = me
        msg['To'] = ', '.join(recipients)

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(me, cipher)
        s.sendmail(me, recipients, msg.as_string())

        print "Email sent to: " + ', '.join(recipients)
        s.quit()
        time.sleep(60) 

spamEveryMinute()
