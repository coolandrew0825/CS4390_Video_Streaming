import sys
from Tkinter import Tk
from ClientThreeButton import ClientThreeButton

if __name__ == "__main__":
	try:
		serverAddr = sys.argv[1]
		serverPort = sys.argv[2]
		rtpPort = sys.argv[3]
		fileName = sys.argv[4]	
	except:
		print "[Usage: ClientThreeButtonLauncher.py Server_name Server_port RTP_port Video_file]\n"	
	
	root = Tk()
	
	# Create a new client
	app = ClientThreeButton(root, serverAddr, serverPort, rtpPort, fileName)
	app.master.title("RTPClientThreeButton")	
	root.mainloop()
	