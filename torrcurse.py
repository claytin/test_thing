from curses import wrapper
from os.path import expanduser
import curses

import os.path
import configparser

selectedOption = 0


def main(stdscr):
	stdscr.clear()
	stdscr.refresh()

	#for window titles
	curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
	#unselected buttons
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	#selected buttons
	curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

	#create search window
	searchWindow = curses.newwin(7, stdscr.getmaxyx()[1], 0, 0)
	searchWindow.box(0, 0)
	drawSearchWindow(searchWindow)

	while True:
		pass


def drawSearchWindow(searchWindow):
	searchBoxButton = "Search"

	searchWindow.move(0, 2)
	searchWindow.addstr("Search", curses.color_pair(1) | curses.A_BOLD)

	#add searchbutton
	searchWindow.move(2, searchWindow.getmaxyx()[1] - len(searchBoxButton) - 1)
	if selectedOption == 1:
		searchWindow.addstr(searchBoxButton,
			curses.color_pair(3) | curses.A_BOLD)
	else:
		searchWindow.addstr(searchBoxButton,
			curses.color_pair(2) | curses.A_BOLD)

	#create search box
	searchBox = curses.newwin(3,
		searchWindow.getmaxyx()[1] - 2 - len(searchBoxButton), 1, 1)
	searchBox.box(0, 0)
	drawSearchBox(searchBox)

	#use a pad for the entered string
	searchStringPad = curses.newpad(1, 160)
	searchStringPad.addstr("012345678912345678|912345678|912345678|912345678|912345678|9")

	searchWindow.refresh()
	searchBox.refresh()
	searchStringPad.refresh(0, 0, 5, 5, 20, 75)


def drawSearchBox(searchBox):
	pass

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
