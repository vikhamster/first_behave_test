import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass
from nose.tools import eq_
import yaml


# Config file loading
with open('qa.yaml', 'r') as f:
    config = yaml.load(f)


# Server ini
server_name = config['server_name']
server = smtplib.SMTP(server_name)


def get_active_sender_login():
    sender_name = config['active_sender']['sender_name']
    return sender_name


def get_active_sender_password():
    sender_password = config['active_sender']['sender_password']
    return sender_password


def auth(login, password):
    server.ehlo()
    login = server.login(login, password)
    return login[0]
