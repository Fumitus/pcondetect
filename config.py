import os


class Config:
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT_SSL = int(os.environ.get('MAIL_PORT_SSL'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_MESSAGE = os.environ.get('MAIL_MESSAGE') or \
    """\
    Subject: Labas teveliai

    Lukas isijunge PS4. Paskambink jam ir primink apie laiko limita.\
    
    PS4
    """
    MAIL_RECEIVER = os.environ.get('MAIL_RECEIVER')
    LOOK_FOR_IP = os.environ.get('LOOK_FOR_IP')
    LOOK_FOR_MAC = os.environ.get('LOOK_FOR_MAC')

