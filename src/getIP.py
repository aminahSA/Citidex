import socket

def get_ip_address():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Connect to an external server (in this case, Google DNS)
        s.connect(('8.8.8.8', 80))

        # Get the IP address of the socket
        ip_address = s.getsockname()[0]

        # Close the socket
        s.close()

        return ip_address
    except Exception as e:
        print(f"Error occurred while getting IP address: {e}")
        return None

# Get and print the IP address
flask_ip = get_ip_address()
print("Flask application IP address:", flask_ip)
