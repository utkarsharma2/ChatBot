import smtplib

user_id = 'postmaster@sandbox418cf31285a1465fb3c25cff4ba476b2.mailgun.org'
user_password = '2b1d910d1a368f92941595fddc176e16-53c13666-c38d6ff0'

def trigger_email(self, sent_to, email_body):
	sent_from = user_id
	to = sent_to
	subject = 'Your Restaurent test results'
	body = email_body

	email_text = """\
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (sent_from, ", ".join(to), subject, body)


	server = smtplib.SMTP_SSL('smtp.mailgun.org', 465)
	server.ehlo()
	server.login(user_id, user_password)
	server.sendmail(sent_from, to, email_text)
	server.close()
