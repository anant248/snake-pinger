# Group#: G7
# Student Names: Anant Goyal, Musa Habib

"""
    This program implements the client for a UDP Pinger 
"""

from socket import *
from time import time

serverName = "localhost"    # running on host 127.0.0.1
serverPort = 12000          # an available port

for i in range(5):
    clientSocket = socket(AF_INET,  SOCK_DGRAM) # create UDP socket for server
    initial_time = time() # time when message sending starts
    clientSocket.settimeout(1) # default timeout for new socket objects to be 1s

    try:
        message = "PING " + str(i+1) + " - hello world" 
        clientSocket.sendto(message.encode(), (serverName, serverPort)) # attach server name, port to message, send into socket
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # read reply characters from socket into a string
        clientSocket.close() # close the socket
        final_time = time() # time when message sending ends
        RTT = final_time - initial_time
        print("Round Trip Time (RTT): " + "{:.3f}".format(RTT) + "ms" + "   Sent message: " + message + "   Recieved message: " + modifiedMessage.decode()) # print the round trip time send and recieved messages

    except timeout:
        print("request timed out")
