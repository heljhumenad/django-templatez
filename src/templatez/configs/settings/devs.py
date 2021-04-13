from templatez.configs.settings.base import *


DEBUG = True

# Add automaticaly machine ip address
def get_ipaddress():
    import socket
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    return ip_address

# You can put your own hostname to test the production base environment
ALLOWED_HOSTS = [get_ipaddress(), 'localhost', '127.0.0.1']

# Custom INSTALLED_APPS for development environment
INSTALLED_APPS += []

# Custom MIDDLEWARE component
MIDDLEWARE +=[]

# Add your Custom Authentication Model
# AUTH_USER_MODEL = ''


# Email Server Configurations
SMTP_PORT = 443
POP3_PORT = 110
IMAP_PORT = 143

# Encrypted Port
POP3_SECURE_PORT = 995
IMAP_SECURE_PORT = 993

# Email Configurations variable
EMAIL_HOST = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = POP3_PORT

# Email Security
# You can set one to True if TLS or SSL is present in your email
# Configurations of your server
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False


