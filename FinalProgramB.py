# Program Name: ProgramB.py
# Course: IT3853/Section W04
# Student Name: David Touchstone
# Assignment Number: Lab4
# Date Due: 03/25/2025
# Purpose:
#   Program A connects to Program B, Program B receives a string, 
#   converts it to uppercase, and sends it back to Progam A.
# List Specific resources used to complete the assignment:
#   - Python official docs: https://docs.python.org/3/library/socket.html, 
# https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
#https://realpython.com/python-sockets/

import socket

def process_message(original_text):
    """Convert the text to uppercase and send it back."""
    return original_text.upper()

def start_server(ip="127.0.0.1", port=50000):
    """
    Create listening server that looks for a single connection.
    
    """
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_sock.bind((ip, port))
        server_sock.listen(1)
        print(f"Program B is listening {ip}:{port} ...")

        # Only One connection at a time
        while True:
            connection, address = server_sock.accept()
            print("Connection established with:", address)
            with connection:
                data = connection.recv(1024)
                if data:
                    # Convert data to uppercase
                    upper_text = process_message(data.decode("utf-8"))
                    # Send the uppercase string back
                    connection.sendall(upper_text.encode("utf-8"))
    finally:
        server_sock.close()

def main():
    start_server()

if __name__ == "__main__":
    main()
