import random
import socket
import json
from time import time, sleep
from typing import Dict, Any

IP = "172.27.63.138" #IP from the RECEIVING PC
PORT = 5000


def generate_mockdata() -> Dict:

	vals_dict = {
		"ground_speed1": random.uniform(0,1),
		"ground_speed2": random.uniform(0,1),
		"wheel_encoders": random.randint(0,10),
		"steering_angle": random.randint(0,100),
		"accelorater_message": random.randint(0,100),
		"brake_message": random.randint(0,100),
		"camera_vals": "EXAMPLE"
	}
	return vals_dict


def send_json_message(
    sock: socket.socket,
    json_message: Dict[str, Any],
) -> None:
    """Send json packet to server"""
    message = (json.dumps(json_message) + '\n').encode()
    sock.sendall(message)
    #print(f'{len(message)} bytes sent')

def try_send():
    try:
        with socket.socket() as sock:
            sock.connect((IP, PORT))
            while True:
                json_message = generate_mockdata()
                send_json_message(sock, json_message)
                sleep(1)
    finally:
        print("Connection failed trying again in 10 seconds")
        sleep(10)
        try_send()

def main() -> None:
    try_send()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

