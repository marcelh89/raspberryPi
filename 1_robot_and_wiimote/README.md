this is a fork of the original raspirobotboard repo
===============

It includes:

1. Source for the RaspiRobotBoard Python library.
2. Modification for using the RaspiRobotBoard with WiiMote Bluetooth

For full instructions to RaspiRobotBoard Installation the for installation and use, see:
https://github.com/simonmonk/raspirobotboard/wiki

### Installation
1. Install Bluetooth and wiimote libs see

	    sudo apt-get update
        sudo apt-get upgrade
        
        sudo apt-get install bluetooth
        sudo service bluetooth status
        hcitool dev
        sudo apt-get install python-cwiid
	

[full instructions](http://www.brianhensley.net/2012/08/wii-controller-raspberry-pi-python.html)
2. Install RaspiRobotBoard

		sudo apt-get install python-rpi.gpio
	    sudo apt-get install python-serial
    
        cd raspirobotboard
        sudo python setup.py install

[full instructions](https://github.com/simonmonk/raspirobotboard/wiki/Tutorial-01---Getting-Started)

 
3. execute python script

		python wiimote_robot.py



