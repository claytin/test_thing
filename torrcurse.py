#windows
from curses import wrapper
from os.path import expanduser
import curses

import os.path
import configparser

selectedOption = 0
searchString = ""
searchStringPos = 0
searchStringPadPos = 0
searchBoxButtonText = "Search"

#windows
searchBox = 0
searchWindow = 0


def main(stdscr):
	global searchString
	global searchStringPos
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
	drawSearchWindow()

	while True:
		key = stdscr.getch()
		#stdscr.addstr(stdscr.getmaxyx()[0] - 1,
		#	stdscr.getmaxyx()[1] - 1 - len(str(key)), str(key) + "")

		if key == 0:
			pass
		if key == 261:
			moveSelect("right")
		if key == 260:
			moveSelect("left")
		if key >= 32 and key <= 126:
			searchString = searchString[:searchStringPos] + \
				str(chr(key)) + searchString[searchStringPos:]
			#searchStringPos += 1
			moveSelect("right")
			#drawSearchWindow()
		if key == 127 and searchStringPos > 0:
			searchString = searchString[:searchStringPos - 1] + \
				searchString[searchStringPos:]
			searchStringPos -= 1
			drawSearchWindow()


def moveSelect(direction):
	global searchStringPos
	global searchStringPadPos

	if direction == "right" and searchStringPos < len(searchString):
		if searchStringPos - searchStringPadPos > searchBox.getmaxyx()[1] - 4:
			searchStringPadPos += 1
		searchStringPos += 1
		drawSearchWindow()
	elif direction == "left" and searchStringPos > 0:
		if searchStringPos - searchStringPadPos < 1:
			searchStringPadPos -= 1
		searchStringPos -= 1
		drawSearchWindow()


def drawSearchWindow():
	global searchBox
	global searchStringPadPos

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

	#use a pad for the entered string
	searchStringPad = curses.newpad(1, len(searchString) + 1)
	searchStringPad.addstr(searchString)

	searchWindow.refresh()
	searchBox.refresh()
	searchStringPad.refresh(0, 0 + searchStringPadPos,
		2, 2, 2, searchBox.getmaxyx()[1] - 1)

	searchBox.move(1, 1 + searchStringPos - searchStringPadPos)
	searchBox.refresh()

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
