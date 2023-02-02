# Driverless Code Design Report

## INTRODUCTION
The telemetry system is a system that consists of the following components:

Receiver.py:
This script is responsible for receiving the data sent from the car and displaying it in the console where the script is run.
The data that is displayed consists of 2 ground speed sensor, wheel encoders data, the values that are sent to the actuator (Brake, Accelerator and steering angle), and the values that are sent from the camera to the PC (A list with cone number, angle, distance and label).
This script listens for connections. When a connection is made it starts receiving, displaying data and writing the data to a file. The IP of the machine has to be entered to create a socket aswell as a suitable port.

Transmitter.py
This script is responsible for transmitting the values previously mentioned to the receiver.py script. This script using websockets to accomplish this. The IP and port of the receiving party have to be entered. The script generates mock data to simulate the real data coming in. The real data has to be wrapped in a JSON object. These values can then be sent to the receiver.py script. The ZeroTier IP from the receiving PC needs to be entered in this script aswell as the same port as defined in the receiving script.

4G Modem/Router
The 4G Modem/Router is responsible for providing internet access to the car to send the values to a PC at the side of the track. This PC at the side of the track also requires internet access.

ZeroTier Virtual Network
In order to make the transfer of data work a virtual local network has to be made in order to circumvent closed ports. An alternative to this is opening ports but this opens the PC's up to security risks. A complete manual for configuring and installing this network is available on the Drive.

## RULES AND DEMANDS
There are rules for antenna placement and size of the antenna specificis can be found in the rulebook.
The system has to have a relatively low latency. This is dependent on coverage at the racetrack.

## RESEARCH
A complete research document is available on the Google Drive describing the research done for the system.

## CODING PROCESS
The Websockets script from the datalogger has been altered to the needs of this system. Coding process was similar to the datalogger.

## TESTING
The system was tested using a simulated enviroment. A laptop was configured with the ZeroTier Virtual Network and connected to the internet using WIFI. The transmitting script was then run on a different PC also configured with the same ZeroTier Virtual Network and connected to the internet using a 4G on a Phone with a WIFI hotspot.
It was checked if the data was transmitted and received correctly. 

## CONLCUSION/DISCUSSION
A Telemetry system capable of transmitting data over the internet was developed.
The only work that still needs to be done is getting the real data from the sensors en etc into this script.
