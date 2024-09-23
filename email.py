import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
username = 'skylineictltd@gmail.com'
password = 'tfpb teef wcmz ftzr'
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Email details
from_email = username
to_emails = ['skylineict@gmail.com', 'talk20rismac@gmail.com']  # List of primary recipients
cc_emails = ['macaulayskyline@gmail.com']  # List of CC recipients (optional)
bcc_emails = ['skylineictltd@gmail.com']  # List of BCC recipients (optional)
reply_to_email = 'replyto@example.com'  # Reply-To address
subject = 'Welcome to the Software Development Course'

# Combine all recipients for sending
all_recipients = to_emails + cc_emails + bcc_emails

# HTML content
html_content = """
<html>
  <body>
    <h2>Welcome to Our Software Development Course!</h2>
    <p>Dear User,</p>
    <p>Congratulations on being admitted to our <strong>Software Development Course</strong>!</p>
    <p>We are excited to have you on board as you begin your journey to becoming a skilled software developer.</p>
    <p>Please find attached your course materials and schedule.</p>
    <p>Best regards,</p>
    <p>Your Company Name</p>
  </body>
</html>
"""

# Creating the message
message = MIMEMultipart()
message['From'] = from_email
message['To'] = ', '.join(to_emails)  # Join list of 'To' emails into a single string
message['CC'] = ', '.join(cc_emails)  # Join list of 'CC' emails into a single string (optional)
message['Subject'] = subject
message['Reply-To'] = reply_to_email  # Set the Reply-To address

# Attach the HTML content
message.attach(MIMEText(html_content, 'html'))

# Sending the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, all_recipients, message.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
