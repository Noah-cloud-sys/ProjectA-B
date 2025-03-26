# Program Name: ProgramA.py
# Course: IT3853/Section W04
# Student Name: David Touchstone
# Assignment Number: Lab4
# Date Due: 03/25/2025
# Purpose:
#   Connects to Program B, Which then prompts the user for a string, 
#   sends it, then prints the response received from Program B.
# List Specific resources used to complete the assignment:
#   - Python official docs: https://docs.python.org/3/library/socket.html
#https://realpython.com/python-sockets/
#https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client

import socket

def get_user_input(prompt="Type something For Program B to hear: "):
    
    return input(prompt)

def talk_to_server(ip="127.0.0.1", port=50000):
    """
    connecting server to the IP and port number.
    Send user input and receive the response.
    Return the response.
    """
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_sock.connect((ip, port))
        # message from the user
        user_message = get_user_input()
        
        # Send message to Program B
        client_sock.sendall(user_message.encode("utf-8"))
        
        # Receive the response from Program B
        response = client_sock.recv(1024)
        return response.decode("utf-8")
    finally:
        client_sock.close()

def main():
    # Connect, return the data and display the results
    result = talk_to_server()
    print("Program B's response:", result)

if __name__ == "__main__":
    main()
