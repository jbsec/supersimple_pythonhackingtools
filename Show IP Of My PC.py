# Gather Your Own IP Address from Website URL
# Without fishing through CMD with commands. 

# My Version
# Semi colons arent required but existed in
# the tutorial.

"""
import socket;
print("Display Current Somputer's IP Address? (y/n): ");
check = input();
if check == 'n':
    #print("Exiting program...");
    exit();
if check == 'y':
    print("\nThe IP Address Of This Computer Is: ",end="");
    print(socket.gethostbyname(socket.gethostbyname()));
else:
    print("error.");
"""
# Python Program - Get IP Address (Original Code)

import socket
print("Show The IP Address of This Computer ? (y/n): ")
check = input()
if check == 'n':
    print("Exiting program...")
    exit()
else:
    print("\nYour IP Address is: ",end="")
    print(socket.gethostbyname(socket.gethostname()))