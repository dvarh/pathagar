#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2012 Aneesh Dogra <aneesh@activitycentral.com>


"""Fabric settings file."""

SETTINGS = {}


#
# SSH connection for Fabric
#

#: List of hosts to work on
SETTINGS['hosts'] = ['localhost']
#: Username to log in in the remote machine
SETTINGS['user'] = 'root'


#
# Database
#

# DB name
SETTINGS['db_name'] = 'pathagarh'

# DB user will be used for creating the database
SETTINGS['db_user'] = 'pootle'

SETTINGS['db_password_opt'] = '-p'

#
# Project
#

#: A meaningful name for your Pootle installation
SETTINGS['project_name'] = 'pootle-staging'
#: This URL will be used in the VirtualHost section
SETTINGS['project_url'] = 'my-pootle.example.com'
#: Change the first path part if your Apache websites are stored somewhere else
SETTINGS['project_path'] = '/var/www/sites/%s' % SETTINGS['project_name']


#
# The rest of the settings probably won't need any changes
#

SETTINGS['project_repo_path'] = '%s/src' % SETTINGS['project_path']
SETTINGS['project_repo'] = 'https://github.com/PathagarBooks/pathagar.git'
SETTINGS['project_settings_path'] = '%s/pathagar/settings' % \
                                        SETTINGS['project_repo_path']

#
# Secret key
#

from base64 import b64encode
from os import urandom
SETTINGS['secret_key'] = b64encode(urandom(50))


#
# Virtualenv
#

#: Python version that will be used in the virtualenv
SETTINGS['python'] = 'python2.7'
SETTINGS['env_path'] = '%s/env' % SETTINGS['project_path']


#
# Apache + VirtualHost + WSGI
#

#: The group your web server is running on
SETTINGS['server_group'] = 'www-data'
SETTINGS['vhost_file'] = '/etc/apache2/sites-available/%s' % \
                                SETTINGS['project_name']
SETTINGS['wsgi_file'] = '%s/src/wsgi.py' % SETTINGS['project_path']