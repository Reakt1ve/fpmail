from pprint import pprint
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib

def send_mail():
	#create message object instance
	msg = MIMEMultipart()
	message = "Attachment"

	# setup the parameters of the message
	msg['From'] = "user1@zapto.org"    # change value with TO
	msg['To'] = "info@zapto.org"     # change value with FROM
	msg['Subject'] = "Test"

	# add in the message body
	msg.attach(MIMEText(message, 'plain'))

	file = MIMEApplication(open('/home/alexeysenu/informator/encrypt/text.txt.asc', 'rb').read())
	file.add_header('Content-Disposition','attachment',filename="dbText.txt.asc")
	msg.attach(file)

	file = MIMEApplication(open("/home/alexeysenu/informator/encrypt/text.txt.sig", "rb").read())
	file.add_header('Content-Disposition','attachment',filename="dbText.txt.sig")
	msg.attach(file)

	#create server
	server = smtplib.SMTP('citismatrix.zapto.org:465')
	server.ehlo()
	server.starttls()

	# Login Credentials for sending the mail
	print(msg['From'])
	server.login(msg['From'], "qwerty123")

	# send the message via the server.
	server.sendmail(msg['From'], msg['To'], msg.as_string())

	server.quit()

	print "successfully sent email to %s:" % (msg['To'])


if __name__ == '__main__':
	send_mail()
