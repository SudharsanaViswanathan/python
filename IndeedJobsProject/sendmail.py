import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from email.mime.base import MIMEBase

from email import encoders
from datetime import date

today = date.today().strftime("%d_%m_%Y")

template_file_name = 'email_template.html'
mail_content = open(template_file_name, mode='r',encoding='utf-8').read()

#The mail addresses and password

sender_address = 'f0cc08d960367a'

sender_pass = 'c6c62ef4cf23ef'

receiver_address = 'viswanathansudharsana@gmail.com'

#Setup the MIME

message = MIMEMultipart()

message['From'] = sender_address

message['To'] = receiver_address

message['Subject'] = 'Indeed Job Posting'

#The subject line

#The body and the attachments for the mail

message.attach(MIMEText(mail_content, 'html', 'utf-8'))

attach_file_name = 'jobs.csv'

attach_file = open(attach_file_name, mode = 'r',encoding='utf-8' ) # Open the file as binary mode

payload = MIMEBase('application', 'octate-stream')

payload.set_payload((attach_file).read())

encoders.encode_base64(payload) #encode the attachment

#add payload header with filename

payload.add_header('Content-Disposition', 'attachment', filename='jobs_'+today+'.csv')

message.attach(payload)

#Create SMTP session for sending the mail

session = smtplib.SMTP('smtp.mailtrap.io', 2525) #use gmail with port

session.starttls() #enable security

session.login(sender_address, sender_pass) #login with mail_id and password

text = message.as_string()

session.sendmail(sender_address, receiver_address, text)

session.quit()

print('Mail Sent')
