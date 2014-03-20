from curses import wrapper
from os.path import expanduser
import curses

import os.path
import configparser

selectedOption = 0
searchString = "this is some long test string that is just meant to be a long test string that is just meant to be a long test string that is meant to be just a long... yeah you get the idea"
searchStringPos = 0
searchBoxButtonText = "Search"

#windows
searchBox = 0
searchWindow = 0


def main(stdscr):
	global searchWindow
	global searchBox

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

	#create search box for search window (the thing you type into)
	searchBox = curses.newwin(3,
		searchWindow.getmaxyx()[1] - 2 - len(searchBoxButtonText), 1, 1)

	searchWindow.box(0, 0)
	drawSearchWindow(searchWindow)

	while True:
		pass


def drawSearchWindow(searchWindow):
	global searchBox

	searchWindow.move(0, 2)
	searchWindow.addstr("Search", curses.color_pair(1) | curses.A_BOLD)

	#add searchbutton
	searchWindow.move(2,
		searchWindow.getmaxyx()[1] - len(searchBoxButtonText) - 1)

	if selectedOption == 1:
		searchWindow.addstr(searchBoxButtonText,
			curses.color_pair(3) | curses.A_BOLD)
	else:
		searchWindow.addstr(searchBoxButtonText,
			curses.color_pair(2) | curses.A_BOLD)

	#create search box
	searchBox.box(0, 0)
	drawSearchBox(searchBox)

	#use a pad for the entered string
	searchStringPad = curses.newpad(1, len(searchString) + 1)
	searchStringPad.addstr(searchString)

	searchWindow.refresh()
	searchBox.refresh()
	searchStringPad.refresh(0, 0, 2, 2, 2, searchBox.getmaxyx()[1] - 1)


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
