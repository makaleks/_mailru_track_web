#!/usr/bin/env python2

import os

os.system("sudo systemctl start mysqld")
os.system("sudo systemctl start nginx")
os.system("sudo systemctl start rabbitmq")
