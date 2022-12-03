# Group#: G7
# Student Names: Anant Goyal, Musa Habib

"""
    This program implements the server for a UDP Pinger 
"""

from socket import *
import time, random

if __name__=="__main__":
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)  # create UDP socket
    serverSocket.bind(('', serverPort)) # bind socket to local port number 12000
    print ("The server is ready to receive")

    while True: # loop forever
        message, clientAddress = serverSocket.recvfrom(2048)    # read from UDP socket into message, getting client's address (client IP and port)
        modifiedMessage = message.decode().replace("hello world", "ditto")  # replace 'hello world' in the incoming message with 'ditto'
        
        # wait for a random time delay before responding
        time.sleep(random.randint(5,50)/1000)
        
        # simulate 10% packet loss
        packet_loss_probability = random.randint(0,9)
        
        if packet_loss_probability > 0: # False if packet_loss_probability = 0
            serverSocket.sendto(modifiedMessage.encode(), clientAddress)    # send modified string back to client