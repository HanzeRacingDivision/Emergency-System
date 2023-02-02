import canopen
import can

driving_state = False

def set_operational():
	try:
		network.send_message(000, data=[0x01, 0x00])
	except:
		print("Message not sent")

def emergency_brake():
	print("E-Brake is pulled")

def start_self_driving():
	if(!driving_state):
		print("The car will start self driving program")
	else:
		print("The car is ready")

network = canopen.Network()

#Replace vcan0 here with real bus
bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=500000)

#Replace vcan0 here with real bus
network.connect(channel='vcan0', bustype='socketcan')

local_node = canopen.LocalNode(1, "/usr/local/etc/coctl.dcf")
network.add_node(local_node)


while True:
	msg = bus.recv()
	#Arbritration ID is without Node ID. Make sure to add the Node ID from the radio to the arbitration_id.
	#So if the radio has Node ID = 1 then arbitration_id needs to be 0x701
	if(msg.arbitration_id == 0x700):
		set_operational()
	if(msg.arbitration_id == 0x180):
		if(bin(msg.data[0])[2] == "1"):
			emergency_brake()
		#K2 switch. for K3 change to 2	
		if(bin(msg.data[0])[3] == "1"):
			start_self_driving()
		if(bin(msg.data[7][8]) == "1"):
			print("Signal Loss detected")
			print("Shutdown within 200ms")
