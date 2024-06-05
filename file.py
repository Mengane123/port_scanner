from scapy.all import *
try:
    host = input("Enter a host address: ")
    l = list(input("Enter the port to scan: ")).split(",")
    temp = map(int.l)
    ports = list(temp)

    if(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",host)):
        print("\n\nScanning...")
        print("Host: ",host)
        print("Ports: ",ports)

        ans,unans = sr(If(dst=host)/TCP(dport=ports,flags="S"),verbose=0 , timeout=2)
        for (s,r) in ans:
            print("[+] {} Open".format(s[TCP].dport))
            
    
    