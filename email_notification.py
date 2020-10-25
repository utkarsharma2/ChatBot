import smtplib

gmail_user = 'postmaster@sandbox418cf31285a1465fb3c25cff4ba476b2.mailgun.org'
gmail_password = '2b1d910d1a368f92941595fddc176e16-53c13666-c38d6ff0'

sent_from = gmail_user
to = 'vishnu.ayyagari@gmail.com'
subject = 'This is a test mail'
body = 'Hey, whats up?\n\n- You'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)


server = smtplib.SMTP_SSL('smtp.mailgun.org', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, email_text)
server.close()

print ('Email sent!')
