#-------------------------------------------------------------------------------
# Name:        Wii Remote - connect to Bluetooth cwiid
# Purpose:
#
# Author:      Brian Hensley
#
# Created:     21/07/2012
# Copyright:   (c) Brian 2012
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import cwiid
import time
from raspirobotboard import *

def main():

	rr = RaspiRobot()
	moving = False

        print 'Press button 1 + 2 on your Wii Remote...'
        time.sleep(1)

        wm=cwiid.Wiimote()
	print 'Wii Remote connected...'
	print '\nPress the PLUS button to disconnect the Wii and end the application'
        time.sleep(1)
	
	Rumble = False
        wm.rpt_mode = cwiid.RPT_BTN
	
	position = 50
	print 'starting position: ', position

        while True:
	    #left
            if wm.state['buttons'] == 2048:
		if position > 0:
			position = position - 10
                	#print 'Left button pressed \n'
			print 'Position: ', position
		
		if moving:
			#only adjust direction, no stopping like e.g. motor right slower that motor left
			pass
		else:
			rr.left(0.05)
		#time.sleep(.5)

            #right
	    if wm.state['buttons'] == 1024:
		if position < 100:
			position = position + 10
                	#print 'Right button pressed \n'
			print 'Position: ', position

		if moving:
			#only adjust direction, no stopping like e.g. motor right slower that motor left
			pass
		else:
                	rr.right(0.05)

		#time.sleep(.5)

            #up
	    if wm.state['buttons'] == 512:
		position = 50
		print 'Position: ', position
		rr.forward(0.05)
		#time.sleep(.5)
            
	    #down
	    if wm.state['buttons'] == 256:
		#set_motors spins forever so set stop after sleep
	        rr.set_motors(1,1,1,1)
		time.sleep(.05)
		rr.stop()

            #button1
            if wm.state['buttons'] == 2:
                print 'Button 1 pressed'
                rr.forward()
		moving = True
		time.sleep(.5)

	    #button2
            if wm.state['buttons'] == 1:
                print 'Button 2 pressed'
                rr.stop()
		moving = False
		time.sleep(.5)
	    
	    #plus button
	    if wm.state['buttons'] == 4096:
		print 'closing Bluetooth connection. Good Bye!'
		time.sleep(1)
		exit(wm)


if __name__ == '__main__':
    main()

