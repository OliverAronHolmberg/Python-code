import smtplib

sender = "oliver@systementor.se"
receiver = "kerstin.holmberg@systementor.se"
password = "Musse2022"
subject = "Python email test"
body = "Musse nusse"

# header
message = f"""From: Musse nusse{sender}
To: Musse Nusse{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")