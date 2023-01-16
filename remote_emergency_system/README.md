# Driverless Code Design Report

## INTRODUCTION
The RES is a system which is responsible for starting the self driving program for the car and in case of emergency stop the car.
This is done using a Radio from grossfunk. Exact details of the model are available in the competition handbook from FSG.
The Radio is included within the shutdown circuit.
The code for interpreting the messages that the Radio sends are included in this directory

## RULES AND DEMANDS
Rules regarding the RES can be found in the FSG rules under T14.3 Remote Emergency System
Further information about the RES can be found within the competition handbook section DE7.4

## RESEARCH
Research was conducted on CAN-Open and available python libraries for this. Aside from this research was done to figure out a way to test the system without having access to the physical radio.

## CODING PROCESS
Using the information about the messages that the radio will send within the competition handbook, code was written using the can and canopen python libraries. This code intercepts and reads these messages and based on the information within the CAN frames functions can be called which are supposed to pull the e-break or start the self driving program.

## TESTING
Since there was no physical access to the radio that needs to be used for the competition an alternative was designed. Using the Lely Core CANopen library the system was tested. Messages were recreated manually using this library and were sent over a virtual CAN bus while the interceptor.py script was running. It was observed that based on these messages the correct functions were called. The messages could be created based on the information within the competition handbook.

## CONLCUSION/DISCUSSION
A script which is capable of intepreting the messages that are sent from the RES Radio over a CAN bus has been written. This script currently does not call a function which activates the E-Break or activates the Self driving program because the code for this does not exist yet. Two functions have been created where this functionality can be implemented. For now all that happens are simple print statements.
More details about the code can be found within the Google Drive in the document RES Documentation.
