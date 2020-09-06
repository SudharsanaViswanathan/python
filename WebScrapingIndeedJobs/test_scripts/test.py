import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from email.mime.base import MIMEBase

from email import encoders


template_file_name = 'email_template.html'
mail_content = open(template_file_name, mode='r',encoding='utf-8')
#mail_content =str(open(template_file_name,"a").encode("utf-8"))

print(mail_content.read())

#The mail addresses and password

# sender_address = 'f0cc08d960367a'

# sender_pass = 'c6c62ef4cf23ef'

# receiver_address = 'thansudharsana@gmail.com'

# #Setup the MIME

# message = MIMEMultipart()

# message['From'] = sender_address

# message['To'] = receiver_address

# message['Subject'] = 'A test mail sent by Python. It has an attachment.'

# #The subject line

# #The body and the attachments for the mail

# message.attach(MIMEText(mail_content, 'html', 'utf-8'))

# attach_file_name = 'test.txt'

# attach_file = open(attach_file_name, mode = 'r',encoding='utf-8' ) # Open the file as binary mode

# payload = MIMEBase('application', 'octate-stream')

# payload.set_payload((attach_file).read())

# encoders.encode_base64(payload) #encode the attachment

# #add payload header with filename

# payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)

# message.attach(payload)

# #Create SMTP session for sending the mail

# session = smtplib.SMTP('smtp.mailtrap.io', 2525) #use gmail with port

# session.starttls() #enable security

# session.login(sender_address, sender_pass) #login with mail_id and password

# text = message.as_string()

# session.sendmail(sender_address, receiver_address, text)

# session.quit()

# print('Mail Sent')
