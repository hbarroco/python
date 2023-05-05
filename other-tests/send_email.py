import smtplib
import Utility
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender email credentials
sender_email = "unittesthtb.noreplay@gmail.com"

password_file_path = '/home/hbarroco/Documents/Notes/file_gmail_app_password.txt'
sender_password = Utility.read_passwords_file(password_file_path)

# Recipient email address
recipient_email = "heliobarroco@gmail.com"

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = "Subject of the email"

body = "This is the body of the email."
msg.attach(MIMEText(body, 'plain'))

# Create a SMTP server object
server = smtplib.SMTP('smtp.gmail.com', 587)

# Start the SMTP session
server.starttls()

# Login to the SMTP server
server.login(sender_email, sender_password)

# Send the email
text = msg.as_string()
server.sendmail(sender_email, recipient_email, text)

# Close the SMTP session
server.quit()

print("Email sent successfully.")


