import subprocess
import datetime
import smtplib, ssl
from config import Config


def send_email():
    # For SSL
    port = Config.MAIL_PORT_SSL

    # mail server
    smtp_server = Config.MAIL_SERVER

    # your address
    sender_email = Config.MAIL_USERNAME

    # receiver address
    receiver_email = Config.MAIL_RECEIVER

    # sender mail configuration
    password = Config.MAIL_PASSWORD
    message = Config.MAIL_MESSAGE

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email.split(','), message)


def arp_a():
    # IP address to look for
    address = Config.LOOK_FOR_IP
    # MAC address is present
    mac_address = Config.LOOK_FOR_MAC
    res = str(subprocess.run(['arp', '-a'], capture_output=True))
    if address and mac_address in res:
        send_email()
    else:
        print("PC was off:" + ' ' + str(datetime.datetime.now()))
