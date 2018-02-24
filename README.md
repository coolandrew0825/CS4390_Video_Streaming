# CS4390_Video_Streaming
class name: data structure
programming language: Python

How to run the files:
1)	Open Command Console
2)	Use cd to get to the directory where the project files are
3)	Use “python Server.py 1025”
4)	Server is now running
5)	Open New Command Console
6)	Go to project directory again
7)	Use python ClientLauncher.py <SYSTEMNAME> 1025 1026 movie.Mjpeg
8)	A GUI should come up
9)	Click the setup button
10)	Click the play button
11)	Click the pause button
12)	Click the teardown button when the video finishes running

Instructions on installing PIL imaging library
1)	Download the Python Imaging Library
2)	Install PIL to Python 2.7
3)	Open System Menu
  I)	Go to Start Menu
  II)	Right Click Computer and Hit “Properties”
  III)	Click “Advanced System Settings”
  IV)	Click “Environment Variables”
  V)	Select PATH variable and hit EDIT
  VI)	If PATH variable not present, hit New to add a variable called PATH
  VII)	Add the path to the Python directory as the value of the PATH variable
  VIII)	Now you can use the python command in the Command Console without entering the full filepath every single time

SPECIAL NOTE
1. THREE BUTTON LAYOUT CLIENT
Please wait until the console reports that the RTP Listener is dying before executing another command when you execute a Pause or a Stop. Trying to execute any command before this WILL cause instability in the program.
