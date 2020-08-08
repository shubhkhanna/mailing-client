import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg['From'] = ' '  # Add sender name here.
msg['To'] = ' '  # Add receiver mail id here.
msg['Subject'] = 'Testing Mailing Client!'  # Add your own subject.

# For reading message from msg.txt file.
with open('msg.txt', 'r') as f:
    message = f.read()

# For attaching message for the mail.
msg.attach(MIMEText(message, 'plain'))

# smtp server of your provider & port number.
server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()  # For enabling security.

# For reading your account password from password.txt file.
with open('password.txt', 'r') as f:
    password = f.read()

sender_mail = ' '  # Add sender mail id here.
receiver_mail = ' '  # Add receiver mail id here.

# For login into your Gmail account.
server.login(sender_mail, password)

text = msg.as_string()

server.sendmail(sender_mail, receiver_mail, text)

server.quit()

print('Your Mail has been sent')
