#!/usr/bin/python
# coding: UTF-8
import os
os.system("ansible-galaxy install -r install_roles.yml -vvvv")
os.system("ansible-playbook -i inventory site.yml")
