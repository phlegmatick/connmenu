#!/usr/bin/env python
"""
ConnMenu: a simple SSH connection menu
Author: Blake Buckalew
Version: 1
Description: A simple console-based SSH connection menu, fed by an INI style configuration file
Usage: Just execute it. Optionally provide a configuration file as an argument.
Dependencies: cursesmenu (pip install curses-menu)

Configuration example:
    ;This is a comment
    [Dev]
    devbox:192.168.0.5,username,passw0rd
    [Production]
    prod01:10.10.10.11,user,pass
    prod02:10.10.10.12,user,hunter2
"""
import ConfigParser, sys, subprocess
import os
from pprint import pprint
from cursesmenu import *
from cursesmenu.items import *

connMenu = True

# title settings
title = True # set terminal title to $hostLabel ($username)

exit_string = 'ConnMenu exiting...'

config_file = os.path.expanduser('~/connmenu.conf')

config_file = sys.argv[1] if (len(sys.argv) > 1) else config_file
print config_file

if not os.path.isfile(config_file):
    print "Configuration file not found!"
    print exit_string
    sys.exit()

hosts = ConfigParser.ConfigParser()
hosts.optionxform=str # preserve case in conn labels
hosts.read(config_file)

categories = hosts.sections()

#proceed = raw_input('\nPress enter to proceed.')

category_selection = SelectionMenu.get_selection( categories , 'Connection Categories')

try:
    category_name = categories[category_selection]
except IndexError:
    print exit_string
    sys.exit()
    
servers = hosts.items(category_name)

pprint(servers)

#proceed = raw_input('\nPress enter to proceed.')

selection = SelectionMenu.get_selection( [ s[0] for s in servers ] , category_name )

try:
    print servers[selection]
except IndexError:
    print exit_string
    sys.exit()

label = servers[selection][0]

serverconf = servers[selection][1].split(',')
print 'serverconf', serverconf


host = serverconf[0]
username, password = serverconf[1].strip(), serverconf[2]

connMenu = True
while connMenu:
    
    print "Connecting to %s..." % host
    command = "ssh '%s' -l %s" % ( host, username)
    print command
    
    if title:
        subprocess.call("xtitle \"%s (%s)\"" % (host.split('.')[0].strip(), username), shell=True)
    
    # Launch interactive SSH
    subprocess.call(command, shell=True)
    
    # Exit logic
    exitOption = raw_input('\nSSH exited. [R]econnect or any other key to exit: ')
    
    if exitOption.strip().upper() != 'R':
        sys.exit()