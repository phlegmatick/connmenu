# connmenu - a simple SSH connection menu


## Description

A simple console-based SSH connection menu, fed by an INI style configuration file

## Usage

Just execute it. Optionally provide a configuration file as an argument.

## Dependencies

cursesmenu (pip install curses-menu)

## Configuration example

	;This is a comment
	[Dev]
	devbox:192.168.0.5,username,passw0rd
	[Production]
	prod01:10.10.10.11,user,pass
	prod02:10.10.10.12,user,hunter2
