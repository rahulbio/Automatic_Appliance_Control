import socket
import RPi.GPIO as GPIO

# Configure GPIO mode
GPIO.setmode(GPIO.BCM)

# Set GPIO pin for the bulb

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

# Server details
SERVER_HOST = '11.12.34.65'  # Replace with the actual server's IP address
SERVER_PORT = 65432

# Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print("Connected to the server.")

    # Receive and process messages from the server indefinitely
    while True:
        try:
            # Receive message from server
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                break  # Connection closed by server

            # Process YOLO output
            yolo_output = int(data[-1])
            fan = int(data[0])   # Extract YOLO output

            # If YOLO output is 1, turn on the bulb
            fans = [14,15,18,23]
            if yolo_output==1:
                GPIO.output(fans[fan], True)
                print(f"Bulb turned on in {fans[fan]}")
            else:
                GPIO.output(fans[fan], False)
                print(f"Bulb turned OFF in {fans[fan]}")

        except KeyboardInterrupt:
            print("Client shutting down...")
            break

# Clean up GPIO
GPIO.cleanup()
print("Client closed.")

