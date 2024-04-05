import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import time

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach body text
    msg.attach(MIMEText(body, 'plain'))

    # Attach tracking image (replace image_path with the path to your tracking image)
    image_path = 'path/to/your/tracking/image.png'
    with open(image_path, 'rb') as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-ID', '<tracker>')
        msg.attach(img)

    # Connect to SMTP server and send email
    smtp_server = 'smtp.gmail.com'  # Change to your SMTP server
    smtp_port = 587  # Change to your SMTP port
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

def track_email_open():
    print("Tracking email open...")
    # This is where you would record the email open event, such as updating a database or sending a notification

if __name__ == "__main__":
    sender_email = 'your_email@gmail.com'  # Replace with your email
    sender_password = 'your_password'  # Replace with your email password
    receiver_email = 'recipient_email@example.com'  # Replace with recipient's email
    subject = 'Test Email with Tracking'
    body = 'This is a test email with a tracking image.'

    # Send the email
    send_email(sender_email, sender_password, receiver_email, subject, body)

    # Simulate email open after 5 seconds (you can adjust this time as needed)
    time.sleep(5)
    track_email_open()
