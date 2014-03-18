from curses import wrapper
from os.path import expanduser
import curses

import os.path
import configparser


def main(stdscr):
	stdscr.clear()
	stdscr.refresh()

	curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)

	#create search window
	searchWindow = curses.newwin(10, 10, 10, 10)
	searchWindow.box(0, 0)

	while True:
		pass


def drawSearchWindow(searchWindow):
	searchWindow.move(0, 2)
	searchWindow.addstr("Search", curses.color_pair(1) | curses.A_BOLD)


#get config before calling ncurses
home_dir = expanduser("~")
config_dir = home_dir + "/.config/"
config_file = config_dir + "torrn"

print("using " + config_dir + " for configs")
print("checking config file at " + config_file)

#check if the config file exists
if os.path.isfile(config_file):
	#if so then read from it
	print("yep")

	config = configparser.ConfigParser()
	config.read(config_file)

	default = config['DEFAULT']

	#yeah... it's not done yet...
	try:
		site = default["site"]
	except KeyError:
		site = "swaswaswa"

else:
	#if not then create a config file with the defaults
	print("creating a default config... Just because")

	#create config
	#config = configparser.ConfigParser()
	#config['DEFAULT'] = {'a': '45', 'b': '123', 'c': '321'}
	#with open("default.conf", 'w') as configfile:
	#	config.write(configfile)


wrapper(main)
