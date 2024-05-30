from scapy.all import *
try:
    host = input("Enter a host address: ")
    l = list(input("Enter the port to scan: ")).split(",")
    temp = map(int.p)
    ports = list(temp)
    
    